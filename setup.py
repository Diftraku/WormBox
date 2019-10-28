import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wormbox",
    version="1.0.0",
    author="Antti Nilakari",
    author_email="antti.nilakari@gmail.com",
    description="Python (half-complete) implementation of Finnish WW2 Vigenère cipher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andyn/WormBox",
    packages=setuptools.find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': ['wormbox=wormbox.wormbox:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
