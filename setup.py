# -*- coding: utf-8 -*-

import setuptools
import pathlib


HERE = pathlib.Path(__file__).parent

# The text of the README file
long_description = (HERE / "README.md").read_text()

setuptools.setup(
    name='metronome_loop',
    version='0.1.0',
    author='Jakub Andrýsek',
    author_email='email@kubaandrysek.cz',
    description='Library for easy timing without time.sleep()',
    url='https://github.com/JakubAndrysek/metronome_loop',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='metronome_loop, loop, sleep, time',
    license='MIT',
    packages=['metronome_loop'],
    # install_requires=[
    #     "",
    #     "typing",
    # ],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
