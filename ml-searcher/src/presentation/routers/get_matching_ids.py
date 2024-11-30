from fastapi import APIRouter
import json

from nltk.corpus import stopwords

from src.text_preprocessor import process_records
from src.text_preprocessor.main import process_prompt, find_matching_ids
from src.text_preprocessor.models import InputData
from fastapi import HTTPException

import nltk
from nltk.stem import WordNetLemmatizer
from deep_translator import GoogleTranslator

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

@app.post("/find-users")
def find_users_endpoint(input_data: InputData):
    try:
        # Преобразование входных данных
        data_dict = input_data.dict()

        # Обработка записей
        processed_data = process_records(data_dict, lemmatizer, stop_words, translator)

        # Обработка поискового запроса
        processed_prompt = process_prompt(input_data.prompt, lemmatizer, stop_words, translator)

        # Поиск совпадающих идентификаторов
        matching_ids = find_matching_ids(processed_data, processed_prompt, 0.7)

        return {"matching_ids": matching_ids}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
