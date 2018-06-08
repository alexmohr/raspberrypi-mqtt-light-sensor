# pylint: disable=invalid-name, exec-used
"""Setup raspberrypi-mqtt-light-sensor package."""
from __future__ import absolute_import
import sys
import os
from setuptools import setup
# import subprocess
sys.path.insert(0, '.')

CURRENT_DIR = os.path.dirname(__file__)

with open('README.md', 'r') as myfile:
    long_description = myfile.read()


# python setup.py register sdist upload
# and be sure to test it firstly using "python setup.py register sdist
# upload -r pypitest"
setup(name='raspberrypi-mqtt-light-sensor',
      # this must be the same as the name above
      packages=['raspberrypi-mqtt-light-sensor'],
      version='0.2.3',
      description='Reading a LDR with a raspberry pi and publishing the data via mqtt',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Alexander Mohr',
      author_email='pypy@mohr.io',
      # use the URL to the github repo
      url='https://github.com/alexmohr/raspberrypi-mqtt-light-sensor',
      download_url='https://codeload.github.com/alexmohr/raspberrypi-mqtt-light-sensor/tar.gz/0.2.3',
      keywords=['mqtt', 'rpi', 'raspberypi', 'light', 'sensor'],
      license='MIT',
      classifiers=[],
      install_requires=[
          'paho-mqtt'
      ],
      )
