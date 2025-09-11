'''
Napisite program koji trazi od korisnika da pogodi koju rijec je "zamislio".
Ako korisnik upise znak ? onda mu ispisite prvo slovo zamisljene rijeci HINT [0]
'''

hidden_word = 'Python'

user_guess = input('Koju rijec sam zamislio: ')

if user_guess.upper() == hidden_word.upper():
    print(f'Pogodili ste!!! Bravo!!! Zamisljena rijec je {hidden_word}!')
else:
    print(f'Na zalost niste pogodili zamisljenu rijec. Pokusajte ponovno.')