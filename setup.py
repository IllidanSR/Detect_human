from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['Pillow>=1.0', 'Matplotlib>=2.1', 'Cython>=0.28.1','Tensorflow-gpu>=1.5']
setup(
    name='Human detect',
    version='1.0',
    author='Sergei Matyshev',
    author_email="SergeiMatyshev@hotmail.com",
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=[p for p in find_packages() if p.startswith('Detect_human')],
    description='Tensorflow Object-Detection, with face recognition and calculate human in frame',
)