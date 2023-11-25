from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image


class Model:
    def allowed_file(filename):
        # You can add more file extensions if needed
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

    def predict(img_path):
        # model = load_model('afd.h5')
        class_labels = ['complex', 'frog_eye_leaf_spot',
                        'healthy', 'powdery_mildew', 'rust', 'scab']

        # Open the image using Pillow
        img = Image.open(img_path)

        # Convert the image to RGB mode (if it's not already)
        img = img.convert('RGB')

        # Resize the image to the desired dimensions (e.g., 224x224)
        img = img.resize((224, 224))

        img_array = np.expand_dims(img, axis=0)

        # # Make predictions
        # prediction = model.predict(img_array)

        # # Dsiplay Results
        # prediction = np.array(prediction)
        # prediction = np.argmax(prediction, axis=1)
        # prediction = list(prediction)

        # predicted_class = class_labels[prediction[0]]
        temp = "model under construction"

        return temp
