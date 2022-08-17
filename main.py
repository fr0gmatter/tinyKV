from flask import jsonify, current_app, redirect
from pyms.flask.app import Microservice

ms = Microservice()
app = ms.create_app()

kv = {}
kv["google"] = "https://www.google.com"
kv["gen"] = "https://www.generation.org"
kv["clownworld"] = "https://esotericawakening.com/clown-world"

@app.route("/")
def example():
    return jsonify( {"main": "{}".format(current_app.config["APP_NAME"])})

# example route
@app.route("/hello/<label>")
def hello( label ):
    return jsonify( {"label": "{}".format(label) } )

@app.route("/<label>")
def redirect_to_teenyUrl( label ):
    if label in kv.keys():
        return redirect( kv[label], 302 )
    else:
        return jsonify( {"label": "{}".format(label) } )

if __name__ == '__main__':
    app.run()
