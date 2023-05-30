translation_dict = {
    'q': '�',
    'w': '�',
    'e': '�',
    'r': '�',
    't': '�',
    'y': '�',
    'u': '�',
    'i': '�',
    'o': '�',
    'p': '�',
    '[': '�',
    ']': '�',
    'a': '�',
    's': '�',
    'd': '�',
    'f': '�',
    'g': '�',
    'h': '�',
    'j': '�',
    'k': '�',
    'l': '�',
    ';': '�',
    'z': '�',
    'x': '�',
    'c': '�',
    'v': '�',
    'b': '�',
    'n': '�',
    'm': '�',
    ',': '�',
    '.': '�',
}


def convert_to_russian(text):
    translated_text = ''
    
    for char in text:
        translated_char = translation_dict.get(char.lower(), char)
        translated_text += translated_char
    
    return translated_text


def convert_to_english(text):
    reverse_translation_dict = {v: k for k, v in translation_dict.items()}
    
    translated_text = ''
    
    for char in text:
        translated_char = reverse_translation_dict.get(char.lower(), char)
        translated_text += translated_char
    
    return translated_text

#ip
english_text = 'hello ������ ����� ghbdtn'
russian_text = convert_to_russian(english_text)
print(russian_text)  # rc

converted_back = convert_to_english(russian_text)
print(converted_back)  # ec