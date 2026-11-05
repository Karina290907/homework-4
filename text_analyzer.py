import re
from collections import Counter

def analyze_text(file_path: str) -> dict:
    """
    Читає текст із файлу, визначає кількість слів та їх частотність.
    Обробляє помилки читання та порожні файли.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        return {"error": "Помилка: Файл не знайдено."}
    except Exception as e:
        return {"error": f"Помилка читання файлу: {e}"}

    # Перевірка на порожній текст
    if not text.strip():
        return {"error": "Помилка: Файл порожній."}

    # Регулярний вираз для пошуку слів (підтримує українську та англійську мови)
    words = re.findall(r'\b\w+\b', text.lower())

    word_count = len(words)
    frequency = dict(Counter(words))

    return {
        "word_count": word_count,
        "frequency": frequency
    }

if __name__ == "__main__":
    result = analyze_text("input.txt")
    if "error" in result:
        print(result["error"])
    else:
        print(f"Загальна кількість слів: {result['word_count']}")
        print("Частотність слів:")
        for word, count in sorted(result['frequency'].items(), key=lambda item: item[1], reverse=True)[:15]:
            print(f"'{word}': {count}")