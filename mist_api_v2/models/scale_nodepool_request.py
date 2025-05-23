# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class ScaleNodepoolRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, autoscaling=None, desired_nodes=None, min_nodes=None, max_nodes=None):  # noqa: E501
        """ScaleNodepoolRequest - a model defined in OpenAPI

        :param autoscaling: The autoscaling of this ScaleNodepoolRequest.  # noqa: E501
        :type autoscaling: bool
        :param desired_nodes: The desired_nodes of this ScaleNodepoolRequest.  # noqa: E501
        :type desired_nodes: int
        :param min_nodes: The min_nodes of this ScaleNodepoolRequest.  # noqa: E501
        :type min_nodes: int
        :param max_nodes: The max_nodes of this ScaleNodepoolRequest.  # noqa: E501
        :type max_nodes: int
        """
        self.openapi_types = {
            'autoscaling': bool,
            'desired_nodes': int,
            'min_nodes': int,
            'max_nodes': int
        }

        self.attribute_map = {
            'autoscaling': 'autoscaling',
            'desired_nodes': 'desired_nodes',
            'min_nodes': 'min_nodes',
            'max_nodes': 'max_nodes'
        }

        self._autoscaling = autoscaling
        self._desired_nodes = desired_nodes
        self._min_nodes = min_nodes
        self._max_nodes = max_nodes

    @classmethod
    def from_dict(cls, dikt) -> 'ScaleNodepoolRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScaleNodepoolRequest of this ScaleNodepoolRequest.  # noqa: E501
        :rtype: ScaleNodepoolRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def autoscaling(self):
        """Gets the autoscaling of this ScaleNodepoolRequest.

        Enable/Disable autoscaling for the specified GKE nodepool.  # noqa: E501

        :return: The autoscaling of this ScaleNodepoolRequest.
        :rtype: bool
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this ScaleNodepoolRequest.

        Enable/Disable autoscaling for the specified GKE nodepool.  # noqa: E501

        :param autoscaling: The autoscaling of this ScaleNodepoolRequest.
        :type autoscaling: bool
        """

        self._autoscaling = autoscaling

    @property
    def desired_nodes(self):
        """Gets the desired_nodes of this ScaleNodepoolRequest.

        The number of nodes that the nodepool should maintain  # noqa: E501

        :return: The desired_nodes of this ScaleNodepoolRequest.
        :rtype: int
        """
        return self._desired_nodes

    @desired_nodes.setter
    def desired_nodes(self, desired_nodes):
        """Sets the desired_nodes of this ScaleNodepoolRequest.

        The number of nodes that the nodepool should maintain  # noqa: E501

        :param desired_nodes: The desired_nodes of this ScaleNodepoolRequest.
        :type desired_nodes: int
        """

        self._desired_nodes = desired_nodes

    @property
    def min_nodes(self):
        """Gets the min_nodes of this ScaleNodepoolRequest.

        Minimum number of nodes for the specified nodepool  # noqa: E501

        :return: The min_nodes of this ScaleNodepoolRequest.
        :rtype: int
        """
        return self._min_nodes

    @min_nodes.setter
    def min_nodes(self, min_nodes):
        """Sets the min_nodes of this ScaleNodepoolRequest.

        Minimum number of nodes for the specified nodepool  # noqa: E501

        :param min_nodes: The min_nodes of this ScaleNodepoolRequest.
        :type min_nodes: int
        """

        self._min_nodes = min_nodes

    @property
    def max_nodes(self):
        """Gets the max_nodes of this ScaleNodepoolRequest.

        Maximum number of nodes for the specified nodepool  # noqa: E501

        :return: The max_nodes of this ScaleNodepoolRequest.
        :rtype: int
        """
        return self._max_nodes

    @max_nodes.setter
    def max_nodes(self, max_nodes):
        """Sets the max_nodes of this ScaleNodepoolRequest.

        Maximum number of nodes for the specified nodepool  # noqa: E501

        :param max_nodes: The max_nodes of this ScaleNodepoolRequest.
        :type max_nodes: int
        """

        self._max_nodes = max_nodes
