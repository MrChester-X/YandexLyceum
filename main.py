MorseCode = {
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
    " ": " "
}

text_welcome = \
    """\
Привет! Я мини-программа, работающая с азбукой Морзы\n
Выбери действие, которое хочешь сделать:
1) Перевести текст на азбуку Морзе"""

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


def print_wait_continue():
    print(text_wait_continue)
    input()


def encode_to_morse(text):
    array = []
    for i in range(len(text)):
        if text[i].upper() in MorseCode.keys():
            array.append(MorseCode[text[i].upper()])
    return " ".join(array)


def main():
    while True:
        print(text_welcome)
        choose = int(input())

        if choose == 1:
            print(text_wait_text)
            text = input()
            print(encode_to_morse(text))
            print_wait_continue()
        else:
            print(text_error)
            print_wait_continue()


main()
