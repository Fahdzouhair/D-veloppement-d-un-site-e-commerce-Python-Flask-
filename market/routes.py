from market import app 
from flask import render_template
from market.models import Item , db 

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/test')
def test_page():
    #item1 = Item(name='laptop' , price= 345 , barcode='145334562023' , description='dell corei5 7th') 
    #db.create_all()
    #db.session.add(item1)
    #db.session.commit()
    #items = Item.query.all()
    item_test = Item.query.all()
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    
    return render_template('test.html' , items=items )
