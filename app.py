
from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='cnn-parameters-improvement-27-0.89.model'

# Load your trained model
model = load_model(MODEL_PATH)




def model_predict(img_path, model):
    #img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    #x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    #x=x/255
    #x = np.expand_dims(x, axis=0)
    
   IMG_SIZE = 240
   img_array = cv2.imread(filepath)
   img_array = cv2.cvtColor(img_array ,cv2.COLOR_BGR2RGB)
   new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
   x=new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)
   

   

    preds = model.predict(x)

    res=int(preds[0][0])
    if(res==1):
      preds= 'Yes Brain Tumor'
    else:
      preds= 'No Brain Tumor'
    
    
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)
