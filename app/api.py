import time
from flask import Flask, jsonify
from flask import render_template
from werkzeug.contrib.cache import SimpleCache

from service import sncf_routes

import ipdb

app = application = Flask("VueFlask")
cache = SimpleCache()

import ipdb


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/one")
def one():
    o = cache.get("one")
    if not o:
        o = {"one": [k for k in range(10)]}
        cache.set("one", o, timeout=30)
    return jsonify(o)


@app.route("/api/two")
def two():
    return jsonify(
        {
            "two": [k for k in range(10, 20)]
        }
    )


@app.route("/api/sncf_routes")
def sncf_route_from_db():

    sncf_routes_df = sncf_routes.read_from_db()
    sncf_routes_df = sncf_routes.convert_date_to_string(sncf_routes_df)

    data = sncf_routes_df.head().to_json(orient='records')
    columns = sncf_routes_df.head().to_json(orient='split')
    print data
    # ipdb.set_trace()

    return jsonify(columns=columns, data=data)


@app.route("/healthz")
def healthz():
    return jsonify(
        {
            "flask": True,
            "global": True
        }
    )


@app.route("/api/ts")
def ts():
    return jsonify(
        {
            "now": time.time()
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
