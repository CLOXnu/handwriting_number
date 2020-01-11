from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploadPic', methods=['GET', 'POST'])
def uploadPic():
    url = request.args.get('url','')
    return jsonify({'result': 1})

if __name__ == '__main__':
    app.run()