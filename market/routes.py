from market import app ,db
from flask import render_template ,redirect ,url_for ,flash 
from market.models import Item ,User 
from market.forms import RegisterForm, LoginForm
from flask_login import login_user ,logout_user , login_required

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/market')
@login_required
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_adress=form.email_adress.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('market_page'))
       
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}' , category='danger')

   
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash("You have been logged out" , category='info')
    return redirect(url_for('index'))

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

    
    return render_template('test.html' , items=item_test , users = user_test)


    

