## GAN-for-Recolourization
1. A Pix2Pix Generative Adversarial Network (GAN) model was constructed to produce recolored images for assisting
the process of diagnosis of patients with color vision deficiency
2. The dataset utilized for training the model was custom-created by merging multiple existing datasets
3. The generated images exhibited an error rate of less than 0.05 when compared to the actual simulated images
4. The development process for the project followed the Agile methodology
5. Model was deployed on Streamlit Cloud<br>

#### NOTE: <br>
1. If the app is not used for a long time, it goes to sleep. If you wake it up, it will take utmost 5 mins to see the app
2. In pix2pix-gan.ipynb: Unable to hide 'training' output despite enabling scrolling, so the length of the notebook increased
<br>

#### OUTPUT: <a href="https://sanjay906-gan-recolourization-mebu9asdk0q.streamlit.app/" target="_blank">recolor-web-app</a>
<br>

### RECOLOURIZATION:<br>
A protanope is a person with protanopia, who can not see the red color due to the absence of red cones in the eyes. Daltonization is an algorithm which is used for recolouring the images so that it makes a protanope distinguish it from other colors. It doesn't cure protanopia but it makes it easy for the patient to differentiate from green and red shades<br>
<br>
![recolor](https://raw.githubusercontent.com/sanjay-906/GAN-for-Recolourization/main/pictures/expression.png)

<br>

### Pix2Pix Architecture:<br>
Pix2Pix contains a generator(U-Net) and a discriminator(Patch-GAN). These two neural networks play a zero-sum game as a training process where one's loss is other's gain. The generator's responsibility is to produce images which are realistic enough to fool the discriminator and the discriminator's role is to not get fooled by the generator. This process continues untill an equilibrium is achieved. <br>
<br>
Input images are recoloured using the standard daltonization algorithm. A daltonized image is our 'target' and the original image is our source. Both of these images data are given to the model and the model is trained. Now the model is ready to perform Image translation. <br>
<br>
![arch](https://raw.githubusercontent.com/sanjay-906/GAN-for-Recolourization/main/pictures/Arch.png)

<br>

### TESTING:<br>
Initially, the generated images are noisy, but as the training goes on, they become more realistic. In this project, we trained on a dataset(images of birds, plants, cars etc...) with 2600 images (which is very less, due to limited hardware resources) for 1 epoch to get these results<br>
<br>
![testing](https://raw.githubusercontent.com/sanjay-906/GAN-for-Recolourization/main/pictures/testing.png)

<br>

### OUTPUT:<br>

![output](https://raw.githubusercontent.com/sanjay-906/GAN-for-Recolourization/main/pictures/output1.png)

<br>
<br>

### VIDEO RECOLOURIZATION:<br>



https://github.com/sanjay-906/GAN-for-Recolourization/assets/99668976/91b0b7fc-096f-44dc-ad4c-fd93d5d33c4e

<br>


https://github.com/sanjay-906/GAN-for-Recolourization/assets/99668976/6774d3a0-6d9b-4569-b855-2865edf57c09

### WEB-APP DEMO:<br>
Full high quality video is in pictures folder

<br>



https://github.com/sanjay-906/GAN-for-Recolourization/assets/99668976/31467d91-e5c5-4977-a054-288e26a104c6



### NOTE:<br>
1. Provided higher computation power, the model can be configured to produce high quality recoloured images.
2. The model in the current state can also recolour videos, but the output has 1:1 aspect ratio (also, the process itself is too slow)
