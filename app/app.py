import os, sys
from bottle import route, run
from bottle import request, post
from bottle import template, TEMPLATE_PATH, static_file

dir_path = os.path.dirname(os.path.abspath(__file__))
# location paths
src_path = dir_path + '\\src'
test_path = dir_path + '\\test'
views_path = dir_path + '\\views'

TEMPLATE_PATH.insert(0, views_path)

sys.path.insert(0, src_path + '\\models')
sys.path.insert(0, test_path + '\\models')
sys.path.insert(0, src_path + '\\controllers')
sys.path.insert(0, test_path + '\\controllers')

from request_model import RequestModel
from main_controller import MainController

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

         
