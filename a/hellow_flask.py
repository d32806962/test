from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('123.html')
    print("data")

@app.route('/aaa',methods=['GET'])
def aaa():
    data = request.args.get('asd')
    data2 = request.args.get('pass')
    dic_data={}
    dic_data['asd']= request.args.get('asd')
    dic_data['pass']= request.args.get('pass')

    return dic_data



if __name__ == '__main__':
    app.debug = True
    app.run()