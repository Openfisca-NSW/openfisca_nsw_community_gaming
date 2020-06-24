# NSW Community Gaming Regulation 2020

Please note that if an organisation is conducting multiple games at the same
time, you must create multiple organisations in the JSON object to send to the API.

If you try to do more than 1 game in an organisation, it will have unpredictable 
consequences.

In the future, if there are rules added that require multiple games to be run at
the same time in an organisation (for example, if there's a yearly limit to the profits
permissable), the code needs to change to remove the dependency on gaming_activity_type.gaming_activity_result. 


## Installing

> We recommend that you use a virtualevn to install OpenFisca. If you don't, 
you may need to add `--user` at the end of all commands starting by `pip`.

```sh
python3 -m venv games
deactive
source games/bin/activate

```
To install your extension, run:

```sh
make install 
```

## Testing

You can make sure that everything is working by running the provided tests:

```sh
make test 
```

To add your extension to the NSW API, update the openfisca-nsw-API repo's makefile with your
extension's name, and add your extension as a dependency.

> [Learn more about tests](http://openfisca.org/doc/coding-the-legislation/writing_yaml_tests.html).

Your extension package is now installed and ready!
