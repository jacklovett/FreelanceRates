import os, sys
from bottle import route, run
from bottle import request, post
from bottle import template, TEMPLATE_PATH, static_file

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
SYSTEM_PATH = sys.path

# location paths
views_path = dir_path + '/views'
controllers_path = dir_path + '/controllers'
models_path = dir_path + '/models'

TEMPLATE_PATH.insert(0, views_path)
SYSTEM_PATH.insert(0, controllers_path)
SYSTEM_PATH.insert(0, models_path)

from requestModel import RequestModel
from mainController import MainController

@route('/')
def home(): 
    return template(views_path + '/index.html') 

@route('/result', method='POST')
def result():
    requestModel = RequestModel(request.forms)
    main_controller = MainController(requestModel) 
    response = main_controller.calc_result()
    return template(views_path + '/result.html', response=response)

@route('/<filename:path>')
def static(filename):
    return static_file(filename, root=dir_path + '/static/')

if __name__ == '__main__': 
    run(host='localhost', port=5000, debug=True, reloader=True)

         
