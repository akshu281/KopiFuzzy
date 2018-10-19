from flask import Flask
from flask import render_template,url_for,request
from kopifuzzy_1 import *
application = Flask(__name__,static_url_path='/static',template_folder='templates')

@application.route("/")
def hello():
    return render_template('index.html')

@application.route("/getcoffee",methods=['POST'])
def get_coffee():
    print(request)
    values=dict(request.form)
    data={'kopi':values['kopi'][0],'milk':values['milk'][0],'sugar':values['sugar'][0]}
    return get_score(data)

if __name__ == "__main__":
application.run()