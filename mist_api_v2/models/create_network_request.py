# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class CreateNetworkRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, cloud=None, tags=None, extra=None, template=None, dry=None, save=None):  # noqa: E501
        """CreateNetworkRequest - a model defined in OpenAPI

        :param name: The name of this CreateNetworkRequest.  # noqa: E501
        :type name: str
        :param cloud: The cloud of this CreateNetworkRequest.  # noqa: E501
        :type cloud: str
        :param tags: The tags of this CreateNetworkRequest.  # noqa: E501
        :type tags: object
        :param extra: The extra of this CreateNetworkRequest.  # noqa: E501
        :type extra: object
        :param template: The template of this CreateNetworkRequest.  # noqa: E501
        :type template: object
        :param dry: The dry of this CreateNetworkRequest.  # noqa: E501
        :type dry: bool
        :param save: The save of this CreateNetworkRequest.  # noqa: E501
        :type save: bool
        """
        self.openapi_types = {
            'name': str,
            'cloud': str,
            'tags': object,
            'extra': object,
            'template': object,
            'dry': bool,
            'save': bool
        }

        self.attribute_map = {
            'name': 'name',
            'cloud': 'cloud',
            'tags': 'tags',
            'extra': 'extra',
            'template': 'template',
            'dry': 'dry',
            'save': 'save'
        }

        self._name = name
        self._cloud = cloud
        self._tags = tags
        self._extra = extra
        self._template = template
        self._dry = dry
        self._save = save

    @classmethod
    def from_dict(cls, dikt) -> 'CreateNetworkRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateNetworkRequest of this CreateNetworkRequest.  # noqa: E501
        :rtype: CreateNetworkRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateNetworkRequest.

        Specify network name  # noqa: E501

        :return: The name of this CreateNetworkRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNetworkRequest.

        Specify network name  # noqa: E501

        :param name: The name of this CreateNetworkRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cloud(self):
        """Gets the cloud of this CreateNetworkRequest.

        Specify cloud to provision on  # noqa: E501

        :return: The cloud of this CreateNetworkRequest.
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this CreateNetworkRequest.

        Specify cloud to provision on  # noqa: E501

        :param cloud: The cloud of this CreateNetworkRequest.
        :type cloud: str
        """
        if cloud is None:
            raise ValueError("Invalid value for `cloud`, must not be `None`")  # noqa: E501

        self._cloud = cloud

    @property
    def tags(self):
        """Gets the tags of this CreateNetworkRequest.

        Assign tags to provisioned network  # noqa: E501

        :return: The tags of this CreateNetworkRequest.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateNetworkRequest.

        Assign tags to provisioned network  # noqa: E501

        :param tags: The tags of this CreateNetworkRequest.
        :type tags: object
        """

        self._tags = tags

    @property
    def extra(self):
        """Gets the extra of this CreateNetworkRequest.

        Configure additional parameters, e.g. cidr (EC2 network)  # noqa: E501

        :return: The extra of this CreateNetworkRequest.
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this CreateNetworkRequest.

        Configure additional parameters, e.g. cidr (EC2 network)  # noqa: E501

        :param extra: The extra of this CreateNetworkRequest.
        :type extra: object
        """

        self._extra = extra

    @property
    def template(self):
        """Gets the template of this CreateNetworkRequest.


        :return: The template of this CreateNetworkRequest.
        :rtype: object
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this CreateNetworkRequest.


        :param template: The template of this CreateNetworkRequest.
        :type template: object
        """

        self._template = template

    @property
    def dry(self):
        """Gets the dry of this CreateNetworkRequest.

        Return provisioning plan and exit without executing it  # noqa: E501

        :return: The dry of this CreateNetworkRequest.
        :rtype: bool
        """
        return self._dry

    @dry.setter
    def dry(self, dry):
        """Sets the dry of this CreateNetworkRequest.

        Return provisioning plan and exit without executing it  # noqa: E501

        :param dry: The dry of this CreateNetworkRequest.
        :type dry: bool
        """

        self._dry = dry

    @property
    def save(self):
        """Gets the save of this CreateNetworkRequest.

        Save provisioning plan as template  # noqa: E501

        :return: The save of this CreateNetworkRequest.
        :rtype: bool
        """
        return self._save

    @save.setter
    def save(self, save):
        """Sets the save of this CreateNetworkRequest.

        Save provisioning plan as template  # noqa: E501

        :param save: The save of this CreateNetworkRequest.
        :type save: bool
        """

        self._save = save
