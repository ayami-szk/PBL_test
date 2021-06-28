from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/', methods = ['POST'])
# def from():
#     field = request.from['field']
#     return render_template('index.html',\
#             title ="From sample",\
#             message = "Hello, %s!", %s field)

# @app.route("/")
# def root():
#    number = int(request.args.get('number'))
#    string = ''
#    for i in range(number):
#        string += ('Hello!')
#    return string

# @app.route("/hogehoge!")
# def hogehoge():
#    return "hogehoge!!"

if __name__=='__main__':
    app.run(debug=True, port=11111)
