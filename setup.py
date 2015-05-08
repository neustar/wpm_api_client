from setuptools import setup

setup(
    name='wpm_client',
    version='0.1',
    description='A Python library for the Web Performance Management API',
    url='https://github.com/ultradns/wpm_api_client',
    author='Shane Barbetta',
    author_email='shane@barbetta.me',
    license='Apache License, Version 2.0',
    keywords='wpm_api',
    packages=['wpm_api'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
    ],
    zip_safe=False
)