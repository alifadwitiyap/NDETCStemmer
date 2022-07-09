import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
name='NDETCStemmer',  
version='1.0.0',
py_modules=['NDETCStemmer'] ,
description="Library untuk stemming kata dalam Bahasa Indonesia menggunakan metode Nondeterministic Context",
long_description=long_description,
long_description_content_type="text/markdown",
url="https://github.com/alifadwitiyap/NDETCStemmer",
packages=setuptools.find_packages(),
classifiers=[
	# How mature is this project? Common values are
	#   3 - Alpha
	#   4 - Beta
	#   5 - Production/Stable
	'Development Status :: 3 - Alpha',
	# that you indicate whether you support Python 2, Python 3 or both.
		"Programming Language :: Python :: 3",
		# Indicate who your project is intended for
	'Intended Audience :: Information Technology',
	'Intended Audience :: Science/Research',
	'Topic :: Text Processing :: Linguistic',
],
# What does your project relate to?
keywords='linguistic stemming indonesian bahasa',
install_requires=[
	'nltk',
	'gensim'
]
)