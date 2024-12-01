import pymorphy3
from fastapi import APIRouter
import json

from nltk import word_tokenize
from nltk.corpus import stopwords

from src.presentation.schemas.models import InputData, SearchResponse, SearchRequest, FilterResponse, FilterRequest
from fastapi import HTTPException

import nltk
from nltk.stem import WordNetLemmatizer

from src.text_preprocessor.main import find_users

nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('WordNetLemmatizer')

app = APIRouter()
@app.post("/filter", response_model=FilterResponse)
def filter_users(request: SearchRequest):
    matching_ids = find_users(request.data["filtered_employees"], request.prompt, 0.3)
    return FilterResponse(matching_ids=matching_ids)