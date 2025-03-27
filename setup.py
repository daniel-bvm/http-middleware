# Copyright 2023 parkminwoo, MIT License
from setuptools import find_packages
from setuptools import setup

setup(
    name="eai_http_middleware",
    version="1.0.0",
    author="daniel",
    author_email="daniel@bvm.network",
    description="A mcp proxy",
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=[], include=["eai_http_middleware", "eai_http_middleware.*"]),
    python_requires=">=3.7",
    keywords="proxy, http, middleware",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ]
)