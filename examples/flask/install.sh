#! /bin/bash
VIRTUAL_ENV=venv

function installPlugins {
  $VIRTUAL_ENV/bin/pip install -r requirements.txt
}

function setupVirtualEnvironment {
  PYTHON=$(which python)
  virtualenv -p ${PYTHON} ${VIRTUAL_ENV}
}

# check for python 3
if [ $(python -c 'import sys; print(sys.version_info[:][0])') == "3" ]
then
  # check for or install virtualenv
  if [ ! $(which virtualenv) ]
  then
    # default to using pip to install virtualenv
    if [ $(which pip) ]
    then
      pip install virtualenv
      setupVirtualEnvironment
    else
      #otherwise download virtualenv directly
      VIRTUALENV_VERSION=1.11.6
      PYTHON=$(which python)
      URL_BASE=http://pypi.python.org/packages/source/v/virtualenv
      echo $URL_BASE/virtualenv-$VIRTUALENV_VERSION.tar.gz
      curl -LO $URL_BASE/virtualenv-$VIRTUALENV_VERSION.tar.gz
      tar xzf virtualenv-$VIRTUALENV_VERSION.tar.gz
      ${PYTHON} virtualenv-$VIRTUALENV_VERSION/virtualenv.py $VIRTUAL_ENV
      rm -rf virtualenv-$VIRTUALENV_VERSION
      rm -rf virtualenv-$VIRTUALENV_VERSION.tar.gz
    fi
  else
    setupVirtualEnvironment
  fi

  # install the plugins we want in our virtaul environment
  installPlugins
else
  # installing python is out of scope for this script
  echo "Please install Python 3 on your system, and make sure \`python\` resolves to it."
  exit 1
fi
