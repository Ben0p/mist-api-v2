# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.script_to_run_all_of import ScriptToRunAllOf
from mist_api_v2 import util

from mist_api_v2.models.script_to_run_all_of import ScriptToRunAllOf  # noqa: E501

class ScriptToRun(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action_type=None, script_type=None, command=None, script=None, params=None):  # noqa: E501
        """ScriptToRun - a model defined in OpenAPI

        :param action_type: The action_type of this ScriptToRun.  # noqa: E501
        :type action_type: str
        :param script_type: The script_type of this ScriptToRun.  # noqa: E501
        :type script_type: str
        :param command: The command of this ScriptToRun.  # noqa: E501
        :type command: str
        :param script: The script of this ScriptToRun.  # noqa: E501
        :type script: str
        :param params: The params of this ScriptToRun.  # noqa: E501
        :type params: str
        """
        self.openapi_types = {
            'action_type': str,
            'script_type': str,
            'command': str,
            'script': str,
            'params': str
        }

        self.attribute_map = {
            'action_type': 'action_type',
            'script_type': 'script_type',
            'command': 'command',
            'script': 'script',
            'params': 'params'
        }

        self._action_type = action_type
        self._script_type = script_type
        self._command = command
        self._script = script
        self._params = params

    @classmethod
    def from_dict(cls, dikt) -> 'ScriptToRun':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScriptToRun of this ScriptToRun.  # noqa: E501
        :rtype: ScriptToRun
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action_type(self):
        """Gets the action_type of this ScriptToRun.


        :return: The action_type of this ScriptToRun.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ScriptToRun.


        :param action_type: The action_type of this ScriptToRun.
        :type action_type: str
        """
        allowed_values = ["run_script"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def script_type(self):
        """Gets the script_type of this ScriptToRun.


        :return: The script_type of this ScriptToRun.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this ScriptToRun.


        :param script_type: The script_type of this ScriptToRun.
        :type script_type: str
        """
        allowed_values = ["existing"]  # noqa: E501
        if script_type not in allowed_values:
            raise ValueError(
                "Invalid value for `script_type` ({0}), must be one of {1}"
                .format(script_type, allowed_values)
            )

        self._script_type = script_type

    @property
    def command(self):
        """Gets the command of this ScriptToRun.

        Command that is about to run  # noqa: E501

        :return: The command of this ScriptToRun.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ScriptToRun.

        Command that is about to run  # noqa: E501

        :param command: The command of this ScriptToRun.
        :type command: str
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def script(self):
        """Gets the script of this ScriptToRun.

        Name or ID of the script to run  # noqa: E501

        :return: The script of this ScriptToRun.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this ScriptToRun.

        Name or ID of the script to run  # noqa: E501

        :param script: The script of this ScriptToRun.
        :type script: str
        """
        if script is None:
            raise ValueError("Invalid value for `script`, must not be `None`")  # noqa: E501

        self._script = script

    @property
    def params(self):
        """Gets the params of this ScriptToRun.


        :return: The params of this ScriptToRun.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ScriptToRun.


        :param params: The params of this ScriptToRun.
        :type params: str
        """

        self._params = params
