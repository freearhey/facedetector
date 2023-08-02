# FaceDetector

Python script for detecting faces in an image.

## Installation

```sh
pip install facedetector-py
```

## Usage

```py
from facedetector import FaceDetector

img = 'path/to/image.jpg' # or NumPy array
faces = FaceDetector.detect(img)

print(faces)
```

Output:

```py
[
  {
    'score': 0.9990496039390564, 
    'angle': -5.194428907734846, 
    'pivot': (1960, 819), 
    'coordinates': [(1920, 782), (1993, 775), (1999, 848), (1927, 855)],
    'bounding_box': {
      'x': 1920, 
      'y': 775, 
      'width': 79, 
      'height': 80
    }, 
    'landmarks': {
      'right_eye': (1949.1595, 809.30695), 
      'left_eye': (1970.3654, 808.0268), 
      'nose': (1963.1459, 819.6671), 
      'mouth_right': (1953.5267, 830.48206), 
      'mouth_left': (1968.4865, 829.6616), 
      'eyes_center': (1959, 808), 
      'mouth_center': (1961, 830),
      'face_center': (1960, 819)
    }
  },
  ...
]
```

## Test

```sh
pytest tests/
```

## License

[MIT](LICENSE)