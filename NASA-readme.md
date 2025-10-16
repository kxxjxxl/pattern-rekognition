# NetCDF recognizer.

A Python image processing library for feature extraction, pattern detection, and image transformations.

## Features

- **Image Acquisition**: Download and load images from URLs with automatic resizing
- **Grayscale Transformation**: Custom mean-based grayscale conversion with threshold activation
- **Pattern Detection**: Identify specific RGBA pixel patterns within images
- **Image Vectorization**: Convert image matrices to vector format for machine learning applications
- **Convolution Operations**: Framework for convolutional neural network operations (in development)

## Installation

```bash
pip install pillow matplotlib numpy wget
```

## Quick Start

```python
from image_processing import getImage, meanTransform, detectPattern, vectorizeImage

# Download and load an image
img = getImage("https://example.com/image.jpg", resize=(300, 300))

# Apply grayscale transformation
gray_img = meanTransform(img)

# Detect red pixels (RGBA: 255, 0, 0, 255)
pattern_map = detectPattern(gray_img)

# Vectorize for ML processing
vector = vectorizeImage(pattern_map)
```

## Core Functions

### `getImage(image_url, path=None, delete=False, pillow=True, resize=(300, 300))`

Downloads and opens an image with optional resizing and automatic cleanup.

### `meanTransform(img)`

Converts an image to grayscale using mean-based thresholding for each pixel's RGB channels.

### `detectPattern(img, pattern=[255, 0, 0, 255])`

Detects specified RGBA patterns and returns a binary map indicating matches.

### `vectorizeImage(img, ops=None)`

Flattens image matrices into vectors suitable for machine learning pipelines.

## Future Development

- Convolutional layer implementation
- Max pooling operations
- ReLU activation functions
- Advanced feature extraction methods

## License

MIT License
