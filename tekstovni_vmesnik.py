#        5 3 6 | 1 2 4 | 7 9 8
#        2 7 8 | 6 5 9 | 4 3 1
#        9 1 4 | 7 3 8 | 6 2 5
#        - - - - - - - - - - -
#        1 2 5 | 9 7 6 | 8 4 3
#        4 6 7 | 3 8 5 | 2 1 9
#        8 9 3 | 2 4 1 | 5 7 6
#        - - - - - - - - - - -
#        7 5 2 | 8 9 3 | 1 6 4
#        6 8 9 | 4 1 7 | 3 5 2
#        3 4 1 | 5 6 2 | 9 8 7

import model

# !!!
# OPOMBA:
# TEKSTOVNI VMESNIK NI DODELAN IN JE NAREJEN
# LE KOT POMOČ PRI RAZVIJANJU PROJEKTA
# !!!

LOGO = '''
 _____           _       _           ___  _ _       
/  ___|         | |     | |         / _ \| | |      
\ `--. _   _  __| | ___ | | ___   _/ /_\ \ | |_   _ 
 `--. \ | | |/ _` |/ _ \| |/ / | | |  _  | | | | | |
/\__/ / |_| | (_| | (_) |   <| |_| | | | | | | |_| |
\____/ \__,_|\__,_|\___/|_|\_\\__,_\_| |_/_|_|\__, |
                                               __/ |
                                              |___/ 
'''
# Trije primeri sudoku mreže (tabele)

tabela_1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]
tabela_2 = [
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 8, 6, 5, 9, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 2, 0],
    [1, 0, 0, 9, 0, 6, 0, 4, 0],
    [0, 0, 7, 0, 8, 0, 2, 0, 0],
    [0, 9, 0, 2, 0, 1, 0, 0, 6],
    [0, 5, 0, 0, 0, 0, 0, 6, 0],
    [6, 0, 0, 4, 1, 7, 3, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
]
tabela_3 = [
    [0, 1, 0, 0, 0, 0, 0, 2, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 4, 5, 0, 2, 1, 0, 0],
    [0, 0, 6, 4, 0, 5, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 3, 0, 6, 5, 0, 0],
    [0, 0, 5, 6, 0, 4, 3, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 8, 0, 0, 0, 0, 0, 9, 0],
]


# Olepšave besedila v vmesniku

def krepko(niz):
    return f'\033[1m{niz}\033[0m'

def modro(niz):
    return f'\033[1;94m{niz}\033[0m'

def rdece(niz):
    return f'\033[1;91m{niz}\033[0m'


# Sestavni deli uporabniškega vmesnika

def glavni_meni():
    print(krepko(LOGO))
    print(krepko('Pozdravljeni v programu SudokuAlly!'))
    print('Za izhod pritisnice Ctrl-C.\n')
    mreza = model.Mreza(vnos_mreze())
    mreza.resi(mreza.resena_tabela)
    while True:
        try:
            print(modro('\nVaša mreža:'))
            print(mreza)
            izbira = input('''\nKaj želiš storiti:\n(1) Reši celotno mrežo!\n(2) Reši naključno polje!\n(3) Reši točno določeno polje!\n> ''')
            if izbira == '1':
                resi_mrezo(mreza)
                vnos_mreze()
            elif izbira == '2':
                nakljucno_polje(mreza)
            elif izbira == '3':
                doloceno_polje(mreza)
            else:
                print(rdece('\nVnesi eno izmed števil 1, 2, 3!\n'))
        except KeyboardInterrupt:
            print()
            print(modro('Nasvidenje!'))
            return # None

def vnos_mreze():
    print(modro('''Vnesi sudoku mrežo na naslednji način: po vsaki vrstici\npritisni enter ter namesto praznih polj vtipkaj 0.\n'''))
    print('''Primer:\n780400120\n600075009\n000601078\n007040260\n001050930\n904060005\n070300012\n120007400\n049206007\n''')
    v1 = input('Prva vrsta > ')
    v2 = input('Druga vrsta > ')
    v3 = input('Tretja vrsta > ')
    v4 = input('Četrta vrsta > ')
    v5 = input('Peta vrsta > ')
    v6 = input('Šesta vrsta > ')
    v7 = input('Sedma vrsta > ')
    v8 = input('Osma vrsta > ')
    v9 = input('Deveta vrsta > ')
    vrste = [v1,v2,v3,v4,v5,v6,v7,v8,v9]
    mreza = [[stevilo for stevilo in vrsta] for vrsta in vrste]
    # Pomoč za razvijalce
    mreza = [
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 8, 6, 5, 9, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 2, 0],
        [1, 0, 0, 9, 0, 6, 0, 4, 0],
        [0, 0, 7, 0, 8, 0, 2, 0, 0],
        [0, 9, 0, 2, 0, 1, 0, 0, 6],
        [0, 5, 0, 0, 0, 0, 0, 6, 0],
        [6, 0, 0, 4, 1, 7, 3, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
    ]
    return mreza

def resi_mrezo(mreza):
    mreza.tabela = mreza.resena_tabela
    print(modro('\nRešena mreža:'))
    print(mreza)
    print(55 * '=')
    return

def nakljucno_polje(mreza):
    mreza.resi_nakljucno_polje()
    print(modro('\nTrenutna mreža:'))
    print(mreza)
    print(55 * '=')
    return

def doloceno_polje(mreza):



    y = input(modro('Vrstica (1-9) > '))
    y = int(y) - 1
    x = input(modro('Stolpec (1-9) > '))
    x = int(x) - 1
    mreza.resi_doloceno_polje((y, x))
    print(modro('\nTrenutna mreža:'))
    print(mreza)
    print(55 * '=')
    return

glavni_meni()