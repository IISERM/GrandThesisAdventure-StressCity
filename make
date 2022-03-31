#! /bin/sh

python3 -m venv env

. env/bin/activate

pip install numpy pillow pysimplegui pyinstaller

pip install -e ../turing-hunt-engine

pyinstaller main.spec

lddver=$(ldd --version | head -1 | cut -f4 -d' ' | tr '.' '-')

mv ./dist/main ./dist/main-$lddver

