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


height = int(input('Upisi visinu: '))
symbol = input('Unesi simbol: ')

for i in range(height):
    razmaci =  ' ' * (height - i - 1)
    broj_znakova = 2 * i + 1

    print(razmaci + symbol * broj_znakova)

deblo_sirina = 3
deblo_visina = 2

for j in range(deblo_visina):
    razmaci_deblo = ' ' * (height - 2)
    