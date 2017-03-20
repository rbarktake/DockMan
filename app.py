# import the Flask class from the flask module
from flask import Flask, render_template
import constants as config
from model import DockerInfo
from util import getDateString
#  create the application object
app = Flask(config.APP['NAME'])
dc = DockerInfo()

def include_app_data(fn):
    template_name = fn()

    def wrapped():
        return render_template(template_name, APP=config.APP)
    return wrapped

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('home.html', APP=config.APP, dock=dc)

@app.route('/index/<entity>/')
def index(entity):
    return render_template('index.html', APP=config.APP, dock=dc)

@app.route('/<template_name>/')
def showpage(template_name):
    #return render_template(template_name, APP=config.APP, dock=dc)  
    return render_template('index.html', APP=config.APP, dock=dc, entity=template_name)
'''
@app.route('/boothome')
def boothame():
    return render_template('boothome.html', APP=config.APP)  # render a template

@app.route('/index')
#@include_app_data
def index():
     return render_template('index.html', APP=config.APP)



@app.route('/index2')
@include_app_data
def index():
    return 'index2.html'
'''

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    return getDateString(date)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8888)
