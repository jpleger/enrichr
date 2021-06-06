#!/usr/bin/env python3
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="enrichr",
    version="0.0.6",
    author="James Pleger",
    author_email="jpleger@gmail.com",
    description="Security Enrichment Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jpleger/enrichr",
    extra_require={
        'cli': ['enrichr-cli'],
        'free': [
            'enrichr-cli',
            'enrichr-extract-text',
        ],
    },
    zip_safe=False,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
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
