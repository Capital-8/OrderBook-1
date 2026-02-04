from pathlib import Path

from setuptools import setup


README = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

setup(
    name='OrderBook',
    version='0.1.2',
    author='Michael Nguyen',
    author_email='dyn4mik3@gmail.com',
    packages=['orderbook'],
    url='https://pypi.org/project/OrderBook/',
    license='LICENSE.txt',
    description='Limit Order Book Matching Engine',
    long_description=README,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    install_requires=[
        'sortedcontainers >= 2'
        ],
    scripts=['bin/algosim.py'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    )
