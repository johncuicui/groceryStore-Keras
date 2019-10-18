
# Color Splash Example

This is an example showing the use of Mask RCNN in a real application.
We train the model to detect balloons only, and then we use the generated 
masks to keep balloons in color while changing the rest of the image to
grayscale.


[This blog post](https://engineering.matterport.com/splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow-7c761e238b46) describes this sample in more detail.

![Balloon Color Splash](/assets/balloon_color_splash.gif)
![Balloon Color Splash](assets/show/store.jpg)

## Installation
From the [Releases page](https://github.com/matterport/Mask_RCNN/releases) page:
1. Download `mask_rcnn_balloon.h5`. Save it in the root directory of the repo (the `mask_rcnn` directory).
2. Download `balloon_dataset.zip`. Expand it such that it's in the path `mask_rcnn/datasets/balloon/`.



#Grocery Store Image classification with Keras
This repository contains a classification with Keras and deep learning on [grocery store image dataset](https://github.com/marcusklasson/GroceryStoreDataset). This dataset not only contains a large volume of natural images but also includes the corresponding information. We reorganize the dataset because our aim is to build a simple classification model。Then we fine-tune the DenseNet-169 for 100 epochs one our dataset. 
##data
Down the grocery store image dataset.It is available at https://github.com/marcusklasson/GroceryStoreDataset.
##build dataset
```
build_dataset ----dataset=/path to grocery store image dataset
```
There are 81.
![Instance Segmentation Sample](assets/show/store.jpg)
##train
```
--dataset dataset --model output/activity.model --label-bin output/lb.pickle --plot output/plot.png --epochs 100
```

![Instance Segmentation Sample](assets/show/plot.png)
##predict
```
--model output/activity.model --labels output/lb.pickle --image assets/Granny-Smith.jpg
```
<p align="left">
  <img src="assets/show/predict1.jpg" width="300" title="hover text">
  <img src="assets/show/predict2.jpg" width="300" title="hover text">
</p>
<p align="left">
  <img src="assets/show/predict3.jpg" width="300" title="hover text">
  <img src="assets/show/predict4.jpg" width="300" title="hover text">
</p>

