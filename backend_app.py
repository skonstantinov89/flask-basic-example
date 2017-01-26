from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_page():
    return "Hello World!"


@app.route('/home')
def home_page():
    return "Hello HOME link!"

@app.route('/template_link')
def template_page():
    return render_template('/template.html')



if __name__ == '__main__':
    app.run()


# run with: python backend_app.py
# open at: 
# localhost:5000
# localhost:5000/home
# localhost:5000/template_link