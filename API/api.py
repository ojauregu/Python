from flask import Flask
from flask import jsonify
from flask import request
from flask import send_file




app = Flask(__name__)

@app.route('/my-first-api', methods = ['GET'])

def hello():


    name = request.args.get('name')

    if name is None:
        text = 'Hola desconocido!'

    else:
        text = 'Holaaaaaaa amigooooo' + name + '!'

    return jsonify({"message": text})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7000)
