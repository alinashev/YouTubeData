from setuptools import setup

setup(name='YouTubeData',
      version='1.0',
      author='Alina Shevchenko',
      packages=['Action', 'Analysis', 'Commons', 'Entities', 'Extract', 'Load', 'Report', 'Settings', 'Transform'],
      install_requires='requirements.txt',
      scripts=[
          'main.py',
          'requirements.txt',
          'categories.txt',
          'channels.txt'
      ],

      )
