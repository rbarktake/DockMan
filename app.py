# import the Flask class from the flask module
from flask import Flask, render_template
import constants as config
from model import DockerInfo

#  create the application object
app = Flask(config.APP['NAME'])

def include_app_data(fn):
    template_name = fn()

    def wrapped():
        return render_template(template_name, APP=config.APP)
    return wrapped

# use decorators to link the function to a url
@app.route('/')
def home():
    dc = DockerInfo()
    return render_template('index.html', APP=config.APP, dock=dc)

'''
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/boothome')
def boothame():
    return render_template('boothome.html', APP=config.APP)  # render a template

@app.route('/index')
#@include_app_data
def index():
     return render_template('index.html', APP=config.APP)

'''

@app.route('/index2')
@include_app_data
def index():
    return 'index2.html'


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, port=8888)
