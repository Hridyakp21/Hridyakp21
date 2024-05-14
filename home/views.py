from django.shortcuts import render
from . models import *
from django.conf import settings
# from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from keras.preprocessing import image
from tensorflow.keras.models import load_model

import numpy as np
import os




# Create your views here.

# Load the currency detection model
filepath = 'D:\\project1 (1)\\project1\\Trainingsets\\mymodel1.h5'
model = load_model(filepath)

def currency_pred(request):
    if request.method == 'POST':
        file = request.FILES['image'] # fet input
        filesave= UploadImage(image=file)
        filesave.save()
        filename = str(filesave.image)   
        print("@@ Input posted = ", filename)
        path = settings.MEDIA_ROOT
        print("Path =  ",path)
        print(path + "/" +filename)

        file_path = path + "\\" +filename

        print(file_path)
        print("@@ Predicting class......")
  
        new_img = image.load_img(file_path, target_size=(224, 224))
        new_img_array = image.img_to_array(new_img)
        new_img_array = np.expand_dims(new_img_array, axis=0)
        new_img_array /= 255.0  # Normalize the image # change dimention 3D to 4D
        
        result = model.predict(new_img_array) # predict fake currency or not
        print('@@ Raw result = ', result)
        
        pred = np.argmax(result)
        classlabels = ['Fake', 'Real']
        predicted_label = classlabels[pred]
        print(predicted_label)
        if predicted_label=='Fake':
            input_image = filename
            text = "Uploaded image of currency is Fake"
            # desc ="Copper fungicides are the most commonly recommended treatment for bacterial leaf spot. Use copper fungicide as a preventive measure after you’ve planted your seeds but before you’ve moved the plants into their permanent homes. You can use copper fungicide spray before or after a rain, but don’t treat with copper fungicide while it is raining. If you’re seeing signs of bacterial leaf spot, spray with copper fungicide for a seven- to 10-day period, then spray again for one week after plants are moved into the field. Perform maintenance treatments every 10 days in dry weather and every five to seven days in rainy weather."
            return render(request, 'curren/precurrency.html',{'input_image':input_image,'pred_text':text})
            
        elif predicted_label=='Real':
            input_image = filename
            text = "Uploaded image of currency is real"
            # desc = "Tomatoes that have early blight require immediate attention before the disease takes over the plants. Thoroughly spray the plant (bottoms of leaves also) with Bonide Liquid Copper Fungicide concentrate or Bonide Tomato & Vegetable. Both of these treatments are organic."
            return render(request, 'curren/precurrency.html',{'input_image':input_image,'pred_text':text})                 
                         

                
        





def home(request):
    return render(request,"index.html")

def currency(request):
    return render(request,"curren/currency.html")


def news(request):
    return render(request,"news.html")
def website(request):
    return render(request,"website.html")
def feedback(request):
    return render(request,"feedback.html")