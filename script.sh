#!/bin/sh

pyenv install 2.7.11
echo "Python 2.7.6 installed"
pyenv install 3.6.4
echo "Python 3.6.4 installed"

pyenv virtualenv 2.7.11 
pyenv virtualenv 3.6.4

pyenv versions
