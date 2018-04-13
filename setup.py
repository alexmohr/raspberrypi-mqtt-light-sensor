# pylint: disable=invalid-name, exec-used
"""Setup raspberrypi-mqtt-light-sensor package."""
from __future__ import absolute_import
import sys
import os
from setuptools import setup, find_packages
# import subprocess
sys.path.insert(0, '.')

CURRENT_DIR = os.path.dirname(__file__)

# to deploy to pip, please use
# make pythonpack
# python setup.py register sdist upload
# and be sure to test it firstly using "python setup.py register sdist upload -r pypitest"
setup(name='raspberrypi-mqtt-light-sensor',
  packages = ['raspberrypi-mqtt-light-sensor'], # this must be the same as the name above
  version = '0.1.0',
  description = 'Reading a LDR with a raspberry pi and publishing the data via mqtt',
  author = 'Alexander Mohr',
  author_email = 'sonyapilib@mohr.io',
  url = 'https://github.com/alexmohr/raspberrypi-mqtt-light-sensor', # use the URL to the github repo
  download_url = 'https://codeload.github.com/alexmohr/raspberrypi-mqtt-light-sensor/tar.gz/0.1.0',
  keywords = ['mqtt', 'rpi', 'raspberypi', 'light', 'sensor'], 
  classifiers = [],
  install_requires=[
      'paho-mqtt'
  ],
)