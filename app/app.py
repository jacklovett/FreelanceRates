import os, sys
from bottle import route, run, template, TEMPLATE_PATH, static_file
from bottle import request, post

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

# location paths
views_path = dir_path + '/views'
controllers_path = dir_path + '/controllers'

sys.path.insert(0, controllers_path + '/mainController.py')
import MainController

TEMPLATE_PATH.insert(0, views_path)

@route('/home')
def home(): 
    return template(views_path + '/index.html') 

# pylint: disable=no-member
@route('/result', method='POST')
def result():       
    main_controller = MainController(request.forms)
    main_controller.calc_result()   
    return template(views_path + '/result.html')

@route('/<filename:path>')
def static(filename):
    return static_file(filename, root=dir_path + '/static/')

if __name__ == '__main__': 
    run(host='localhost', port=5000, debug=True, reloader=True)

         
