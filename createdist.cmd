@ECHO OFF
CLS

REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
REM @ First delete the existing distributions
REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
del dist /Q

REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
REM The following URL served as a useful guide on how to
REM     structure a python package for distribution
REM
REM     https://packaging.python.org/tutorials/packaging-projects/
REM
REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
REM @ Upgrading 'PIP' - always a good idea to have latest version
REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
python -m pip install --upgrade pip
ECHO.

REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
REM @ Install 'twine' - used to upload to python PyPi securely
REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
pip install twine
ECHO.

REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
REM @ Make sure we have the latest version of 'setuptools', 'wheel' and 'twine'
REM @ 'setuptools' and 'wheel' are used by twine
REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
python -m pip install --user --upgrade setuptools wheel twine
ECHO.

REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
REM @ To avoid prompts for username/passwords
REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
REM
REM Create a file called '.pypirc' and place it in your user home directory which
REM      is typically c:\users\<username> (On Windows 10)
REM
REM The file should have the following content
REM
REM [distutils]
REM index-servers=
REM 	testpypi
REM  	pypi
REM [testpypi]
REM repository = https://test.pypi.org/legacy/
REM username = StreamlinePartners
REM password = <PasswordHere>
REM
REM [pypi]
REM repository = https://pypi.python.org/pypi
REM username = StreamlinePartners
REM password = <PasswordHere>
REM
REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
REM ***Note: Passwords are in PasswordSafe ***
REM  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
REM @ Create the distribution
REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
REM python setup.py sdist bdist_wheel
python setup.py sdist
ECHO.

REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
REM @ NOTE: If you wanted to test the install of the package locally before
REM @       uploading to PyPi, you can do the following:
REM @
REM @       1) Open a command prompt and set the current directory to 'dist'
REM @          ***This is where packages are created/recreated
REM @
REM @       2) Run a simple web server with python:
REM @             python -m SimpleHTTPServer 9000
REM @
REM @       3) Open another command prompt and run the following:
REM @                pip install --extra-index-url=http://127.0.0.1:9000/ CherwellAPI
REM @
REM @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

ECHO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
ECHO @ Use the following command to check the distribution before uploading
ECHO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
ECHO twine check dist/*
ECHO.

ECHO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
ECHO @ Use the following command to upload to Test PyPi
ECHO Recommended to do this before uploading to production
ECHO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
ECHO twine upload dist/* -r testpypi
ECHO.
ECHO *** You can upload the same version multiple times to
ECHO *** test on testpypi. On production that is not the case,
ECHO *** you can only upload once before having to upload a new version
ECHO *** so get it right on test first
ECHO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

ECHO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
ECHO @ Use the following command to upload to PyPi
ECHO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
ECHO twine upload dist/* -r pypi
ECHO.
