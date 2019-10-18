# USAGE
# python build_dataset.py

# import the necessary packages
from imutils import paths
import shutil
import os
import argparse

TRAIN = "train"
TEST = "test"

BASE_PATH = "dataset"


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
args = vars(ap.parse_args())

# loop over the data splits
for split in (TRAIN, TEST):
	# grab all image paths in the current split
	print("[INFO] processing '{} split'...".format(split))
	p = os.path.sep.join([args["dataset"], split])
	imagePaths = list(paths.list_images(p))

	#print(len(imagePaths))

	# loop over the image paths
	for imagePath in imagePaths:
		# extract class label from the filename
		filename = imagePath.split(os.path.sep)[-1]

		label = filename.split("_")[0]
		# construct the path to the output directory
		dirPath = os.path.sep.join([BASE_PATH,label])

		#print(filename,label,dirPath)

		# if the output directory does not exist, create it
		if not os.path.exists(dirPath):
			os.makedirs(dirPath)

		markFilename=split+"-"+filename

		print("copy:",filename)

		# construct the path to the output image file and copy it
		p = os.path.sep.join([dirPath, markFilename])
		shutil.copy2(imagePath, p)

	print("--infor-- end")
