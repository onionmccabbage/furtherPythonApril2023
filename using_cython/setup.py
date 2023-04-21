from setuptools import setup
from Cython.Build import cythonize # pip install cython

setup(
    ext_modules = cythonize("sample.pyx")
)