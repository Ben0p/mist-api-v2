# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class LxdCloudFeatures(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, container=False):  # noqa: E501
        """LxdCloudFeatures - a model defined in OpenAPI

        :param container: The container of this LxdCloudFeatures.  # noqa: E501
        :type container: bool
        """
        self.openapi_types = {
            'container': bool
        }

        self.attribute_map = {
            'container': 'container'
        }

        self._container = container

    @classmethod
    def from_dict(cls, dikt) -> 'LxdCloudFeatures':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LxdCloudFeatures of this LxdCloudFeatures.  # noqa: E501
        :rtype: LxdCloudFeatures
        """
        return util.deserialize_model(dikt, cls)

    @property
    def container(self):
        """Gets the container of this LxdCloudFeatures.


        :return: The container of this LxdCloudFeatures.
        :rtype: bool
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this LxdCloudFeatures.


        :param container: The container of this LxdCloudFeatures.
        :type container: bool
        """

        self._container = container
