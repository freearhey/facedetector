from setuptools import setup, find_packages

with open("README.md", "r") as f:
  long_description = f.read()

setup(
  name="facedetector-py",
  version="0.0.4",
  description='Python script for detecting faces in an image',
  long_description=long_description,
  long_description_content_type='text/markdown',
  packages=find_packages(),
  url='https://github.com/freearhey/facedetector',
  author='Arhey',
  license='MIT',
  python_requires='>=3.5.5',
  install_requires=["retina-face>=0.0.12", "numpy>=1.14.0"],
  extras_require={
    'dev': ["pytest>=7.0", "twine>=4.0.2"]
  }
)