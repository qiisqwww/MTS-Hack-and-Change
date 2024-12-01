import json
import string
import pymorphy3
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')

# Вспомогательные функции
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
    for record in data:
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

        processed_tokens[record["id"]] = final_tokens

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


def find_matching_ids_inverted(inverted_index, processed_prompt, min_matches=1):
    matches = {}
    for word in processed_prompt:
        if word in inverted_index:
            for user_id in inverted_index[word]:
                if user_id not in matches:
                    matches[user_id] = 0
                matches[user_id] += 1
    filtered = {user_id: count for user_id, count in matches.items() if count >= min_matches}

    return filtered


def find_users(filtered_employees, prompt, threshold=0.5):
    morph = pymorphy3.MorphAnalyzer()
    stop_words = set(stopwords.words('russian')).union(set(stopwords.words('english')))
    stop_words.difference_update({'не', 'нет'})

    processed_prompt = preprocess_text(prompt, morph, stop_words)

    min_matches = max(1, int(len(processed_prompt) * threshold))

    processed_data = process_records(filtered_employees, morph, stop_words)

    inverted_index = create_inverted_index(processed_data)

    matching_dict = find_matching_ids_inverted(inverted_index, processed_prompt, min_matches=min_matches)

    if not matching_dict:
        return []

    max_count = max(matching_dict.values())

    top_ids = [user_id for user_id, count in matching_dict.items() if count == max_count]

    return top_ids