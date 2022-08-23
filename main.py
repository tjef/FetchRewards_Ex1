from flask import Flask, request
import json
import  ast
import  example1
output = example1.output #[(1, 1),(3, 1),(1, 3),(3, 3)]

json_string = json.dumps(output)





app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return json_string 


    value = request.json['key']
    # return value
    # envelope  = request.get_json()
    # print(envelope)

    # return "", 204




if __name__ == '__main__':
    app.run(debug=True)
