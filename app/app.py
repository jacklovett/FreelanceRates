import os, sys
from bottle import route, run
from bottle import request, post
from bottle import template, TEMPLATE_PATH, static_file

dir_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(dir_path))
# views location
views_path = dir_path + '\\app\\views'

TEMPLATE_PATH.append(views_path)

from app.src.models.request_model import RequestModel
from app.src.controllers.main_controller import MainController

@route('/')
def home(): 
    return template(views_path + '/index.html') 

@route('/result', method='POST')
def result():
    requestModel = RequestModel(request.forms)
    mainController = MainController(requestModel) 
    response = mainController.calc_result()
    return template(views_path + '/result.html', response=response)

@route('/<filename:path>')
def static(filename):
    return static_file(filename, root=dir_path + '\\app\\static')

if __name__ == '__main__':
    run(host='localhost', port=5000, debug=True, reloader=True)         