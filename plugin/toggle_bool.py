values = {
    'true': 'false',
    'on': 'off',
    'yes': 'no',
    '1': '0',
}


def format_value(word, toggleWord):
    if word.isupper():
        toggleWord = toggleWord.upper()
    elif word.istitle():
        toggleWord = toggleWord.title()
    return toggleWord


def toggle_bool_value(word):
    toggleWord = word
    for key in values.keys():
        if key == word.lower():
            toggleWord = values[key]
            toggleWord = format_value(word, toggleWord)
            break
        elif values[key] == word.lower():
            toggleWord = key
            toggleWord = format_value(word, toggleWord)
            break
    return toggleWord
