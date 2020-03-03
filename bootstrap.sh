#!/bin/bash

set -e

if ! test $EXT_NAME || ! test $REPOSITORY_URL
then
	echo 'You need to define and export EXT_NAME and REPOSITORY_URL first  ;)'
	echo 'Open README.md for more information.'
	exit 1
fi

cd $(dirname $0)  # support being called from anywhere on the file system

if [[ -d .git ]]
then
	echo 'It seems you cloned this repository, or already initialised it.'
	echo 'Refusing to go further as you might lose work.'
	echo "If you are certain this is a new repository, run 'cd $(dirname $0) && rm -rf .git' to erase the history."
	exit 2
fi

lowercase_ext_name=$(echo $EXT_NAME | tr '[:upper:]' '[:lower:]')
last_bootstrapping_line_number=$(grep --line-number '^## Writing the Legislation' README.md | cut -d ':' -f 1)

cd ..
pwd
mv openfisca_nsw_extension_template openfisca_$lowercase_ext_name
cd openfisca_$lowercase_ext_name

git init
git add .
git commit --no-gpg-sign --message 'Initial import from OpenFisca ext-template' --author='OpenFisca Bot <bot@openfisca.org>'

all_module_files=`find openfisca_nsw_extension_template -type f`

set -x

# Use intermediate backup files (`-i`) with a weird syntax due to lack of portable 'no backup' option. See https://stackoverflow.com/q/5694228/594053.
sed -i.template "s|ext_template|$lowercase_ext_name|g" README.md setup.py .circleci/config.yml Makefile $all_module_files
sed -i.template "s|Ext-Template|$EXT_NAME|g" README.md setup.py .github/PULL_REQUEST_TEMPLATE.md CONTRIBUTING.md $all_module_files
sed -i.template -e "3,${last_bootstrapping_line_number}d" README.md  # remove instructions lines
sed -i.template "s|ext-template|$lowercase_ext_name|g" README.md
sed -i.template "s|https://github.com/openfisca/openfisca-ext-template|$URL|g" setup.py
find . -name "*.template" -type f -delete

set +x

git mv openfisca_nsw_extension_template openfisca_$lowercase_ext_name

git rm bootstrap.sh
git add .
git commit --no-gpg-sign --message 'Customise ext-template through script' --author='OpenFisca Bot <bot@openfisca.org>'
git remote add origin $REPOSITORY_URL.git

echo '************'
echo '* All set! *'
echo '************'
