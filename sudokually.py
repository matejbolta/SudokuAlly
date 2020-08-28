# _____           _       _           ___  _ _       
#/  ___|         | |     | |         / _ \| | |      
#\ `--. _   _  __| | ___ | | ___   _/ /_\ \ | |_   _ 
# `--. \ | | |/ _` |/ _ \| |/ / | | |  _  | | | | | |
#/\__/ / |_| | (_| | (_) |   <| |_| | | | | | | |_| |
#\____/ \__,_|\__,_|\___/|_|\_\\__,_\_| |_/_|_|\__, |
#                                               __/ |
#                                              |___/ 

import bottle, model

# Konstante
IME_MREZE_COOKIE = 'id_igre'
COOKIE_SECRET = 'my very special - secret key and passphrase'
DATOTEKA_S_STANJEM = 'stanje.json'

# Naredimo nov objekt SudokuAlly in naložimo vanj stanje iz datoteke
sudokually = model.SudokuAlly()
print('check')
sudokually.nalozi_mreze_iz_datoteke()
print('check')
@bottle.get('/')
def index():
    return bottle.template('index.tpl')


# Pomoč pri razvijanju - ustvaritev mreže
print('check')
ime_nove_mreze0 = sudokually.nova_mreza('enkica', model.tabela_1)
print('check')
ime_nove_mreze1 = sudokually.nova_mreza('dvojkica', model.tabela_2)
print('check')
ime_nove_mreze2 = sudokually.nova_mreza('iz appa', model.tabela_ctcapp)
print('check')
ime_nove_mreze3 = sudokually.nova_mreza('iz youtuba', model.tabela_ctcyt)
print('check')




# Slike
@bottle.get('/img/<slika>')
def serve_pictures(slika):
    return bottle.static_file(slika, root='img')

bottle.run(debug=True, reloader=True)