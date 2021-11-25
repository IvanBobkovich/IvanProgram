from setuptools import setup
from setuptools import find_namespace_packages


with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(

    name='Dealership-app',
    author='Bobkovich Ivan',
    author_email='ivanbobkovich199@gmail.com',
    version='0.1.0',
    description='Web application that allows the administrator to record information about cars',
    url='https://github.com/IvanBobkovich/IvanProgram',
    install_requires=[
        'Django',

    ],

    classifiers=[

        'Framework :: Django',
        'Framework :: Django :: X.Y  # Replace "X.Y" as appropriate'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'

    ]
)