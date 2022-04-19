from email.headerregistry import Address
import logging
from flask  import render_template, flash, redirect, session, url_for,request
from .models import  Booking, Customer, User
from app import app,db
logger = logging.getLogger('app')


@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

def login_user(user,remember=True,ctype='customer'):
    session['username']= user.username
    session['id']= user.id
    session['is_login']= True 
    if ctype =='admin':
        session['is_admin']=True
    else:
        session['email']= user.email
        session['is_customer'] = True

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =="POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # print(username,password)
        ctype = request.form.get('type')
        if username and password and ctype =='customer':
            user = Customer.query.filter_by(username=username).first()
            print(user)
            if user  is None or user.password != password:
                flash('Invalid  username or password ','danger' )
                return redirect(url_for('login'))
            else:
                login_user(user, remember=True)
                return redirect (url_for('booking'))   
        elif username and password and ctype =='admin':
            user = User.query.filter_by(username=username).first()
            print(user)
            if user  is None or user.password != password:
                flash('Invalid  username or password ','danger' )
                return redirect(url_for('login'))
            else:
                login_user(user, remember=True, ctype='admin')
                return redirect (url_for('dashboard'))
        else:
            flash("username and password must be provided",'danger')  

    return render_template('login.html')         


@app.route('/registration',methods =['GET','POST'])
def registration():
    if request.method=='POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        address = request.form.get('address')
        mobile_no = request.form.get('mobile')
        aadharno = request.form.get('adhaar')
        # print(cpassword, password, cpassword==password)
        if username and password and address and email and mobile_no and aadharno:
                if Customer.query.filter_by(email=email).first() is not None:
                    flash('Please use a different email address','danger')
                    return redirect('/registration')
                elif Customer.query.filter_by(username=username).first() is not None:
                    flash('Please use a different username','danger')
                    return redirect('/registration')
                elif Customer.query.filter_by(mobile_no=mobile_no).first() is not None:
                    flash('A Customer with same mobile number exists','danger')
                    return redirect('/registration')
                elif Customer.query.filter_by(aadharno=aadharno).first() is not None:
                    flash('A customer with same aadhar number exists','danger')
                    return redirect('/registration')
                else:
                    customer = Customer(username=username, email=email, password=password, address=address, mobile_no=mobile_no, aadharno=aadharno)
                    db.session.add(customer)
                    db.session.commit()
                    flash('Congratulations, you are now a registered user!','success')
                    return redirect(url_for('login'))
        else:
            flash('Fill all the fields','danger')
            return redirect('/register')

    return render_template('registration.html', title='Sign Up page')


@app.route('/booking',methods =['GET','POST'])
def booking():
    if request.method =='POST':
        customer = Customer.query.get(session.get('id'))
        booking = Booking(customer=customer.id)
        db.session.add(booking)
        db.session.commit()
        session['booking_id'] = booking.id
        return redirect('/payment')
    return render_template('Booking.html')

@app.route('/dashboard')
def dashboard():
    customers =Customer.query.all()
    return render_template('Dashboard.html', cm=customers)

@app.route('/payment', methods=['GET','POST'])
def payment():
    if session.get('booking_id'):
        bid = session.get('booking_id')
        if request.method=="POST":
         return redirect('/success')
        
        return render_template('payment.html')  
    return redirect('/booking')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have successfully logged out','success')
    return redirect('/login')




