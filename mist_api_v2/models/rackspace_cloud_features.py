# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class RackspaceCloudFeatures(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, compute=True):  # noqa: E501
        """RackspaceCloudFeatures - a model defined in OpenAPI

        :param compute: The compute of this RackspaceCloudFeatures.  # noqa: E501
        :type compute: bool
        """
        self.openapi_types = {
            'compute': bool
        }

        self.attribute_map = {
            'compute': 'compute'
        }

        self._compute = compute

    @classmethod
    def from_dict(cls, dikt) -> 'RackspaceCloudFeatures':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RackspaceCloudFeatures of this RackspaceCloudFeatures.  # noqa: E501
        :rtype: RackspaceCloudFeatures
        """
        return util.deserialize_model(dikt, cls)

    @property
    def compute(self):
        """Gets the compute of this RackspaceCloudFeatures.


        :return: The compute of this RackspaceCloudFeatures.
        :rtype: bool
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """Sets the compute of this RackspaceCloudFeatures.


        :param compute: The compute of this RackspaceCloudFeatures.
        :type compute: bool
        """

        self._compute = compute
