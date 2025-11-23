from flask import Flask, render_template, request, redirect
import fnmatch

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    print(page_name)
    return render_template(page_name)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
    else:
        return redirect('/')

