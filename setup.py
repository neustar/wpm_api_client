from setuptools import setup

setup(
    name='wpm_api_client',
    version='2.7.1',
    description='A Python library for the Web Performance Management API',
    url='https://github.com/neustar/wpm_api_client',
    author='Shane Barbetta',
    author_email='shane@barbetta.me',
    license='Apache License, Version 2.0',
    keywords='wpm_api_client',
    packages=['wpm_api'],
    package_dir={'wpm_api': 'src'},
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
    ],
    zip_safe=False,
)