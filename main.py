# Сделано вместе с Валерией Заугловой
# GitHub: https://github.com/MrChester-X/YandexLyceum

# По всемирным стандартам:
# 1) Между каждой буквой соблюдается один пробел
# 2) Между каждым словом соблюдается три пробела
# 3) Все буквы рассматриваются в верхнем регстре

# Было сделано 3 словаря для дальнейшей удобной работы с ними
# Так, при декодировании, русские и англ расшифровки совпадают, значит надо выбирать язык при таких операциях
# Можно совмещать словари в самых разных комбинациях

# Библиотека Азбуки Морзы (англ)
MorseCode_En = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

# Библиотека Азбуки Морзы (ру)
MorseCode_Ru = {
    "А": ".-",
    "Б": "-...",
    "В": ".--",
    "Г": "--.",
    "Д": "-..",
    "Е": ".",
    "Ж": "...-",
    "З": "--..",
    "И": "..",
    "Й": ".---",
    "К": "-.-",
    "Л": ".-..",
    "М": "--",
    "Н": "-.",
    "О": "---",
    "П": ".--.",
    "Р": ".-.",
    "С": "...",
    "Т": "-",
    "У": "..-",
    "Ф": "..-.",
    "Х": "····",
    "Ц": "-.-.",
    "Ч": "−−−·",
    "Ш": "----",
    "Щ": "--.-",
    "Ъ": "−−·−−",
    "Ы": "-.--",
    "Ь": "-..-",
    "Э": "··−··",
    "Ю": "··−−",
    "Я": "·−·−",
}

# Библиотека Азбуки Морзы (знаки и остальное)
MorseCode_Other = {
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": "......",
    ",": ".-.-.-",
    ":": "---...",
    ";": "-.-.-.",
    "(": "-.--.-",
    ")": "-.--.-",
    "-": "-....-",
    "_": "..--.-",
    "?": "..--..",
    "!": "--..--",
    "+": ".-.-.",
    "@": ".--.-.",
    " ": " ",
}

# Текста, используемые программой
text_welcome = \
    """\
Привет! Я мини-программа, работающая с азбукой Морзы\n
Выбери действие, которое хочешь сделать:
1) Перевести текст на азбуку Морзе
2) Перевести текст с Морзы на русский
3) Перевести текст с Морзы на английский"""

text_wait_text = \
    """\
Отлично, теперь впиши текст в поле ниже:"""

text_error = \
    """\
Ошибочка =((((((
Такой настройки нет.\n"""

text_wait_continue = \
    """\
Нажми Enter для продолжения..."""


# Получаем ту самую комбинацию словарей
def get_dict_by_lang(lang):
    temp_codes = {}
    if lang == "all":
        temp_codes.update(MorseCode_Ru)
        temp_codes.update(MorseCode_En)
        temp_codes.update(MorseCode_Other)
    elif lang == "ru":
        temp_codes.update(MorseCode_Ru)
        temp_codes.update(MorseCode_Other)
    elif lang == "en":
        temp_codes.update(MorseCode_En)
        temp_codes.update(MorseCode_Other)
    return temp_codes


# Делаем ожидание ввода Enter одной функцией
def print_wait_continue():
    print(text_wait_continue)
    input()


# Ждем от пользователя ввода текста + пишем ему об этом
def input_wait():
    print(text_wait_text)
    return input()


# Создаем новый словарь, в котором ключи и значения поменялись местами (для декодирования)
def dict_invert(use_dict):
    new_dict = {}
    for key, value in use_dict.items():
        new_dict[value] = key
    return new_dict


# Кодирование текста в Азбуку Морзы
def encode_to_morse(text):
    array = []
    temp_codes = get_dict_by_lang("all")
    for i in range(len(text)):
        if text[i].upper() in temp_codes.keys():
            array.append(temp_codes[text[i].upper()])
    return " ".join(array)


def decode_from_morse(text, lang):
    temp_codes = dict_invert(get_dict_by_lang(lang))
    array = [i.split(" ") for i in text.split("   ")]
    for i in range(len(array)):
        for x in range(len(array[i])):
            if array[i][x] in temp_codes:
                array[i][x] = temp_codes[array[i][x]]
    return " ".join(["".join(i) for i in array])


# Делаем функцию, которая дает пользователю бесконечно пользоваться программой
def main():
    while True:
        print(text_welcome)
        choose = int(input())

        if choose == 1:
            text = input_wait()
            print(encode_to_morse(text))
            print_wait_continue()
        elif choose == 2:
            text = input_wait()
            print(decode_from_morse(text, "ru"))
            print_wait_continue()
        elif choose == 3:
            text = input_wait()
            print(decode_from_morse(text, "en"))
            print_wait_continue()
        else:
            print(text_error)
            print_wait_continue()


# Запускаем нашу программу =)
main()
