from flask import Flask,render_template,request
import json
import  ast
import  example1
# example1.tuple
# example1.corner_points



# json_string = json.dumps(output)

lists = [
    ]

fh = open('file.txt', 'r+')




app = Flask(__name__)




@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        print("made it!!!!!!!!!!!!!!!!!!!!!!!")
        # print(request.form)
        tuples = request.form.get('tuple')
        points = request.form.get('CornerPoint')
        obj = example1.Example1(tuples, points) 
        fh.write(str(obj.output))
        lists.append(fh.readline())
        print("writeeeeeeeewASDFADFFDAF")
        fh.close()
        

        
        # lists.append(
        #     (
        #         obj.output
        #     )    
        # )
    
        
            

    
   
    # return obj.output

    return render_template('form.html')

@app.route('/display', methods=['GET', 'POST'])
def display():
    # with open('file.txt') as f:
    #     first_line = f.readline()
    #     lists.append(first_line)
        
    
   
    return render_template('display.jinja2', entries = lists)
# @app.route('/form')
# def form():
#     print(request.args)
#     return render_template('form.html')
#[(1, 1),(3, 1),(1, 3),(3, 3)]
# @app.route('/data/', methods = ['POST', 'GET'])

# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':

#         #grab tuple 
#         #grab corner_points 
#         #feed it to example1.py
#         #dispaly it here
#         # output = example1.output #[(1, 1),(3, 1),(1, 3),(3, 3)]
#         # tuples = request.form.items[0]
#         # corner_point = request.form.items[1]


#         form_data = request.form.items
#         return render_template('data.html',form_data = form_data)

#     # value = request.json['key']
#     # return value
#     # envelope  = request.get_json()
#     # print(envelope)

#     # return "", 204


if __name__ == '__main__':
    app.debug = True
    app.run()



# from flask import Flask,render_template,request
 
# app = Flask(__name__)
 
# @app.route('/', methods=['POST', 'GET'])
# def index():
#     return 204
# @app.route('/form')
# def form():
#     return render_template('form.html')
 
# @app.route('/data/', methods = ['POST', 'GET'])
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#         return render_template('data.html',form_data = form_data)
 
 
# app.run(host='localhost', port=5000)