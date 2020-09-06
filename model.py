# _____           _       _           ___  _ _       
#/  ___|         | |     | |         / _ \| | |      
#\ `--. _   _  __| | ___ | | ___   _/ /_\ \ | |_   _ 
# `--. \ | | |/ _` |/ _ \| |/ / | | |  _  | | | | | |
#/\__/ / |_| | (_| | (_) |   <| |_| | | | | | | |_| |
#\____/ \__,_|\__,_|\___/|_|\_\\__,_\_| |_/_|_|\__, |
#                                               __/ |
#                                              |___/ 

import random, json

# Konstante
LOGOTIP = r'''
 _____           _       _           ___  _ _       
/  ___|         | |     | |         / _ \| | |      
\ `--. _   _  __| | ___ | | ___   _/ /_\ \ | |_   _ 
 `--. \ | | |/ _` |/ _ \| |/ / | | |  _  | | | | | |
/\__/ / |_| | (_| | (_) |   <| |_| | | | | | | |_| |
\____/ \__,_|\__,_|\___/|_|\_\\__,_\_| |_/_|_|\__, |
                                               __/ |
                                              |___/ 
'''
DATOTEKA_S_STANJEM = 'stanje.json'
# Pomoč za ocenjevalca: prednastavljeno stanje
# je shranjeno v spodnji datoteki.
# DATOTEKA_S_STANJEM = 'stanje_prednastavljeno.json'
ZACETEK = 'zacetno_stanje'
NAPACEN_UGIB = 'ugib_je_napacen'
ZAPOLNJENO_POLJE = 'polje_je_zapolnjeno'
PRAVILEN_UGIB = 'ugib_je_pravilen'
NEVELJAVEN_VNOS = 'vnos_je_neveljaven'
USPESNA_POMOC = 'pomoc_je_uspesna'
RESEN_SUDOKU = 'sudoku_je_resen'
PRAZNA_TABELA = [[0 for _ in range(9)] for _ in range(9)]

# Navajeni smo, da koordinate vedno podajamo v obliki (x, y). Vendar 
# pa se pri reševanju sudokuja uporablja standardna notacija, ki je 
# oblike R1C1, kjer je R row (vrstica), C column (stolpec), 
# pripadajoči številki pa zaporedna vrstica oz. stolpec. Ta notacija 
# je seveda oblike (y, x). Primer: R3C6 pomeni polje v tretji vrstici 
# in v šestem stolpcu. Naše oznake pa bodo med (0, 0) in (8, 8).

class Mreza:
    '''Predstavlja eno sudoku mrežo. Vsebuje začetno, trenutno in 
    rešeno tabelo'''
    def __init__(self, zacetna_tabela, tabela=None, resena_tabela=None):
        self.zacetna_tabela = zacetna_tabela
        if tabela:
            self.tabela = tabela
        else:
            self.tabela = [[stevilo for stevilo in vrstica] for 
            vrstica in zacetna_tabela]
        if resena_tabela:
            self.resena_tabela = resena_tabela
        else:
            self.resena_tabela = [[stevilo for stevilo in vrstica] 
            for vrstica in zacetna_tabela]
            self.resi(self.resena_tabela)

    def __repr__(self):
        '''Prikaže mrežo v obliki gnezdenega seznama.'''
        return f'{self.tabela}'
    
    def __str__(self):
        '''Prikaže mrežo v obliki, ki je berljiva za ljudi.'''
        izpis = '\n'
        for i in range(len(self.tabela)): # Vrstice
            if i % 3 == 0 and i != 0: # not i % 3 and bool(i)
                izpis += 10 * '- ' + '-\n'

            for j in range(len(self.tabela[0])): # Po eni vrstici
                if j % 3 == 0 and j != 0: # not j % 3 and bool(j)
                    izpis += '| '

                if j != 8:
                    izpis += str(self.tabela[i][j]) + ' '
                else: # j == 8
                    izpis += str(self.tabela[i][j]) + '\n'
        return izpis

    def najdi_prazno_polje(self, tabela):
        '''V dani tabeli poišče prazno polje, in vrne njegove 
        koordinate v obliki (y, x). Če praznih polj ni, vrne None. 
        tabela = (self.tabela / self.zacetna_tabela)'''
        for i in range(len(tabela)):
            for j in range(len(tabela[0])):
                if not tabela[i][j]:
                    return (i, j)  # (vrstica, stolpec)
        return # None

    def ustreznost_tabele_osnovno(self, tabela):
        '''Preveri, ali je tabela v podani mreži ustrezna (brez
        ponovljenih številk). Vrne True/False.'''
        for i in range(9):
            for j in range(9):
                if tabela[i][j] and not self.ustrezen(tabela[i][j], 
                (i, j), tabela):
                    return False
        return True

    def ustreznost_tabele_napredno(self):
        '''Preveri, ali je začetna tabela v podani mreži rešljiva (ima 
        najmanj eno končno rešitev)'''
        # Prejšnja funkcija preveri ustreznost tabele, glede na 
        # ponovitev števil, kar pa še ne pomeni, da je tabela rešljiva.
        return all([
            self.ustreznost_tabele_osnovno(self.zacetna_tabela),
            self.ustreznost_tabele_osnovno(self.resena_tabela),
            not self.najdi_prazno_polje(self.resena_tabela)
        ])

    def ustrezen(self, kandidat, polje, tabela):
        '''Podamo tabelo, številko ki je preverjamo in koordinate.
        Funkcija vrne True/False glede na ustreznost kandidata
        tabela = (self.tabela / self.zacetna_tabela)'''
        return all([
            self.preveri_vrstico(kandidat, polje, tabela),
            self.preveri_stolpec(kandidat, polje, tabela),
            self.preveri_boks(kandidat, polje, tabela)
        ])

    def preveri_vrstico(self, kandidat, polje, tabela):
        '''Preveri, ali kandidat ustreza polju glede na vrstico v
        tabeli. tabela = (self.tabela / self.zacetna_tabela)'''
        for i in range(len(tabela[0])):
            if tabela[polje[0]][i] == kandidat and polje[1] != i:
                return False
        return True

    def preveri_stolpec(self, kandidat, polje, tabela):
        '''Preveri, ali kandidat ustreza polju glede na stolpec v
        tabeli. tabela = (self.tabela / self.zacetna_tabela)'''
        for i in range(len(tabela)):
            if tabela[i][polje[1]] == kandidat and polje[0] != i:
                return False
        return True

    def preveri_boks(self, kandidat, polje, tabela):
        '''Preveri, ali kandidat ustreza polju glede na boks v tabeli. 
        tabela = (self.tabela / self.zacetna_tabela)'''
        boks_x = polje[1] // 3  # Vrednost 0 1 ali 2
        boks_y = polje[0] // 3  # Vrednost 0 1 ali 2

        for i in range(boks_x * 3, boks_x * 3 + 3):
            for j in range(boks_y * 3, boks_y * 3 + 3):
                if tabela[j][i] == kandidat and (j, i) != polje:
                    return False
        # Če pridemo do konca je kandidat ustrezen
        return True

    def resi(self, tabela, stikalo=True):
        '''Z rekurzivnim klicem ("backtracking" algoritmom) reši 
        tabelo in vrne True/False.'''
        if stikalo and not self.ustreznost_tabele_osnovno(tabela):
            return False # Preveri le v ničtem rekurzivnem klicu
        polje = self.najdi_prazno_polje(tabela)
        if polje is None:  # Našli smo rešitev
            return True
        else:
            vrstica, stolpec = polje

        for i in range(1, 10): # i je kandidat
            if self.ustrezen(i, polje, tabela):
                # Kandidat (i) ustreza trenutni tabeli, ne pa še nujno 
                # končni reštvi
                tabela[vrstica][stolpec] = i

                # Poskusimo rešiti novo tabelo (rekurzivni klic)
                if self.resi(tabela, False):
                    return True

                # Če ne pridemo do konca, je številka neustrezna, 
                # ponastavimo polje poskusimo z naslednjim kandidatom.
                tabela[vrstica][stolpec] = 0

        return False # Nismo našli rešitve (tabela je nerešljiva)

    def resi_nakljucno_polje(self):
        '''Izbere nakljucno prazno polje v tabeli in ga zapolni z 
        ustrezno številko.'''
        if self.najdi_prazno_polje(self.tabela):
            y, x = random.choice(range(9)), random.choice(range(9))
            while self.tabela[y][x]:
                y, x = random.choice(range(9)), random.choice(range(9))
            self.tabela[y][x] = self.resena_tabela[y][x]
            if self.najdi_prazno_polje(self.tabela):
                return USPESNA_POMOC
        return RESEN_SUDOKU

    def resi_doloceno_polje(self, polje):
        '''Z ustrezno številko zapolni podano polje v tabeli'''
        y, x = polje
        if not y.isdigit() or not x.isdigit():
            return NEVELJAVEN_VNOS
        y, x = int(y) - 1, int(x) - 1
        if not self.tabela[y][x]:
            self.tabela[y][x] = self.resena_tabela[y][x]
            if self.najdi_prazno_polje(self.tabela):
                return USPESNA_POMOC
            return RESEN_SUDOKU
        return ZAPOLNJENO_POLJE

    def vnesi_stevilko(self, stevilka, polje):
        '''Vrne NAPACEN_UGIB, ZAPOLNJENO_POLJE, PRAVILEN_UGIB, 
        NEVELJAVEN_VNOS, RESEN_SUDOKU'''
        y, x = polje
        if not stevilka.isdigit() or not y.isdigit() or not x.isdigit() or \
        stevilka == '0':
            return NEVELJAVEN_VNOS
        y, x, stevilka = int(y) - 1, int(x) - 1, int(stevilka)
        if self.tabela[y][x]:
            return ZAPOLNJENO_POLJE
        elif self.resena_tabela[y][x] != stevilka:
            return NAPACEN_UGIB
        else:
            self.tabela[y][x] = stevilka
            if self.tabela == self.resena_tabela:
                return RESEN_SUDOKU
            else:
                return PRAVILEN_UGIB

    def stevilo_zacetnih_polj(self, tabela=None):
        if tabela is None:
            tabela = self.zacetna_tabela
        return sum([1 if tabela[y][x] else 0 for x in range(9) for y in
        range(9)])


class SudokuAlly:
    '''Skrbi za trenutno stanje večih mrež (imel bo več objektov tipa 
    Mreza)'''

    def __init__(self, datoteka_s_stanjem=DATOTEKA_S_STANJEM):
        # Slovar, ki imenu priredi njegovo mrežo
        self.mreze = {}    # self.mreze[ime] = (Mreza, stanje)
        self.datoteka_s_stanjem = datoteka_s_stanjem

    def nova_mreza(self, ime, tabela):
        '''Naredi novo mrežo. Vrne ime mreže ali False'''
        self.nalozi_mreze_iz_datoteke()
        mreza = Mreza(tabela) # Naredi novo mrežo
        if mreza.ustreznost_tabele_napredno():
            self.mreze[ime] = (mreza, ZACETEK)
            self.zapisi_mreze_v_datoteko()
            return ime
        else:
            return False

    def resi_polje(self, ime, polje=None):
        self.nalozi_mreze_iz_datoteke()
        trenutna_mreza, _ = self.mreze[ime]

        if polje:
            stanje = trenutna_mreza.resi_doloceno_polje(polje)
        else:
            stanje = trenutna_mreza.resi_nakljucno_polje()

        self.mreze[ime] = (trenutna_mreza, stanje)
        self.zapisi_mreze_v_datoteko()

    def resi_vse(self, ime):
        self.nalozi_mreze_iz_datoteke()
        mreza = self.mreze[ime][0]
        mreza.tabela = mreza.resena_tabela
        self.mreze[ime] = (mreza, RESEN_SUDOKU)
        self.zapisi_mreze_v_datoteko()

    def vnesi_stevilko(self, ime, stevilka, polje):
        self.nalozi_mreze_iz_datoteke()
        trenutna_mreza, _ = self.mreze[ime]
        stanje = trenutna_mreza.vnesi_stevilko(stevilka, polje)
        self.mreze[ime] = (trenutna_mreza, stanje)
        self.zapisi_mreze_v_datoteko()

    def izbrisi_mrezo(self, ime):
        self.nalozi_mreze_iz_datoteke()
        del self.mreze[ime]
        self.zapisi_mreze_v_datoteko()

    def odprte_resene(self):
        '''Vrne števili odprtih in rešenih mrež'''
        odprti, reseni = 0, 0
        for _, stanje in self.mreze.values():
            if stanje == RESEN_SUDOKU:
                reseni += 1
            else:
                odprti += 1
        return (odprti, reseni)

    def zapisi_mreze_v_datoteko(self):
        # { ime : ( zacetna_tabela, tabela, resena_tabela, stanje ) }

        mreze1 = {
            ime : (mreza.zacetna_tabela, mreza.tabela,
            mreza.resena_tabela, stanje)
            for ime, (mreza, stanje) in self.mreze.items()
        }

        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as out_file:
            json.dump(mreze1, out_file, ensure_ascii=False)

    def nalozi_mreze_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as in_file:
            mreze_iz_diska = json.load(in_file)

        self.mreze = {
            ime: (Mreza(zacetna_tabela, tabela, resena_tabela), stanje)
            for ime, (zacetna_tabela, tabela, resena_tabela, stanje) in
            mreze_iz_diska.items()
        }


# Statistika
def odstotek(stevec, imenovalec):
    return int((stevec / imenovalec) * 100)

def statistika(datoteka_s_stanjem=DATOTEKA_S_STANJEM):
    '''
    stevilo_mrez, 
    stevilo_koncanih_mrez, 
    odstotek_odprtih_mrez, 
    odstotek_odprtih_mrez, 
    najtezja_mreza, 
    skupno_stevilo_uganjenih_polj, 
    povprecje_polnih_polj, 
    povprecje_polnih_zacetnih_polj, 
    odstotek_resenih_mrez
    '''
    statistike = dict() # {}
    sudokually = SudokuAlly()
    sudokually.nalozi_mreze_iz_datoteke()
    stevilo_mrez = len(sudokually.mreze)
    statistike['stevilo_mrez'] = str(stevilo_mrez)
    if stevilo_mrez:
        stevilo_koncanih_mrez = sum([1 if not
        mreza.najdi_prazno_polje(mreza.tabela)
        else 0 for mreza, _ in sudokually.mreze.values()])
        statistike['stevilo_koncanih_mrez'] = str(stevilo_koncanih_mrez)

        stevilo_odprtih_mrez = sum([1 if
        mreza.najdi_prazno_polje(mreza.tabela)
        else 0 for mreza, _ in sudokually.mreze.values()])
        statistike['odstotek_odprtih_mrez'] = \
        f'{odstotek(stevilo_odprtih_mrez, stevilo_mrez)}%'

        najtezja = (None, 82) # Več kot 81
        for ime, (mreza, _) in sudokually.mreze.items():
            if mreza.stevilo_zacetnih_polj() <= najtezja[1]:
                najtezja = (ime, mreza.stevilo_zacetnih_polj())
        statistike['najtezja_mreza'] = f'{najtezja[0]}: {najtezja[1]} polj'

        vsa_zacetna_polja = sum([mreza.stevilo_zacetnih_polj() for (mreza, _)
        in sudokually.mreze.values()])
        vsa_polna_polja = sum([mreza.stevilo_zacetnih_polj(mreza.tabela)
        for (mreza, _) in sudokually.mreze.values()])

        statistike['skupno_stevilo_uganjenih_polj'] = str(vsa_polna_polja
        - vsa_zacetna_polja)
        statistike['povprecje_polnih_polj'] = \
        f'{odstotek(vsa_polna_polja, stevilo_mrez * 81)}%'
        statistike['povprecje_polnih_zacetnih_polj'] = round(vsa_zacetna_polja
        / stevilo_mrez, 1)

        resene_mreze = sum([1 if mreza.tabela == mreza.resena_tabela else 0
        for (mreza, _) in sudokually.mreze.values()])
        statistike['odstotek_resenih_mrez'] = \
        f'{odstotek(resene_mreze, stevilo_mrez)}%'

    return statistike
