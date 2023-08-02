import os
import sys
import json
import unittest
sys.path.append('...')

from facedetector import FaceDetector

class FaceDetectorTest(unittest.TestCase):
	def test_detect_faces(self) -> None:
		img = os.path.abspath("tests/__data__/example.jpg") # Photo by (Eddi Aguirre)[https://unsplash.com/@soloeddi]
		faces = FaceDetector.detect(img)
		f = open('tests/__data__/expected.txt')
		expected = f.read()
		self.assertEqual(str(faces), expected)
		f.close()