# _____           _       _           ___  _ _       
#/  ___|         | |     | |         / _ \| | |      
#\ `--. _   _  __| | ___ | | ___   _/ /_\ \ | |_   _ 
# `--. \ | | |/ _` |/ _ \| |/ / | | |  _  | | | | | |
#/\__/ / |_| | (_| | (_) |   <| |_| | | | | | | |_| |
#\____/ \__,_|\__,_|\___/|_|\_\\__,_\_| |_/_|_|\__, |
#                                               __/ |
#                                              |___/ 

import bottle
import model
import json
import os

# Konstante
IME_MREZE_COOKIE = 'ime_mreze'
OPOZORILO_COOKIE = 'opozorilo'
COOKIE_SECRET = 'potni list do mojega piškotka'

# Če datoteka s stanjem še ne obstaja, jo naredimo.
if not os.path.exists(model.DATOTEKA_S_STANJEM):
    with open(model.DATOTEKA_S_STANJEM, 'w', encoding='utf-8') as empty:
        json.dump({}, empty)

# Naredimo nov objekt SudokuAlly in naložimo vanj stanje iz datoteke
sudokually = model.SudokuAlly()
sudokually.nalozi_mreze_iz_datoteke()


@bottle.get('/')
def slash():
    return bottle.redirect('/SudokuAlly/')

@bottle.get('/SudokuAlly/')
def index():
    return bottle.template('index.tpl')

@bottle.get('/SudokuAlly/nova_mreza/')
def nova_mreza_get():
    opozorilo = bottle.request.get_cookie(
        OPOZORILO_COOKIE, secret=COOKIE_SECRET
        )
    return bottle.template('vnos_mreze.tpl', opozorilo=opozorilo)

@bottle.post('/SudokuAlly/nova_mreza/')
def nova_mreza_post():
    tabela = [[stevilo for stevilo in vrstica] for vrstica in 
    model.PRAZNA_TABELA]
    ime = bottle.request.forms.getunicode('ime').upper()
    if not ime:
        bottle.response.set_cookie(
            OPOZORILO_COOKIE, 'noname', path='/SudokuAlly/nova_mreza/', 
            secret=COOKIE_SECRET
            )
        bottle.redirect('/SudokuAlly/nova_mreza/')
    for vrsta in range(9):
        for stolpec in range(9):
            stevilka = bottle.request.forms[f'{vrsta}{stolpec}']
            if stevilka == '':
                continue
            elif not stevilka.isdigit():
                bottle.response.set_cookie(
            OPOZORILO_COOKIE, 'int', path='/SudokuAlly/nova_mreza/', 
            secret=COOKIE_SECRET
            )
                bottle.redirect('/SudokuAlly/nova_mreza/')
            tabela[vrsta][stolpec] = int(stevilka)
    if sudokually.nova_mreza(ime, tabela):
        bottle.response.set_cookie(
            IME_MREZE_COOKIE, ime, path='/SudokuAlly/', secret=COOKIE_SECRET
            )
        bottle.response.set_cookie(
            OPOZORILO_COOKIE, '', path='/SudokuAlly/nova_mreza/', 
            secret=COOKIE_SECRET
            )
        bottle.redirect('/SudokuAlly/poskus_namig/')
    else:
        bottle.response.set_cookie(
            OPOZORILO_COOKIE, 'unsolvable', path='/SudokuAlly/nova_mreza/', 
            secret=COOKIE_SECRET
            )
        bottle.redirect('/SudokuAlly/nova_mreza/')

@bottle.get('/SudokuAlly/poskus_namig/')
def prikaz_poskusa():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    mreza, stanje = sudokually.mreze[ime]
    return bottle.template('poskus_namig.tpl',
    ime=ime, mreza=mreza, stanje=stanje)

@bottle.post('/SudokuAlly/poskus_namig/vnesi_stevilko/')
def vnesi_stevilko():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    vrsta = bottle.request.forms.getunicode('vrsta')
    stolpec = bottle.request.forms.getunicode('stolpec')
    stevilo = bottle.request.forms.getunicode('stevilo')
    sudokually.vnesi_stevilko(ime, stevilo, (vrsta, stolpec))
    bottle.redirect('/SudokuAlly/poskus_namig/')

@bottle.post('/SudokuAlly/poskus_namig/resi_polje/')
def resi_polje():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    vrsta = bottle.request.forms.getunicode('vrsta')
    stolpec = bottle.request.forms.getunicode('stolpec')
    sudokually.resi_polje(ime, (vrsta, stolpec))
    bottle.redirect('/SudokuAlly/poskus_namig/')

@bottle.post('/SudokuAlly/poskus_namig/resi_nakljucno/')
def resi_nakljucno():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    sudokually.resi_polje(ime)
    bottle.redirect('/SudokuAlly/poskus_namig/')

@bottle.post('/SudokuAlly/poskus_namig/resi_vse/')
def resi_vse():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    sudokually.resi_vse(ime)
    bottle.redirect('/SudokuAlly/poskus_namig/')

@bottle.post('/SudokuAlly/poskus_namig/izbris_mreze/')
def izbrisi():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    sudokually.izbrisi_mrezo(ime)
    bottle.redirect('/SudokuAlly/')

@bottle.get('/SudokuAlly/obstojece_mreze/')
def obstojece_mreze_get():
    return bottle.template('obstojece_mreze.tpl', 
    sudokually=sudokually)

@bottle.post('/SudokuAlly/obstojece_mreze/<ime>/')
def obstojece_mreze_post(ime):
    mreza, stanje = sudokually.mreze[ime]
    if stanje != model.RESEN_SUDOKU:
        sudokually.mreze[ime] = mreza, model.ZACETEK
    bottle.response.set_cookie(
        IME_MREZE_COOKIE, ime, path='/SudokuAlly/', secret=COOKIE_SECRET
        )
    bottle.redirect('/SudokuAlly/poskus_namig/')

@bottle.post('/SudokuAlly/brisanje_sledi/')
def pobrisi_piskotke():
    bottle.response.set_cookie(
            OPOZORILO_COOKIE, '', path='/SudokuAlly/nova_mreza/', 
            secret=COOKIE_SECRET
            )
    bottle.redirect('/SudokuAlly/')

# Statistika
@bottle.get('/SudokuAlly/statistika/')
def prikazi_statistiko():
    statistike = model.statistika()
    return bottle.template('statistika.tpl', statistike=statistike)

# Slike
@bottle.get('/SudokuAlly/img/<slika>')
def serve_pictures(slika):
    return bottle.static_file(slika, root='img')


bottle.run(debug=True, reloader=True)