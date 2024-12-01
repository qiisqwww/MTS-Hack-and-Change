from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import json
import string
import pymorphy3
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Убедитесь, что необходимые ресурсы NLTK загружены
nltk.download('stopwords')
nltk.download('punkt_tabs')


def is_email(text):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_pattern, text) is not None


def extract_emails(text):
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    return re.findall(email_pattern, text.lower())


def preprocess_text(text, morph, stop_words):
    if not isinstance(text, str):
        return set()

    if is_email(text):
        return {text}

    text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    tokens = word_tokenize(text, language="russian")
    tokens = [word for word in tokens if word not in stop_words]
    lemmas = [morph.parse(word)[0].normal_form for word in tokens]

    return set(lemmas)


def process_records(data, morph, stop_words):
    processed_tokens = {}
    for record in data['filtered_employees']:
        words = set()
        for key, value in record.items():
            if isinstance(value, str):
                if key == 'email':
                    words.add(value)
                else:
                    emails = extract_emails(value)
                    words.update(emails)
                    tokens = word_tokenize(value, language="russian")
                    words.update(tokens)

        non_email_words = [w for w in words if not is_email(w)]
        lemmas = preprocess_text(' '.join(non_email_words), morph, stop_words)
        final_tokens = lemmas.union({w for w in words if is_email(w)})

        processed_tokens[record['id']] = final_tokens

    return processed_tokens


def create_inverted_index(processed_data):
    inverted_index = {}
    for record_id, lemmas in processed_data.items():
        for lemma in lemmas:
            if lemma in inverted_index:
                inverted_index[lemma].add(record_id)
            else:
                inverted_index[lemma] = {record_id}
    return inverted_index


def find_matching_ids_inverted(index, processed_prompt, min_matches=1):
    record_counts = {}
    for lemma in processed_prompt:
        if lemma in index:
            for record_id in index[lemma]:
                record_counts[record_id] = record_counts.get(record_id, 0) + 1
    return [record_id for record_id, count in record_counts.items() if count >= min_matches]

