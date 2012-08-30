pycmdliner
==========

A scaffolding for developing python command line non interactive tools.

This package may be useful when developing command line tools in that it provides the logic that parses
and validates input commands and options and then invokes the user provided application logic.

The user of this module provides:
* an object implementing the application logic of the tool
* some basic configuration

then pycmdliner takes care of the rest

Usage
-----

First element when using this module is installing it. A packaged distribution is present on 
[http://pypi.python.org/pypi/pycmdliner]. Just download it and install through easy_install:

    easy_install -U pycmdliner-0.1.0-py2.7.egg

Second step is importing it in your python script:

    from pycmdliner import Pycmdliner

Third step is preparing the configuration. 
Configuration is provided as a dictionary to the module. This is an example:

    config = {'commandMapping':
    		{'command1': 'method1', 
    	 	'command2': 'method2'},
    	      'appHeader': 'My useless command line tool version 0.0.0.0.1',
              'usageString': "Read the manual!!"}

