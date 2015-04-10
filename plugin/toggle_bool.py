values = {
        'false': 'true',
        'true': 'false',

        'on': 'off',
        'off': 'on',

        'yes': 'no',
        'no': 'yes',

        '1': '0',
        '0': '1'
        }

def toggle_bool_value(word):
    toggleWord = word
    for key in values.keys():
      if key == word.lower():
        toggleWord = values[key]
        if word.isupper():
          toggleWord = toggleWord.upper()
        elif word.istitle():
          toggleWord = toggleWord.title()
        break
    return toggleWord
