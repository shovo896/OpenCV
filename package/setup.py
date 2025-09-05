# setup.py
from setuptools import setup, find_packages

setup(
    name='opencv_custom',            # your package name
    version='0.1.0',
    description='Custom OpenCV utility code',
    author='MD Ahadul Haque Suvo',
    packages=find_packages(),        # automatically finds opencv_custom folder
    install_requires=[
        'numpy',                     # add other dependencies here
        'opencv-python',
    ],
    python_requires='>=3.8',
)
