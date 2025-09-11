'''
Napisite program koji ispisuje bozicno drvce, a korisnik moze birati znak i visinu

Primjer:
Visina je 8
Znak je *

       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
     | | |
     | | |
'''


'''height = int(input('Upisi visinu: '))
symbol = input('Unesi simbol: ')

for i in range(height):
    razmaci =  ' ' * (height - i - 1)
    broj_znakova = 2 * i + 1

    print(razmaci + symbol * broj_znakova)

deblo_sirina = 3
deblo_visina = 2

for j in range(deblo_visina):
    razmaci_deblo = ' ' * (height - 2)'''

height = 10
symbol = '*'

# height = int(input('Upisite visinu jelke: '))
# symbol = input('Upisite znak: ')

for i in range(1, height + 1):       # 0 - 10
    # Ispis praznina
    print(' ' * (height - i), end='')

    # Ispis zvjezdica
    #print(symbol * ((i * 2) -1))
    for j in range(1, i):
        print(symbol * (j - 1), end='')
          

for j in range(3):
    print(' ' * (height - 2), end='')
    print('|' * 3)