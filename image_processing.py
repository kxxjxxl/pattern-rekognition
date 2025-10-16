# -*- coding: utf-8 -*-

"""
Image Processing Module.
@author Rodrigo Hernandez-Mota
"""

from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np
import wget
import os


def downloadImage(image_url, path=None):
    """Download an image given an url."""
    if not path:
        path = "imgs"
        if not os.path.isdir("imgs"):
            os.makedirs("imgs")
    image_filename = wget.download(image_url, out=path)
    return image_filename


def openImage(filename, pillow=True):
    """Open an image given a filename or path."""
    if pillow:
        image_file = Image.open(filename)
        return image_file  # np.asarray()
    with open(filename, "rb") as imageFile:
        image_file = imageFile.read()
        img = np.array(image_file)
    return img


def saveImage(img, filename):
    """Save an image given numpy bytes array."""
    bytes_array = bytearray(img)
    with open(filename, "wb") as newImage:
        newImage.write(bytes_array)
    return True


def getImage(image_url, path=None, delete=False,
             pillow=True, resize=(300, 300)):
    """Download and opens an image."""
    filename = downloadImage(image_url, path)
    img = openImage(filename, pillow)
    if resize:
        img.thumbnail(resize, Image.ANTIALIAS)
        new_img = Image.new('RGBA', resize, (255, 255, 255, 0))
        new_img.paste(img, (int((resize[0] - img.size[0]) / 2),
                            int((resize[1] - img.size[1]) / 2)))
    else:
        new_img = img
    if delete:
        os.remove(filename)
    return np.asarray(new_img)


def meanTransform(img):
    """Return an image matrix with necesary values for grayscale."""
    dim = img.shape
    gray_img = []

    def activateWB(value, threshold):
        return (np.uint8(0) if value < threshold else np.uint8(255))

    for row in range(dim[0]):
        gray_img.append([])
        for col in range(dim[1]):
            reference_vals = img[row][col][:-1]
            _average = np.mean(reference_vals)
            # Note: use img[row][col][-1] instead of np.uint8(255)
            gray_img[-1].append(list(map(
                                         lambda x: activateWB(x, _average),
                                         reference_vals))+[np.uint8(255)])
    return np.asarray(gray_img)


def detectPattern(img, pattern=np.array([255, 0, 0, 255])):
    """Detect a given arrange of pixel RGBA."""
    def booleanCheck(_array, pattern):
        return -2*(sum(_array == pattern) != 4) + 1
    dim = img.shape
    data = []
    for row in range(dim[0]):
        data.append([])
        for col in range(dim[1]):
            reference_vals = img[row][col][:]
            data[-1].append(booleanCheck(reference_vals, pattern))
    return np.asarray(data)


def featureExtraction(img):
    """Get some generic features."""
    pass


def performConvolution(feature, img):
    """Convolv an imag and return a "layer"."""
    pass


def maxPooling(img, size=(3, 3)):
    """Perform pooling operation at a filtered image."""
    pass


def relu():
    """Perform a Rect. Linear Unit computation."""
    pass


def vectorizeImage(img, ops=None):
    """Vectorize an image following a set of operations."""
    def matrix2vect(matrix):
        dim = np.shape(matrix)
        vector = []
        for i in range(dim[0]):
            for j in range(dim[-1]):
                vector.append(matrix[i][j])
        return np.array(vector)
    if not ops:
        return matrix2vect(img)
    return img
