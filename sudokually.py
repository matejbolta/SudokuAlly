# _____           _       _           ___  _ _       
#/  ___|         | |     | |         / _ \| | |      
#\ `--. _   _  __| | ___ | | ___   _/ /_\ \ | |_   _ 
# `--. \ | | |/ _` |/ _ \| |/ / | | |  _  | | | | | |
#/\__/ / |_| | (_| | (_) |   <| |_| | | | | | | |_| |
#\____/ \__,_|\__,_|\___/|_|\_\\__,_\_| |_/_|_|\__, |
#                                               __/ |
#                                              |___/ 

# Uporabljene slike so iz naslednjih naslovov:
# Favicon: https://www.pngrepo.com/png/45383/180/sudoku.png
# Gif: https://giphy.com/gifs/aarp-social-l41Yy6jvn3BXYDRu0
# Slika v readme.md datoteki: 
# https://qph.fs.quoracdn.net/main-qimg-bd9c2c0ab60b01af87f135939d847684.webp

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

@bottle.get('/nova_mreza/')
def nova_mreza_get():
    opozorilo = bottle.request.get_cookie(
        OPOZORILO_COOKIE, secret=COOKIE_SECRET
        )
    return bottle.template('vnos_mreze.tpl', opozorilo=opozorilo)

@bottle.post('/nova_mreza/')
def nova_mreza_post():
    tabela = [[stevilo for stevilo in vrstica] for vrstica in 
    model.PRAZNA_TABELA]
    ime = bottle.request.forms.getunicode('ime').upper()
    if not ime:
        bottle.response.set_cookie(
            OPOZORILO_COOKIE, 'noname', path='/nova_mreza/', 
            secret=COOKIE_SECRET
            )
        bottle.redirect('/nova_mreza/')
    for vrsta in range(9):
        for stolpec in range(9):
            stevilka = bottle.request.forms[f'{vrsta}{stolpec}']
            if stevilka == '':
                continue
            elif not stevilka.isdigit():
                bottle.response.set_cookie(
            OPOZORILO_COOKIE, 'int', path='/nova_mreza/', 
            secret=COOKIE_SECRET
            )
                bottle.redirect('/nova_mreza/')
            tabela[vrsta][stolpec] = int(stevilka)
    if sudokually.nova_mreza(ime, tabela):
        bottle.response.set_cookie(
            IME_MREZE_COOKIE, ime, path='/', secret=COOKIE_SECRET
            )
        bottle.response.set_cookie(
            OPOZORILO_COOKIE, '', path='/nova_mreza/', 
            secret=COOKIE_SECRET
            )
        bottle.redirect('/poskus_namig/')
    else:
        bottle.response.set_cookie(
            OPOZORILO_COOKIE, 'unsolvable', path='/nova_mreza/', 
            secret=COOKIE_SECRET
            )
        bottle.redirect('/nova_mreza/')

@bottle.get('/poskus_namig/')
def prikaz_poskusa():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    mreza, stanje = sudokually.mreze[ime]
    return bottle.template('poskus_namig.tpl',
    ime=ime, mreza=mreza, stanje=stanje)

@bottle.post('/poskus_namig/vnesi_stevilko/')
def vnesi_stevilko():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    vrsta = bottle.request.forms.getunicode('vrsta')
    stolpec = bottle.request.forms.getunicode('stolpec')
    stevilo = bottle.request.forms.getunicode('stevilo')
    sudokually.vnesi_stevilko(ime, stevilo, (vrsta, stolpec))
    bottle.redirect('/poskus_namig/')

@bottle.post('/poskus_namig/resi_polje/')
def resi_polje():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    vrsta = bottle.request.forms.getunicode('vrsta')
    stolpec = bottle.request.forms.getunicode('stolpec')
    sudokually.resi_polje(ime, (vrsta, stolpec))
    bottle.redirect('/poskus_namig/')

@bottle.post('/poskus_namig/resi_nakljucno/')
def resi_nakljucno():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    sudokually.resi_polje(ime)
    bottle.redirect('/poskus_namig/')

@bottle.post('/poskus_namig/resi_vse/')
def resi_vse():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    sudokually.resi_vse(ime)
    bottle.redirect('/poskus_namig/')

@bottle.post('/poskus_namig/izbris_mreze/')
def izbrisi():
    ime = bottle.request.get_cookie(
        IME_MREZE_COOKIE, secret=COOKIE_SECRET
        )
    sudokually.izbrisi_mrezo(ime)
    bottle.redirect('/SudokuAlly/')

@bottle.get('/obstojece_mreze/')
def obstojece_mreze_get():
    return bottle.template('obstojece_mreze.tpl', 
    sudokually=sudokually)

@bottle.post('/obstojece_mreze/<ime>/')
def obstojece_mreze_post(ime):
    bottle.response.set_cookie(
        IME_MREZE_COOKIE, ime, path='/', secret=COOKIE_SECRET
        )
    bottle.redirect('/poskus_namig/')

@bottle.post('/brisanje_sledi/')
def pobrisi_piskotke():
    bottle.response.set_cookie(
            OPOZORILO_COOKIE, '', path='/nova_mreza/', 
            secret=COOKIE_SECRET
            )
    bottle.redirect('/SudokuAlly/')

# Statistika
@bottle.get('/statistika/')
def prikazi_statistiko():
    statistike = model.statistika()
    return bottle.template('statistika.tpl', statistike=statistike)

# Slike
@bottle.get('/img/<slika>')
def serve_pictures(slika):
    return bottle.static_file(slika, root='img')


bottle.run(debug=True, reloader=True)