
# USAGE
# python predict.py --model output/activity.model --labels output/lb.pickle --image assets/pic/Yellow-Onion.jpg

# import the necessary packages
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

import pickle

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to our input image")
ap.add_argument("-m", "--model", required=True,
	help="path to output serialized model")
ap.add_argument("-l", "--labels", required=True,
	help="path to output label binarizer")
args = vars(ap.parse_args())

# load the class label names from disk, one label per line
categoryLB = pickle.loads(open(args["labels"], "rb").read())

# load the input image and then clone it so we can draw on it later
image = cv2.imread(args["image"])
output =image.copy()
output = imutils.resize(output, width=400)

# our model was trained on RGB ordered images but OpenCV represents
# images in BGR order, so swap the channels, and then resize to
# 224x224 (the input dimensions for DenseNet169)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (224, 224))

# convert the image to a floating point data type and perform mean
# subtraction
image = image.astype("float32")
mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
image -= mean

# load the trained model from disk
print("[INFO] loading model...")
model = load_model(args["model"])

#print(model.summary())

# pass the image through the network to obtain our predictions
preds = model.predict(np.expand_dims(image, axis=0))[0]
i = np.argmax(preds)
label = categoryLB.classes_[i]

# draw the prediction on the output image
text = "{}: {:.2f}%".format(label, preds[i] * 100)
cv2.putText(output, text, (3, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
	(0, 255, 0), 2)

# show the output image
cv2.imshow("Predict", output)
cv2.imwrite("Output/predict.jpg",output)

cv2.waitKey(0)