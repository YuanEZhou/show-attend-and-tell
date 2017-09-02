# show-attend-and-tell
This is a modification version of  yunjey's code https://github.com/yunjey/show-attend-and-tell.  
TensorFlow~1.2 Implementation of "Show, Attend and Tell".

1.In the original code, the train.features.hkl file is too big to load in my computer's RAM. SO,I don't produce the image feature vectors in the preprocess step. When I need a batch of image feature vectors, I call sess.run(vggnet.features, feed_dict={vggnet.images: image_batch}) instead. Though repeated calculation was made, the need of RAM capacity is relief.

2.I modify the implementation of doubly stochastic regularization which makes more sense.

3.I use weight transposed shared trick which reduces model parameters and gains a point promotion for BLEU1 metricI 

4.I change the vocabulary size to 10000.

