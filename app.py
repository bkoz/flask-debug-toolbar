from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
 
app = Flask(__name__, instance_relative_config=True)
 
app.debug = True

app.config.from_mapping(SECRET_KEY='dev')

toolbar = DebugToolbarExtension(app)

@app.route('/form')
@app.route('/')
def form():
    return render_template('form.html')
 
app.run(host='localhost', port=8080)

