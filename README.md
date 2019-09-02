# pytrav

[![codecov](https://codecov.io/gh/Madoshakalaka/pytrav/branch/master/graph/badge.svg)](https://codecov.io/gh/Madoshakalaka/pytrav)
[![Build Status](https://travis-ci.org/Madoshakalaka/pytrav.svg)](https://travis-ci.org/Madoshakalaka/pytrav)

![beautiful-picture](./very-beautiful.PNG)

Use travis to the most.

- 3 operating systems
- python 3.5 3.6 3.7
- tox
- pytest
- codecov
- automatic pypi release

### This is so cool! Want!
essential to-dos:
- if you are very cool
    - figure it out yourself
    
- if not that cool
    - copy three files: `tox.ini` `setup.py` `.travis.yml`
    - changes to make:
        - in `tox.ini` --cov=<your_package_folder_name>
        - in `setup.py` change description; find and replace all `pytrav` to your package name
    - push code to github
    - go to travis ci and add repo
    - go to codecov and add repo
    - copy codecov environment variable and set it on travis ci
    - change pypi `user` key to your pypi username in `.travis.yml`
    - `$ travis encrypt <your-pypi-password>` copy the result and overwrite the `secure` key in `.travis.yml`
    - figure out a bunch of other problems yourself