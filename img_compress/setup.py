from setuptools import setup, find_packages

setup(
    name="img_compress",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['Pillow'],
    description="A Python module for compressing images.",
    author="Sharukh Mohammed",
    author_email="sharukhmohammed@me.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Android - Termux (Targeted)",
    ],
    python_requires='>=3.11',
)