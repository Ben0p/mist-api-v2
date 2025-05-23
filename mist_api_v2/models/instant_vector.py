# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.datapoints_values_item import DatapointsValuesItem
from mist_api_v2 import util

from mist_api_v2.models.datapoints_values_item import DatapointsValuesItem  # noqa: E501

class InstantVector(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, metric=None, values=None):  # noqa: E501
        """InstantVector - a model defined in OpenAPI

        :param metric: The metric of this InstantVector.  # noqa: E501
        :type metric: object
        :param values: The values of this InstantVector.  # noqa: E501
        :type values: List[DatapointsValuesItem]
        """
        self.openapi_types = {
            'metric': object,
            'values': List[DatapointsValuesItem]
        }

        self.attribute_map = {
            'metric': 'metric',
            'values': 'values'
        }

        self._metric = metric
        self._values = values

    @classmethod
    def from_dict(cls, dikt) -> 'InstantVector':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InstantVector of this InstantVector.  # noqa: E501
        :rtype: InstantVector
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metric(self):
        """Gets the metric of this InstantVector.


        :return: The metric of this InstantVector.
        :rtype: object
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this InstantVector.


        :param metric: The metric of this InstantVector.
        :type metric: object
        """

        self._metric = metric

    @property
    def values(self):
        """Gets the values of this InstantVector.


        :return: The values of this InstantVector.
        :rtype: List[DatapointsValuesItem]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this InstantVector.


        :param values: The values of this InstantVector.
        :type values: List[DatapointsValuesItem]
        """

        self._values = values
