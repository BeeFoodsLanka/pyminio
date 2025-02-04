import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyminio",
    version="0.2.1",
    author="Michael Tugendhaft",
    author_email="tugmica@gmail.com",
    description="Python client for Minio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mmm1513/pyminio",
    packages=setuptools.find_packages(),
    install_requires=[
        'minio',
        'pytz',
        'cached-property',
        'attrdict',
        'dataclasses'
    ],
    extras_require={
        'dev': [
            'pytest',
            'flake8',
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
        'Programming Language :: Python :: 3.9'
    ],
    python_requires='>=3.6',
)
