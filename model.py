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
# najdi_prazno_polje(tabela)
# Da v določenem polju preverimo ustreznost kandidata:
# ustrezen(tabela, kandidat, polje)
# Glavna funkcija, ki reši mrežo
# resi(tabela)

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
    