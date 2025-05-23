# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class ResourceSelector(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, ids=None):  # noqa: E501
        """ResourceSelector - a model defined in OpenAPI

        :param type: The type of this ResourceSelector.  # noqa: E501
        :type type: str
        :param ids: The ids of this ResourceSelector.  # noqa: E501
        :type ids: List[str]
        """
        self.openapi_types = {
            'type': str,
            'ids': List[str]
        }

        self.attribute_map = {
            'type': 'type',
            'ids': 'ids'
        }

        self._type = type
        self._ids = ids

    @classmethod
    def from_dict(cls, dikt) -> 'ResourceSelector':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResourceSelector of this ResourceSelector.  # noqa: E501
        :rtype: ResourceSelector
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this ResourceSelector.

        one of \"machines\", \"volumes\", \"clusters\" or \"networks\" resource types  # noqa: E501

        :return: The type of this ResourceSelector.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceSelector.

        one of \"machines\", \"volumes\", \"clusters\" or \"networks\" resource types  # noqa: E501

        :param type: The type of this ResourceSelector.
        :type type: str
        """
        allowed_values = ["machines", "volumes", "clusters", "networks"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def ids(self):
        """Gets the ids of this ResourceSelector.

        a list of UUIDs in case type is resource like \"machines\", \"volumes\", \"clusters\" or \"networks\"  # noqa: E501

        :return: The ids of this ResourceSelector.
        :rtype: List[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this ResourceSelector.

        a list of UUIDs in case type is resource like \"machines\", \"volumes\", \"clusters\" or \"networks\"  # noqa: E501

        :param ids: The ids of this ResourceSelector.
        :type ids: List[str]
        """

        self._ids = ids
