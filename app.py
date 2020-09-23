from flask import Flask, request, render_template
from extract_entities import extract_entities

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')


@app.route('/extract_entities', methods=['GET', 'POST'])
def pos_tags():
    data = request.form['text']
    response = extract_entities(data)
    return render_template('index.html', data=data, response=response)


if __name__ == '__main__':
    app.run()
