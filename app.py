import os
from flask import Flask, render_template, request
from keras.preprocessing import image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load your trained model
model = tf.keras.models.load_model('model.h5')

# Ensure the uploads directory exists
uploads_dir = 'uploads'
os.makedirs(uploads_dir, exist_ok=True)

# Function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(180, 180), color_mode='grayscale')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        file = request.files['image']
        if file:
            file_path = os.path.join(uploads_dir, file.filename)
            file.save(file_path)  # Save the uploaded file
            img_array = preprocess_image(file_path)  # Preprocess the image
            predictions = model.predict(img_array)
            prediction = 'Pneumonia' if predictions[0][0] < 0.5 else 'Normal'
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable
    app.run(host='0.0.0.0', port=port, debug=True)
