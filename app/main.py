

from flask import Flask,render_template,request
import json 
import  ast
import exercise #grabs exercise file
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        tuples = request.form.get('tuple') #grabs input tuple data
        points = request.form.get('CornerPoint') #grabs input points data
        obj = exercise.ListPrint(tuples, points)  #make an object of ListPrint init values
        result = obj.output() #runs exercise and outputs list
        return str(result) 
    return render_template('form.html') #creats form 
        
if __name__ == '__main__':
    app.run(debug = True, port = 5000, host = "0.0.0.0") #stat specificly what port i'd like to use
