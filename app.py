from flask import Flask, render_template,redirect,url_for,flash
from forms import SignupForm,LoginForm

app=Flask(__name__)
app.config['SECRET_KEY']='this_is secret_key'  

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/signup',methods=['GET','POST'])
def signup():

    forms=SignupForm()
    if forms.validate_on_submit():
        flash(f'You have Successfully Signed UP! {forms.username.data}')
        return redirect(url_for('home'))
    return render_template('signup.html',title='Signup',form=forms)


@app.route('/login', methods=['GET','POST'])
def login():

    forms=LoginForm()
    email=forms.email.data
    pw=forms.password.data
    if forms.validate_on_submit():
        if email== 'abc@a.com'and pw=='123456':
            flash(f'U have successfully Logged In!')
            return redirect(url_for('home'))
        else:
            flash(f'Input has Incorrect Credentials!')
    return render_template('login.html',title='login',form=forms)


if __name__ == '__main__':
    app.run(debug=True)