import pymorphy3
from fastapi import APIRouter
import json

from nltk import word_tokenize
from nltk.corpus import stopwords



from src.presentation.schemas.models import InputData, SearchResponse, SearchRequest
from fastapi import HTTPException

import nltk
from nltk.stem import WordNetLemmatizer
from deep_translator import GoogleTranslator

from src.text_preprocessor.main import find_matching_ids_inverted, create_inverted_index, process_records, \
    preprocess_text

nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('WordNetLemmatizer')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('russian')).union(stopwords.words('english'))
translator = GoogleTranslator(source='auto', target='ru')

app = APIRouter()

@app.post("/filter", response_model=SearchResponse)
async def search_users(request: SearchRequest):
    data = request.data
    prompt = request.prompt

    morph = pymorphy3.MorphAnalyzer()
    stop_words = set(stopwords.words('russian')).union(set(stopwords.words('english')))
    stop_words.difference_update({'не', 'нет'})

    # Предобработка данных
    processed_data = process_records(data, morph, stop_words)
    processed_prompt = preprocess_text(prompt, morph, stop_words)

    # Пороговые условия
    original_tokens = word_tokenize(prompt, language="russian")
    original_count = len(original_tokens)
    preprocessed_count = len(processed_prompt)

    if original_count == 3 and preprocessed_count == 2:
        threshold = 0.5
    elif original_count == 2 and preprocessed_count == 2:
        threshold = 0.6
    elif original_count > 3:
        threshold = 0.7
    elif original_count > 5:
        threshold = 0.8
    else:
        threshold = 0.5

    min_matches = max(1, int(len(processed_prompt) * threshold))

    # Создание инвертированного индекса
    inverted_index = create_inverted_index(processed_data)

    # Поиск подходящих идентификаторов
    matching_ids = find_matching_ids_inverted(inverted_index, processed_prompt, min_matches)

    # Формирование результата
    matching_ids_name = {record['id']: record['first_name'] + " " + record['last_name']
                         for record in data['filtered_employees'] if record['id'] in matching_ids}

    return SearchResponse(matching_ids_name=matching_ids_name)