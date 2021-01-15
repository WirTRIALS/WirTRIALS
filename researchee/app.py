from flask import Flask, render_template, jsonify, request
import name
import profile
import expertise
import coauthors

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    prof = jsonify(name.getName())
    prof.headers.add('Access-Control-Allow-Origin', '*')  # CORS Policy
    return prof


@app.route('/expertise')
def get_expertise():
    name = request.args.get('name')
    prof_expertise = jsonify(expertise.getExpertise(name))
    prof_expertise.headers.add('Access-Control-Allow-Origin', '*')
    return prof_expertise


@app.route('/image')
def get_image():
    name = request.args.get('name')  # query parameter of prof name
    try:
        image = profile.getImage(name)
        parse_image = jsonify(image)
        parse_image.headers.add('Access-Control-Allow-Origin', '*')
        return parse_image
    # some code
    except Exception as e:
        msg = jsonify("NODATA")
        msg.headers.add('Access-Control-Allow-Origin', '*')
        return msg


@app.route('/details')
def get_details():
    name = request.args.get('name')  # query parameter of prof name
    try:
        image = profile.getDetails(name)
        parse_image = jsonify(image)
        parse_image.headers.add('Access-Control-Allow-Origin', '*')
        return parse_image
    # some code
    except Exception as e:
        msg = jsonify("NODATA")
        msg.headers.add('Access-Control-Allow-Origin', '*')
        return msg


@ app.route('/publications')
def get_publications():
    name = request.args.get('name')
    pubs = jsonify(coauthors.getPublication(name))
    pubs.headers.add('Access-Control-Allow-Origin', '*')
    return pubs


if __name__ == "__main__":
    app.run()
