#!/opentty.py sh
# Script to compile and upload OpenTTY to PyPi Server

python setup.py sdist bdist_wheel


prompt Press ENTER to continue or Ctrl+C to cancel. . . 

exec twine upload dist/* --verbose
