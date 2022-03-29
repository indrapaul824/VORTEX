import tensorflow as tf
from keras.preprocessing.image import img_to_array, load_img
from keras.models import load_model
import numpy as np
import mimetypes
import argparse
from termcolor import colored
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image/text file of image filenames")
args = vars(ap.parse_args())

# determine the input file type, but assume that we're working with
# single input image
filetype = mimetypes.guess_type(args["input"])[0]
imagePaths = [args["input"]]
# if the file type is a text file, then we need to process *multiple*
# images
if "text/plain" == filetype:
	# load the filenames in our testing file and initialize our list
	# of image paths
	filenames = open(args["input"]).read().strip().split("\n")
	imagePaths = []
	# loop over the filenames
	for f in filenames:
		# construct the full path to the image filename and then
		# update our image paths list
		p = os.path.sep.join(["../../data/processed/Obj_Det/images", f])
		imagePaths.append(p)

def get_key(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "Key doesn't exist"

# load our trained intensity estimator from disk
model = load_model("../artifacts/in_estimator/in_estimator.h5")

for imagePath in imagePaths:
    classes = {'EXTREME':0, 'NORMAL':1, 'SEVERE':2, 'SUPER':3, 'VERY':4}
    
    
    image = load_img(imagePath, target_size=(100, 100))
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    
    # Predict the values from the validation dataset
    Y_pred = model.predict(image)
    # Convert predictions classes to one hot vectors 
    Y_pred_classes = np.argmax(Y_pred,axis = 1) 

    print(colored("The predicted class for the given image is: ", "green"), colored(get_key(classes, Y_pred_classes[0]), "red"))