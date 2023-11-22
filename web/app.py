from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

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

        # Return a success message
        return 'File uploaded and saved as JPG successfully.'

    return 'Invalid file.'

def allowed_file(filename):
    # You can add more file extensions if needed
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}


if __name__ == '__main__':
    app.run(debug=True)
