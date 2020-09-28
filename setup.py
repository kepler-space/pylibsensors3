"""Setup script for pylibsensors3 package."""

import setuptools

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()

setuptools.setup(
        name="pylibsensors3",
        version="0.0.1",
        author="Pavel Rojtberg",
        author_email="mail@rojtberg.net",
        description="Python Bindings for libsensors3",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        url="https://github.com/paroj/sensors.py",
        py_modules=["sensors"],
        classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
                "Operating System :: OS Independent",
        ],
        python_requires='>=3.0',
)
