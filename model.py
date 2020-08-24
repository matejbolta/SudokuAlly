# _____           _       _           ___  _ _       
#/  ___|         | |     | |         / _ \| | |      
#\ `--. _   _  __| | ___ | | ___   _/ /_\ \ | |_   _ 
# `--. \ | | |/ _` |/ _ \| |/ / | | |  _  | | | | | |
#/\__/ / |_| | (_| | (_) |   <| |_| | | | | | | |_| |
#\____/ \__,_|\__,_|\___/|_|\_\\__,_\_| |_/_|_|\__, |
#                                               __/ |
#                                              |___/ 


# Konstante
'''...'''

# Primer sudoku mreže
tabela_1 = [
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

# POTREBNE FUNKCIJE OZ METODE
# Za iskanje prvega praznega polja v tabeli:
#   najdi_prazno_polje(tabela)
# Da v določenem polju preverimo ustreznost kandidata:
#   ustrezen(tabela, kandidat, polje)
# Glavna funkcija, ki reši mrežo:
#   resi(tabela)

def prikazi_tabelo(tabela):
    '''Prikaže tabelo v obliki, ki je berljiva za ljudi.'''
    for i in range(len(tabela)): # Vrstice
        if i % 3 == 0 and i != 0: # not i % 3 and bool(i)
            print('- - - - - - - - - - -')

        for j in range(len(tabela[0])): # Po eni vrstici
            if j % 3 == 0 and j != 0: # not j % 3 and bool(j)
                print('| ', end='')

            if j != 8:
                print(str(tabela[i][j]) + ' ', end='')
            else: # j == 8
                print(tabela[i][j])

# Navajeni smo, da koordinate vedno podajamo v obliki (x, y). Vendar pa se pri reševanju
# sudokuja uporablja standardna notacija, ki je oblike R1C1, kjer je R row (vrstica), C
# column (stolpec), pripadajoči številki pa zaporedna vrstica oz. stolpec. Ta notacija je
# seveda oblike (y, x). Primer: R3C6 pomeni polje v tretji vrstici in v šestem stolpcu.

def najdi_prazno_polje(tabela):
    '''V podani tabeli poišče prazno polje,in
       vrne njegove koordinate v obliki (y, x).
       Če praznih polj ni, vrne None'''
    for i in range(len(tabela)):
        for j in range(len(tabela[0])):
            if tabela[i][j] == 0:
                return (i, j)  # (vrstica, stolpec)
    return None

def ustrezen(tabela, kandidat, polje):
    '''Podamo tabelo, številko ki je preverjamo in koordinate.
       Funkcija vrne True/False glede na ustreznost kandidata'''
    # Preverimo vrstico
    for i in range(len(tabela[0])):
        if tabela[polje[0]][i] == kandidat and polje[1] != i:
            return False

    # Preverimo stolpec
    for i in range(len(tabela)):
        if tabela[i][polje[1]] == kandidat and polje[0] != i:
            return False

    # Preverimo boks
    boks_x = polje[1] // 3  # Vrednost 0 1 ali 2
    boks_y = polje[0] // 3  # Vrednost 0 1 ali 2

    for i in range(boks_x * 3, boks_x * 3 + 3): # Pravi trije indeksi na abscisi
        for j in range(boks_y * 3, boks_y * 3 + 3): # Pravi trije indeksi na ordinati
            if tabela[j][i] == kandidat and (j, i) != polje:
                return False
    
    # Če pridemo do konca je kandidat ustrezen
    return True

def resi(tabela):
    '''Z rekurzivnim klicem ("backtracking" algoritmom) reši tabelo in vrne True/False'''
    polje = najdi_prazno_polje(tabela)
    if polje is None:  # Našli smo rešitev
        return True
    else:
        vrstica, stolpec = polje

    for i in range(1, 10): # i je kandidat
        if ustrezen(tabela, i, polje):
            # Kandidat ustreza trenutni tabeli, ne pa še nujno končni reštvi
            tabela[vrstica][stolpec] = i

            # Poskusimo rešiti novo tabelo (rekurzivni klic)
            if resi(tabela):
                return True

            # Če ne pridemo do konca, je številka neustrezna, ponastavimo
            # polje poskusimo z naslednjim kandidatom.
            tabela[vrstica][stolpec] = 0

    return False # Nismo našli rešitve (tabela je nerešljiva)


# Prikaz tabele v začetnem in nato še rešenem stanju
TABELA = tabela_1
print('')
prikazi_tabelo(TABELA)
resi(TABELA)
print("\n+-+-+-+-+-+-+-+-+-+-+")
print('')
prikazi_tabelo(TABELA)
print('')






class Mreza:
    def __init__(self, tabela):
        self.tabela = tabela
    
    def najdi_prazno_polje(self):
        pass

    def ustrezen(self, kandidat, polje):
        pass

    def resi(self):
        pass

    def ugani_stevilko(self):
        pass
