values = {
        'false': 'true',
        'False': 'True',

        'true': 'false',
        'True': 'False',

        'on': 'off',
        'off': 'on',

        'yes': 'no',
        'no': 'yes',

        '1': '0',
        '0': '1'
        }

def toggle_bool_example(word):
    for key in values.keys():
      if key == word:
        word = values[key]
        break
    return word
