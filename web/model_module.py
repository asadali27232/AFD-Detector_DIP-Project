# from tensorflow.keras.models import load_model
# import numpy as np
# import cv2 as cv2


class Model:
    def allowed_file(filename):
        # You can add more file extensions if needed
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

    # def predict(img_path):
    #     model = load_model('afd.h5')
    #     class_labels = ['complex', 'frog_eye_leaf_spot',
    #                     'healthy', 'powdery_mildew', 'rust', 'scab']

    #     # Load and preprocess the input image using OpenCV
    #     img = cv2.imread(img_path)
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #     img = cv2.resize(img, (224, 224))
    #     img_array = np.expand_dims(img, axis=0)

    #     # Make predictions
    #     prediction = model.predict(img_array)

    #     # Dsiplay Results
    #     prediction = np.array(prediction)
    #     prediction = np.argmax(prediction, axis=1)
    #     prediction = list(prediction)

    #     predicted_class = class_labels[prediction[0]]

    #     return predicted_class
