import requests
import random

def get_word_data():
    # Список слів, з яких випадково вибирається одне
    word_list = ["elated", "resilient", "serendipity", "benevolent", "meticulous"]
    word = random.choice(word_list)

    # Запит до Free Dictionary API
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        definition = data["meanings"][0]["definitions"][0]["definition"]
        example = data["meanings"][0]["definitions"][0].get("example", "No example available.")
        phonetic = data.get("phonetic", "")
        audio = ""

        # Пошук аудіо-вимови
        for phon in data.get("phonetics", []):
            if phon.get("audio"):
                audio = phon["audio"]
                break

        return {
            "word": word,
            "transcription": phonetic,
            "translation": "",  # Можна додати переклад через Google Translate API
            "example": example,
            "audio": audio
        }
    else:
        # Якщо API не відповідає — повертаємо заглушку
        return {
            "word": word,
            "transcription": "",
            "translation": "",
            "example": "Слово не знайдено.",
            "audio": ""
        }