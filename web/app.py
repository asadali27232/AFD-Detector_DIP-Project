from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import Model as model
import json
import os


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detector')
def detector():
    return render_template('detector.html')


@app.route('/detector/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # Check if the file is present and allowed
    if file and model.allowed_file(file.filename):
        # Save the file with a new name and JPG extension
        filename = 'uploaded_image.jpg'
        filepath = os.path.join(filename)
        file.save(filepath)

        # # Make prediction
        # predicted_class = model.predict(filepath)
        # return json.dumps({'predicted_class': predicted_class})
        return json.dumps({'filepath': filepath})

    return json.dumps({'inv': 'Invalid file.'})


if __name__ == '__main__':
    app.run(debug=True)
