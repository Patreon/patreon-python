from setuptools import setup

setup(name='patreon',
      version='0.1',
      description='Python library for interacting with the Patreon API. OAuth-centric for now.',
      url='http://github.com/Patreon/patreon-python',
      author='Patreon',
      author_email='david@patreon.com',
      license='MIT',
      packages=['patreon'],
      install_requires=[
          'requests',
      ],
      zip_safe=True)

#python setup.py register sdist upload