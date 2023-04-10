from flask import Flask

app = Flask(__name__)

test = ['bla', 'bla2', 'bla3']


@app.get("/store")
def find_test():
    return test
