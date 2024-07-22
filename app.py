from flask import Flask
from flask import url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello<h1>'


@app.route('/usr/<name>')
def user_page(name):
    return f'User:{escape(name)}'


@app.route('/test')
def test_url_for():
    print(f'url_for_hello:{url_for("hello")}')
    print(f'url_for_user_page:{url_for("user_page", name="jackson")}')
    print(f'url_for_user_page:{url_for("user_page", name="jay")}')
    print(f'test_url_for:{url_for("test_url_for")}')
    return "test page"


if __name__ == '__main__':
    app.run()
