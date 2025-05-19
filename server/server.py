from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form["image_data"]

    response  = jsonify(util.classify_image(image_data))

    response.headers.add("Access-Control_Allow_Origin",'*')

    return response


if __name__ == "__main__":
    print("Starting python server for Celebrity Face Detection")
    util.load_saved_artifacts()
    # util.classify_image(None, "test_images/220px-Cristiano_Ronaldo_Portugal_2018.jpg")
    app.run(port=5000)