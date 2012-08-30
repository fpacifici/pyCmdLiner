#!/usr/bin/env python
#
# Copyright 2012 Filippo Pacifici
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import sys


class Pycmdliner(object):
    '''
    Python Command liner script.

    Provides the boiler plate code for developing command line non
    interactive tools.

    The main idea is that the user provides a small configurationa and
    an object that implements business logic, then this script interprets
    input parameters and invokes the correct  method on the business logic
    object setting correctly input parameters and attributes.

    Created on Aug 27, 2012

    @author: fpacifici
    '''

    def __init__(self, configuration, businessObject):
        '''
        Initializes the Command liner providing the business object,
        if needed it gets the list of input parameters and the configuration
        '''
        super(Pycmdliner, self).__init__()
        if configuration == None or businessObject == None:
            raise Exception('Configuration and Business Object cannot be' +
                ' null to instantiate a PyCmdLiner')

        if type(configuration) != dict:
            raise Exception('COnfiguration must be a dictionary')

        self.configuration = configuration
        self.businessObject = businessObject


    def process(self, inputParams = sys.argv[1:], businessObject = None):
        '''
        Performs the actual processing of the command line tool.

        1) parse input commands elements to check if the size is correct
        2) find the command to be executed
        3) gets the method name for the command to be executed
        4) runs the command.
        '''
        methodToExecute = self.__extractMethod__(inputParams)
        if businessObject == None and self.businessObject == None:
            raise Exception('Business object not provided')
        bObject = self.businessObject
        if businessObject != None:
            bObject = businessObject
        return self.__runMethod__(bObject, methodToExecute)


    def __basicInputValidation__(self, inputParameters):
        '''
        Validate input parameters according to the configuration
        '''
        if len(inputParameters) < 1:
            raise InvalidInputError('Not Enough input parameters')


    def __extractMethod__(self, inputParameters):
        self.__basicInputValidation__(inputParameters)
        command = inputParameters[0]
        if 'commandMapping' not in self.configuration:
            raise Exception('Invalid configuration: commandMapping section not present')
        if command in self.configuration['commandMapping']:
            return self.configuration['commandMapping'][command]
        else:
            raise InvalidInputError('Command %s does not exist' % command)


    def __runMethod__(self, businessObject, methodName):
        method = getattr(businessObject, methodName)
        return method()


class InvalidInputError(Exception):
    """Manages invalid input exceptions"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
