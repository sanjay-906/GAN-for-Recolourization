import streamlit as st
import numpy as np
import time
from PIL import Image
import requests
import numpy as np
import cv2
import sklearn
from keras.models import load_model
import keras
from io import BytesIO, StringIO

import urllib.request

import matplotlib.pyplot as plt
import os
from PIL import Image
from keras.models import load_model
from tensorflow.keras.optimizers import Adam


st.title('Image Recolouring for Protanopia')

st.markdown("***")

def predict(img):


    model=load_model('model_2600d.h5',compile=False)
    opt=Adam(learning_rate=0.0002,beta_1=0.5)
    model.compile(loss= 'binary_crossentropy', optimizer= opt, loss_weights= [0.5])

    gen=model.predict(img)

    data= np.vstack((img, gen))
    data= (data+1)/2.0


    fig= plt.figure(figsize=(16,9))

    title=['Original', 'Daltonized']

    plt.subplot(1, 2, 1)
    plt.axis('off')
    plt.imshow(data[0])
    plt.title(title[0],fontsize = 40)


    plt.subplot(1, 2, 2 )
    plt.axis('off')
    plt.imshow(data[1])
    plt.title(title[1],fontsize = 40)
    st.pyplot(fig)

st.subheader('Brief')
st.markdown('Colour blindeness to red is called Protanopia, a condition where the red cones are absent in a person\'s eye. A person with protanopia is unable to perceive any \'red\' light')


f1="https://raw.githubusercontent.com/sanjay-906/GAN-for-Recolourization/main/pictures/colorspectrum.png"
im1= Image.open(requests.get(f1, stream=True).raw)
st.image(im1)


st.markdown('It is harder for a protanope to differentiate between the shades of red and green')
st.markdown('There is no cure for protanopia at present, but there are many ways to manage this issue')
st.markdown('Daltonization is an algorithm which recolours \'red\' parts of an image which makes it look different from the shades of green')


f2="https://raw.githubusercontent.com/sanjay-906/GAN-for-Recolourization/main/pictures/image.png"
im2= Image.open(requests.get(f2, stream=True).raw)
st.image(im2)

st.markdown('Original Images and Images generated using daltonization are fed to our Pix2Pix GAN which uses Image translation to learn and to generate recoloured images without the algorithm')

st.subheader('Upload any image')
file = st.file_uploader("Choose a file",type = ['jpg', 'png','jpeg'],accept_multiple_files = False)

if file is None:
    st.text("Please upload an image file")
else:
    st.text('Please wait, Image is processing...')
    img = cv2.imdecode(np.fromstring(file.read(), np.uint8), 1)
    img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img=Image.fromarray(img,mode='RGB')
    image= np.asarray(img)
    new_array = cv2.resize(image, (256, 256))

    srcimage=list()
    srcimage.append(new_array)
    src=np.asarray(srcimage)
    src= (src - 127.5)/127.5

    predict(src)

    st.markdown('Although, a protanope still cannot see red color, with daltonization atleast it is possible to differentiate colors')

    link = '[back to github](https://github.com/sanjay-906/GAN-for-Recolourization)'
    st.markdown(link, unsafe_allow_html=True)
