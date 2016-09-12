import flask
from flask import Response
app = flask.Flask(__name__,static_url_path='')

@app.route("/")
def root():
    return flask.send_from_directory(".","map.html")

@app.route("/logo")
def logo():
    return flask.send_from_directory(".","logooocc.png")

@app.route("/data")
def data():
    return flask.send_from_directory(".","geo.json")

@app.route("/bg")
def bg():
    return flask.send_from_directory(".","mex-gray.jpg")

@app.route("/bg/svg")
def svg():
    return flask.send_from_directory(".","map.svg")

# No cacheing at all for API endpoints.
@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == "__main__":
    app.run()
