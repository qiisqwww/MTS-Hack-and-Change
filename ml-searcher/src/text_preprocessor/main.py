import json
from nltk.tokenize import word_tokenize
import string

__all__=[
    "load_json",
    "translate_text",
    "preprocess_text",
    "format_birthdate",
    "process_records",
    "find_matching_ids"
]

def load_json(json_input):
    """Загружает данные из JSON строки."""
    return json.loads(json_input)


def translate_text(text, translator):
    """
    Переводит весь текст на английский язык.
    """
    translated = translator.translate(text)
    return translated.lower()


def preprocess_text(text, lemmatizer, stop_words):
    """
    Выполняет предварительную обработку текста:
    - Приведение к нижнему регистру
    - Удаление пунктуации и цифр
    - Токенизация
    - Удаление стоп-слов
    - Лемматизация
    """
    if not isinstance(text, str):
        return set()

    # Приведение к нижнему регистру
    text = text.lower()

    # Удаление пунктуации
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Токенизация
    tokens = word_tokenize(text)

    # Удаление стоп-слов
    tokens = [word for word in tokens if word not in stop_words]

    # Лемматизация
    lemmas = [lemmatizer.lemmatize(word) for word in tokens]

    return set(lemmas)


def format_birthdate(text):
    """
    Заменяет точки в дате рождения на пробелы.
    """
    return text.replace('.', ' ')


def process_records(data, lemmatizer, stop_words, translator):
    """
    Обрабатывает все записи:
    - Объединяет все строковые значения в одной записи
    - Переводит объединенный текст на английский
    - Предобрабатывает переведенный текст
    """
    processed = {}
    for record in data['filtered_employees']:
        # Объединение всех строковых полей
        combined = ' '.join([format_birthdate(str(value)) if 'birthdate' in key else str(value) for key, value in record.items() if isinstance(value, str)])

        # Перевод всего текста
        translated_text = translate_text(combined, translator)

        # Предобработка переведенного текста
        processed[record['id']] = preprocess_text(translated_text, lemmatizer, stop_words)
    return processed


def process_prompt(prompt, lemmatizer, stop_words, translator):
    """
    Обрабатывает поисковый запрос:
    - Переводит запрос на английский
    - Предобрабатывает переведенный текст
    """
    translated_prompt = translate_text(prompt, translator)
    return preprocess_text(translated_prompt, lemmatizer, stop_words)


def find_matching_ids(processed_data, processed_prompt, threshold):
    """
    Ищет идентификаторы записей, которые соответствуют запросу по заданному порогу совпадений.
    """
    matching_ids = []
    for uid, words in processed_data.items():
        matches = len(words & processed_prompt)
        ratio = matches / len(processed_prompt) if processed_prompt else 0
        if ratio >= threshold:
            matching_ids.append(uid)
    return matching_ids

