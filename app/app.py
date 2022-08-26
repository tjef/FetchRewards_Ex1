

from flask import Flask,render_template,request
import json
import  ast
import  example1
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        tuples = request.form.get('tuple')
        points = request.form.get('CornerPoint')
        obj = example1.Example1(tuples, points) 
        result = obj.output()
        return str(result)
    return render_template('form.html')
        
if __name__ == '__main__':
    app.debug = True
    app.run()