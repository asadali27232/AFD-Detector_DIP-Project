from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image


class Model:
    def __init__(self):
        self.class_labels = ['complex', 'frog_eye_leaf_spot',
                             'healthy', 'powdery_mildew', 'rust', 'scab']

        self.disease_info = {
            'complex': {
                'name': 'Complex Disease',
                'description': "Complex disease refers to a condition where an apple tree leaf exhibits symptoms of more than one disease simultaneously. It may require tailored treatments for each identified disease. Regular monitoring, timely intervention, and proper orchard hygiene are essential precautions to reduce the occurrence of complex diseases."
            },
            'frog_eye_leaf_spot': {
                'name': 'Frog Eye Leaf Spot',
                'description': "Frog eye leaf spot is a fungal disease characterized by round, dark lesions with a reddish-brown margin, resembling a frog's eye. Prevent and manage this disease by maintaining good air circulation, pruning infected leaves, and removing fallen debris promptly."
            },
            'healthy': {
                'name': 'Healthy Leaves',
                'description': "Healthy leaves are a sign of a thriving apple tree. To maintain leaf health, ensure proper nutrition, adequate water supply, and a pest-free environment. Prune to improve air circulation and sunlight exposure. Regular monitoring for diseases and pests is essential."
            },
            'powdery_mildew': {
                'name': 'Powdery Mildew',
                'description': "Powdery mildew appears as white, powdery spots on leaves and can affect apple trees. Prevent and manage this disease by planting disease-resistant apple varieties, maintaining proper spacing, and pruning to remove infected leaves. Fungicides can be used during the growing season. Vigilant monitoring is necessary."
            },
            'rust': {
                'name': 'Rust Disease',
                'description': "Rust disease causes orange or yellowish-orange lesions on apple tree leaves. Prevent rust disease by choosing rust-resistant varieties, practicing proper orchard sanitation, and using fungicides during early stages of infection. To combat rust disease, choose rust-resistant varieties, maintain proper orchard sanitation, and use fungicides as needed. Timely removal of infected leaves and vigilant monitoring are essential."
            },
            'scab': {
                'name': 'Scab Disease',
                'description': "Apple scab disease manifests as dark, scaly lesions on leaves and fruit. Prevent scab disease by choosing disease-resistant apple varieties, maintaining good orchard hygiene, and using fungicides during the growing season. To prevent scab disease, choose disease-resistant varieties, maintain good orchard hygiene, and use fungicides as needed. Regular monitoring and prompt treatment are crucial."
            }
        }

    def allowed_file(self, filename):
        # You can add more file extensions if needed
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

    def predict(self, img_path):
        # Load the model (uncomment this when you have a model to load)
        # model = load_model('afd.h5')

        # Open the image using Pillow
        img = Image.open(img_path)

        # Convert the image to RGB mode (if it's not already)
        img = img.convert('RGB')

        # Resize the image to the desired dimensions (e.g., 224x224)
        img = img.resize((224, 224))

        img_array = np.expand_dims(img, axis=0)

        # Make predictions (uncomment this when you have a model to make predictions)
        # prediction = model.predict(img_array)
        # predicted_class_index = np.argmax(prediction, axis=1)[0]
        # predicted_class = self.class_labels[predicted_class_index]

        # For testing purposes, use 'complex' as a placeholder
        predicted_class = 'complex'

        return self.disease_info.get(predicted_class, {'name': 'Unknown Disease', 'description': 'No information available for this disease.'})
