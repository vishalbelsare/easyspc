# Sparse principal components analysis based on SVD.
## Content
This package implements the sparse principal components algorithm developed by Shen and Huang and explained in [this paper]( http://www.sciencedirect.com/science/article/pii/S0047259X07000887).

This implementation is faster and easier than the one proposed in [Scikit learn](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA). Please check the [post on my blog](https://smartparrot.wordpress.com/2017/09/30/spca/) if you want more information about this method. There is also a Jupyter notebook file that shows how SPCA can be used on images to detect objects of interest.

## Getting started
Besides a recent version of Numpy, the PyWavelets package is required in order to perform thresholding operations
### Prerequisites
```
pip install PyWavelets
```

### Installing

To install easyspc you can just use pip

```
pip install easyspc
```
## Example


### Computation of sparse principal components and sparse low rank approximation
U is the learnt left singular vectors matrix
V is the learnt right singular vectors matrix (the sparse approximation of the covariance matrix eigenvectors)
W is the matrix containing the standard estimation of the covariance matrix eigenvectors

```
>>> import numpy as np
>>> from easyspc import SPC
>>> X_ = np.random.normal(size=(1000,2000))
>>> spc = SPC( 4, max_iter=10, threshold_val=1.5 )
>>> U, V, W = spc.fit(X_)
>>> X_low_rank_approximation = spc.transform(X_)
```
