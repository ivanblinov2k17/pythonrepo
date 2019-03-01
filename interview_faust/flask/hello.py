import flask
app = flask.Flask(__name__)

arr = [
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
    ['ivan', 'blinov', '01.03.2019', 228],
]
@app.route('/')
@app.route('/<int:n>')
def hello(n=1):
    return flask.render_template('hello.html', arr=arr, n=n)


if __name__ == '__main__':
    app.run(debug='true')