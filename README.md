# Dynamic Forms With Flask/WTForms

This shows how to create a form with a dynamically-built list of checkboxes.
The trick is to dynamically create a subclass of UserForm, add the dynamic fields, and then create an instance of the subclass.

- A `count` variable is used in app.py to show an increasing number of checkboxes. The number of checkboxes shown starts at 1 and increases each time the form is displayed until the app is restarted.
- The results are printed to the terminal to show how the POST sends the data. However `user_data` does *not* get updated when the form is submitted.
- Class methods for UserForm and CuisineForm let us put all form-related manipulation in forms.py (where it belongs), thus keeping it out of app.py (where it doesn't).

## Links

- https://wtforms.readthedocs.io/en/3.0.x/specific_problems/#dynamic-form-composition
- https://wtforms.readthedocs.io/en/3.0.x/fields/#field-enclosures