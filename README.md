# StyleTransfer
In our research this topic has been implemented a lot both in academic fields and industrial fields, but we still think it is worth it to modify it with add-ons and re-implement it because we will have more occasions to mix two images together without losing the originality of the image, and this is a good start to learn about the concept from doing this project.

Although using Tensorflow and VGG to build up the environment of image style transfer is common, we found vgg19 and python 3.7 has some compatibility issues with crucial parts like anaconda3 and even the add-ins for the terminal (oh-my-zsh). So we tried to re-implement it on vgg16 with python 3.6 on Linux, which is successful.

After analyzing multiple implementations on GitHub, google codes and the one from the hvass lab, we tried to figure it out with our style of implementing the image style transfers. However, the core of these different implementations is same, involving 3 steps theoretically.

Traditional Image Style Transfer
Here, we partially re-implemented the traditional and successful image style transfer. After setting up the environment and generated the result from the original code, we re-implemented the image style transfer codes.

Rooms for improvement
Relatively Slow Process: It took at least several minutes to generate a satisfying result, as we use high-resolution image imputs.
Different content images and style images require different weights to generate good results

References

Gatys, L. A., Ecker, A. S., & Bethge, M. (2016). Image Style Transfer Using Convolutional Neural Networks. 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR). doi:10.1109/cvpr.2016.265

Artistic Style Transfer with Convolutional Neural Network. (2018). Retrieved from https://medium.com/data-science-group-iitr/artistic-style-transfer-with-convolutional-neural-network-7ce2476039fd

https://github.com/Hvass-Labs/TensorFlow-Tutorials

https://github.com/fzliu/style-transfer
