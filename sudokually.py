import bottle, model

# Spletni vmesnik

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

