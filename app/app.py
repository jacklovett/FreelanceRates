import os
from bottle import route, run, template, TEMPLATE_PATH, static_file
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
views_path = dir_path + '/views'

TEMPLATE_PATH.insert(0, views_path)

@route('/home')
def home(): 
    return template(views_path + '/index.html') 

@route('/result', method='POST')
def result():
    return template(views_path + '/result.html')

@route('/<filename:path>')
def static(filename):
    return static_file(filename, root=dir_path + '/static/')

if __name__ == '__main__': 
    run(host='localhost', port=5000, debug=True, reloader=True)

         
