from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    template_var = 'Template Flask App'
    return render_template('index.html',
                           title='Template App',
                           template_var=template_var)
