from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from flask_cors import CORS
import numpy as np
import json
import cv2
import os


app = Flask(__name__)
CORS(app)
CORS(app, resources={
     r"/detector/upload": {"origins": "http://localhost:19006"}})


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
    if file and allowed_file(file.filename):
        # Save the file with a new name and JPG extension
        filename = 'uploaded_image.jpg'
        filepath = os.path.join(filename)
        file.save(filepath)

        # Make prediction
        predicted_class = predict(filepath)
        return json.dumps({'predicted_class': predicted_class})

    return 'Invalid file.'


def allowed_file(filename):
    # You can add more file extensions if needed
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}


def predict(img_path):
    model = load_model('afd.h5')
    class_labels = ['complex', 'frog_eye_leaf_spot',
                    'healthy', 'powdery_mildew', 'rust', 'scab']

    # Load and preprocess the input image using OpenCV
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = cv2.resize(img, (224, 224))
    img_array = np.expand_dims(img, axis=0)

    # Make predictions
    prediction = model.predict(img_array)

    # Dsiplay Results
    prediction = np.array(prediction)
    prediction = np.argmax(prediction, axis=1)
    prediction = list(prediction)

    predicted_class = class_labels[prediction[0]]

    return predicted_class


if __name__ == '__main__':
    app.run(debug=True)