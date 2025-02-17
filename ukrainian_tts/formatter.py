import num2words
import re


def preprocess_text(text):
    text = text.lower()
    # currencies
    text = text.replace("$", "долар")
    text = text.replace("₴", "гривня")
    text = text.replace("€", "євро")
    # replace apostrophe
    text = text.replace("`", "'")
    text = text.replace("ʼ", "'")
    text = text.replace("…", "...")

    symbols = {
        "”": '"',
        "“": '"',
        "’": '"',
        "‘": '"',
        "«": '"',
        "»": '"',
        "–": "-",
        "—": "-",
        "―": "-",
    }
    for symbol, value in symbols.items():
        text = text.replace(symbol, value)
    # numbers
    text = re.sub(r"(\d)\s+(\d)", r"\1\2", text)

    def detect_num_and_convert(word):
        numbers = "0123456789,."
        result = []
        parts = word.split("-")  # for handling complex words
        for part in parts:
            is_number = all(map(lambda x: x in numbers, part))
            if is_number:
                try:
                    result.append(num2words.num2words(part, lang="uk"))
                except:
                    result.append(part)
            else:
                result.append(part)
        return "-".join(result)

    # print([detect_num_and_convert(word) for word in text.split(" ")])
    text = " ".join([detect_num_and_convert(word) for word in text.split(" ")])

    # fallback numbers
    text = text.replace("1", "один ")
    text = text.replace("2", "два ")
    text = text.replace("3", "три ")
    text = text.replace("4", "чотири ")
    text = text.replace("5", "п'ять ")
    text = text.replace("6", "шість ")
    text = text.replace("7", "сім ")
    text = text.replace("8", "вісім ")
    text = text.replace("9", "дев'ять ")
    text = text.replace("0", "нуль ")
    # speak english alphabet using brute force transliteration
    english = {
        "qu": "кв",
        "ch": "ч",
        "sh": "ш",
        "ph": "ф",
        "kh": "х",
        "a": "а",
        "b": "б",
        "c": "ц",
        "d": "д",
        "e": "е",
        "f": "ф",
        "g": "ґ",
        "h": "г",
        "i": "і",
        "j": "дж",
        "k": "к",
        "l": "л",
        "m": "м",
        "n": "н",
        "o": "о",
        "p": "п",
        "q": "кв",
        "r": "р",
        "s": "с",
        "t": "т",
        "u": "ю",
        "v": "в",
        "w": "в",
        "x": "кс",
        "y": "і",
        "z": "з",
    }
    for english_char, english_value in english.items():
        # uppercase
        text = text.replace(english_char.upper(), english_value.upper())
        text = text.replace(english_char, english_value)

    return text
