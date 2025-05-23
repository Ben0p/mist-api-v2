# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.kvm_credentials_hosts import KvmCredentialsHosts
from mist_api_v2 import util

from mist_api_v2.models.kvm_credentials_hosts import KvmCredentialsHosts  # noqa: E501

class KvmCredentials(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, hosts=None):  # noqa: E501
        """KvmCredentials - a model defined in OpenAPI

        :param hosts: The hosts of this KvmCredentials.  # noqa: E501
        :type hosts: List[KvmCredentialsHosts]
        """
        self.openapi_types = {
            'hosts': List[KvmCredentialsHosts]
        }

        self.attribute_map = {
            'hosts': 'hosts'
        }

        self._hosts = hosts

    @classmethod
    def from_dict(cls, dikt) -> 'KvmCredentials':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The KvmCredentials of this KvmCredentials.  # noqa: E501
        :rtype: KvmCredentials
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hosts(self):
        """Gets the hosts of this KvmCredentials.


        :return: The hosts of this KvmCredentials.
        :rtype: List[KvmCredentialsHosts]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this KvmCredentials.


        :param hosts: The hosts of this KvmCredentials.
        :type hosts: List[KvmCredentialsHosts]
        """

        self._hosts = hosts
