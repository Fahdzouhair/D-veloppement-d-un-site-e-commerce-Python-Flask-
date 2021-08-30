from market import app ,db
from flask import render_template ,redirect ,url_for ,flash 
from market.models import Item ,User 
from market.forms import RegisterForm

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_adress=form.email_adress.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
       
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}' , category='danger')

   
    return render_template('register.html', form=form)

        



@app.route('/test')
def test_page():
    #item1 = Item(name='laptop' , price= 345 , barcode='145334562023' , description='dell corei5 7th') 
    #db.create_all()
    #db.session.add(item1)
    #db.session.commit()
    #items = Item.query.all()
    item_test = Item.query.all()
    user_test = User.query.all()
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]

    
    return render_template('test.html' , items=items , users = user_test)


    

