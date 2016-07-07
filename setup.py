from setuptools import setup, find_packages

setup(name='patreon',
      version='0.3.1',
      description='Python library for interacting with the Patreon API. OAuth-centric for now.',
      url='http://github.com/Patreon/patreon-python',
      author='Patreon',
      author_email='david@patreon.com',
      license='Apache 2.0',
      packages=find_packages(),
      install_requires=[
          'requests',
      ],
      zip_safe=True,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ])
