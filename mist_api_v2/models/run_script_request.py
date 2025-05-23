# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class RunScriptRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, machine=None, params=None, su=None, env=None, job_id=None):  # noqa: E501
        """RunScriptRequest - a model defined in OpenAPI

        :param machine: The machine of this RunScriptRequest.  # noqa: E501
        :type machine: str
        :param params: The params of this RunScriptRequest.  # noqa: E501
        :type params: str
        :param su: The su of this RunScriptRequest.  # noqa: E501
        :type su: str
        :param env: The env of this RunScriptRequest.  # noqa: E501
        :type env: str
        :param job_id: The job_id of this RunScriptRequest.  # noqa: E501
        :type job_id: str
        """
        self.openapi_types = {
            'machine': str,
            'params': str,
            'su': str,
            'env': str,
            'job_id': str
        }

        self.attribute_map = {
            'machine': 'machine',
            'params': 'params',
            'su': 'su',
            'env': 'env',
            'job_id': 'job_id'
        }

        self._machine = machine
        self._params = params
        self._su = su
        self._env = env
        self._job_id = job_id

    @classmethod
    def from_dict(cls, dikt) -> 'RunScriptRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RunScriptRequest of this RunScriptRequest.  # noqa: E501
        :rtype: RunScriptRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def machine(self):
        """Gets the machine of this RunScriptRequest.


        :return: The machine of this RunScriptRequest.
        :rtype: str
        """
        return self._machine

    @machine.setter
    def machine(self, machine):
        """Sets the machine of this RunScriptRequest.


        :param machine: The machine of this RunScriptRequest.
        :type machine: str
        """
        if machine is None:
            raise ValueError("Invalid value for `machine`, must not be `None`")  # noqa: E501

        self._machine = machine

    @property
    def params(self):
        """Gets the params of this RunScriptRequest.


        :return: The params of this RunScriptRequest.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this RunScriptRequest.


        :param params: The params of this RunScriptRequest.
        :type params: str
        """

        self._params = params

    @property
    def su(self):
        """Gets the su of this RunScriptRequest.


        :return: The su of this RunScriptRequest.
        :rtype: str
        """
        return self._su

    @su.setter
    def su(self, su):
        """Sets the su of this RunScriptRequest.


        :param su: The su of this RunScriptRequest.
        :type su: str
        """
        allowed_values = ["true", "false"]  # noqa: E501
        if su not in allowed_values:
            raise ValueError(
                "Invalid value for `su` ({0}), must be one of {1}"
                .format(su, allowed_values)
            )

        self._su = su

    @property
    def env(self):
        """Gets the env of this RunScriptRequest.


        :return: The env of this RunScriptRequest.
        :rtype: str
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this RunScriptRequest.


        :param env: The env of this RunScriptRequest.
        :type env: str
        """

        self._env = env

    @property
    def job_id(self):
        """Gets the job_id of this RunScriptRequest.


        :return: The job_id of this RunScriptRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RunScriptRequest.


        :param job_id: The job_id of this RunScriptRequest.
        :type job_id: str
        """

        self._job_id = job_id
