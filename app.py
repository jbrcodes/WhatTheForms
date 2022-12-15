from flask import Flask, render_template, request
from forms import CuisineForm, UserForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hey, how R U today?'


user_data = {
    'name': 'Herbert',
    'language': 'Python',
    'cuisines': [
        ('French', True),
        ('Greek', False),
        ('Italian', True),
        ('Mexican', False),
        ('Spanish', True),
        ('Vietnamese', False)
    ]
}


# The number of checkboxes to show; it gets reset when app restarts
count = 1


@app.route('/')
def route_home():
    global count

    # Dynamically define a subclass of UserForm
    class DynUserForm(UserForm):
        pass

    # Dynamically add 'count' checkboxes to an empty CuisineForm
    CuisineForm.add_checkboxes(user_data['cuisines'][:count])
    count += 1
    
    # Dynamically add CuisineForm to the dynamic subclass of UserForm
    DynUserForm.add_cuisines_fields(CuisineForm)

    # Create the form (finally!)
    form = DynUserForm(data=user_data)

    return render_template('home.html', form=form)


@app.route('/submit', methods=['POST'])
def route_submit():
    print(request.form)

    return render_template('thanks.html')