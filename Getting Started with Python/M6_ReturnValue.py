def greet(lang):
    if lang == 'en':
        return 'Hello'
    elif lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('fr'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('oi'), 'Sakib')