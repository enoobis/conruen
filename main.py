translation_dict = {
    'q': 'й',
    'w': 'ц',
    'e': 'у',
    'r': 'к',
    't': 'е',
    'y': 'н',
    'u': 'г',
    'i': 'ш',
    'o': 'щ',
    'p': 'з',
    '[': 'х',
    ']': 'ъ',
    'a': 'ф',
    's': 'ы',
    'd': 'в',
    'f': 'а',
    'g': 'п',
    'h': 'р',
    'j': 'о',
    'k': 'л',
    'l': 'д',
    ';': 'ж',
    'z': 'я',
    'x': 'ч',
    'c': 'с',
    'v': 'м',
    'b': 'и',
    'n': 'т',
    'm': 'ь',
    ',': 'б',
    '.': 'ю',
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
english_text = 'hello ïðèâåò ðóääù ghbdtn'
russian_text = convert_to_russian(english_text)
print(russian_text)  # rc

converted_back = convert_to_english(russian_text)
print(converted_back)  # ec
