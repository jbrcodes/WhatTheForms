from flask import Flask, render_template
from forms import UserForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hey, how R U today?'


user_data = {
    'name': 'Herbert',
    'language': 'Python',
    'opt1': False, 
    'opt2': True, 
    'opt3': False 
}


@app.route('/')
def route_home():
    form = UserForm(data=user_data)
    return render_template('home.html', form=form)