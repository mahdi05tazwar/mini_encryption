from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='minimal_encryption',
  version='0.0.1',
  description='A simple package/system encryption and decryption. The way of using the package has been described.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Mahdi Tazwar Raeed',
  author_email='mahdi05tazwar@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['encryption', 'encrypt', 'decrypt', 'decryption', 'encryptor'], 
  packages=find_packages(),
  install_requires=[''] 
)
