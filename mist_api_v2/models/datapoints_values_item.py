# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class DatapointsValuesItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """DatapointsValuesItem - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'DatapointsValuesItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DatapointsValuesItem of this DatapointsValuesItem.  # noqa: E501
        :rtype: DatapointsValuesItem
        """
        return util.deserialize_model(dikt, cls)
