import random
from create_post import main
from flask import Flask, send_file

app = Flask('')


@app.route('/')
def home():
    return "Hello. I am alive!"


N = [0]

@app.route('/create')
def create():
    main()
    N.clear()
    N.append(str(random.randint(1, 25)))
    return {"status": "Completed"}

@app.route('/request')
def request():
    N.clear()
    N.append(str(random.randint(1, 25)))
    return {"N": N[0]}


@app.route(f'/get/<n>/quote.jpg')
def get_image(n):
    if n == N[0]:
        filename = "quote.jpg"
        return send_file(filename, mimetype='image/jpeg')
    else:
        return {'ERROR': "ACCESS Denied"}


app.run(host='0.0.0.0', port=2453)
