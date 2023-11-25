from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from model_module import Model
import os
import base64


app = Flask(__name__)
CORS(app)
CORS(app, origins=["http://localhost:19006"])
model = Model()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detector')
def detector():
    return render_template('detector.html')


@app.route('/blogs')
def blogs():
    return render_template('blogs.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/detector/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # Check if the file is present and allowed
    if file and model.allowed_file(file.filename):
        # Save the file with a new name and JPG extension
        filename = 'uploads/uploaded_image.jpg'
        filepath = os.path.join(filename)
        file.save(filepath)

        # Make prediction
        prediction = model.predict(filepath)
        return jsonify(prediction)

    return jsonify({'inv': 'Invalid file.'})


@app.route('/upload', methods=['POST'])
def upload_image():
    print('upload_image')
    try:
        data = request.get_json()
        base64_image = data.get('image')

        if base64_image:
            # Decode the base64 image
            image_data = base64.b64decode(base64_image)

            # Define the file path where you want to save the image
            upload_folder = 'uploads'  # Create an 'uploads' folder in your Flask project directory
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            # Specify the file name (you can use a unique name or use a fixed name like 'uploaded_image.jpg')
            file_name = 'uploaded_image.jpg'

            # Combine the folder path and file name to get the full file path
            file_path = os.path.join(upload_folder, file_name)

            # Write the image data to the file
            with open(file_path, 'wb') as file:
                file.write(image_data)

            # Make prediction
            prediction = model.predict(file_path)
            return jsonify(prediction)
        else:
            return jsonify({'error': 'No image data provided'})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
