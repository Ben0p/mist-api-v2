# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.key_value_pairs_secret import KeyValuePairsSecret
from mist_api_v2 import util

from mist_api_v2.models.key_value_pairs_secret import KeyValuePairsSecret  # noqa: E501

class KeyValuePairs(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, secret=None):  # noqa: E501
        """KeyValuePairs - a model defined in OpenAPI

        :param secret: The secret of this KeyValuePairs.  # noqa: E501
        :type secret: List[KeyValuePairsSecret]
        """
        self.openapi_types = {
            'secret': List[KeyValuePairsSecret]
        }

        self.attribute_map = {
            'secret': 'secret'
        }

        self._secret = secret

    @classmethod
    def from_dict(cls, dikt) -> 'KeyValuePairs':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The KeyValuePairs of this KeyValuePairs.  # noqa: E501
        :rtype: KeyValuePairs
        """
        return util.deserialize_model(dikt, cls)

    @property
    def secret(self):
        """Gets the secret of this KeyValuePairs.

        Secret data  # noqa: E501

        :return: The secret of this KeyValuePairs.
        :rtype: List[KeyValuePairsSecret]
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this KeyValuePairs.

        Secret data  # noqa: E501

        :param secret: The secret of this KeyValuePairs.
        :type secret: List[KeyValuePairsSecret]
        """

        self._secret = secret
