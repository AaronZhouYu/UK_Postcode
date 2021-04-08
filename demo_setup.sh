#!/bin/bash

set -x

sudo yum update -y
sudo yum install python3 -y
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
pip install inquirer
pip install requests

echo "Test_1:"
python3 ./postcode.py

echo "Test_2:"
python3 ./postcode.py ""

echo "Test_3:"
python3 ./postcode.py "a"

echo "Test_4:"
python3 ./postcode.py "ab"

echo "Test_5:"
python3 ./postcode.py "abc"

echo "Test_6:"
python3 ./postcode.py "abcd"

echo "Test_7:"
python3 ./postcode.py "abcdef"

echo "Test_8:"
python3 ./postcode.py "abcdefghijk"

echo "Test_9:"
python3 ./postcode.py AB10 1AL

echo "Test_10:"
python3 ./postcode.py "AB10 1AL"

echo "Test_11:"
python3 ./postcode.py AB101AL

echo "Test_12:"
python3 ./postcode.py "1"

echo "Test_13:"
python3 ./postcode.py "23"

echo "Test_14:"
python3 ./postcode.py "234"

echo "Test_15:"
python3 ./postcode.py "423678"

echo "Test_16:"
python3 ./postcode.py "3245234098723"