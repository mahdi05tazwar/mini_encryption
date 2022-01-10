from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mini_encryption',
    version='0.0.1',
    description="A simple encryption and decryption library. Usage has been described in this page; if not, then: Download the library and open a python file. Type \"from mini_encryption import explain\" and then in the next line, type \"explain()\"",
    author='Mahdi Tazwar Raeed',
    url = 'https://mahditaz.pythonanywhere.com',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['encryption', 'encrypt', 'encryptor', 'mini', 'simple', 'mahdi', 'tazwar', 'raeed', 'mahditaz', 'shaion'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.1',
    py_modules=['mini_encryption'],
    #package_dir={'':''},
    install_requires = []
)