#!/usr/bin/env python3
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="enrichr",
    version="0.0.1",
    author="Enrichr Project",
    author_email="contact@enrichr.io",
    description="Security Enrichment Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enrichr-io/enrichr",
    packages=setuptools.find_packages(),
    extra_require={
        'cli': ['enrichr-cli'],
        'free': ['enrichr-extract-text'],
    },
    install_requires = [
        "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires='>=3.6',
)
