import os
from setuptools import setup, Extension
from distutils.command.install_data import install_data


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="RPIO",
    version="0.1.8",
    package_dir={"": "source"},
    py_modules=["RPIO"],
    ext_modules=[Extension('GPIO', ['source/c_gpio/py_gpio.c', \
            'source/c_gpio/c_gpio.c', 'source/c_gpio/cpuinfo.c'])],
    #data_files=[('/sbin', ['source/rpio'])],
    scripts=["source/rpio"],

    description=("An extension of RPi.GPIO to easily use interrupts on the "
            "Raspberry Pi"),
    long_description=read('README.txt'),
    url="https://github.com/metachris/RPIO",

    author="Chris Hager",
    author_email="chris@linuxuser.at",

    license="MIT",
    keywords=["raspberry", "raspberry pi", "interrupts", "gpio", "gpio2"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Topic :: Home Automation",
        "Topic :: System :: Hardware",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)