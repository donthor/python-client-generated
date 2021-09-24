# coding: utf-8

"""
    IMDb-API

    The IMDb-API Documentation. You need a <a href='/Identity/Account/Manage' target='_blank'><code>API Key</code></a> for testing APIs.<br/><a class='link' href='/API'>Back to API Tester</a>  # noqa: E501

    OpenAPI spec version: 1.5
    Contact: support@imdb-api.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WikipediaDataPlot(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'plain_text': 'str',
        'html': 'str'
    }

    attribute_map = {
        'plain_text': 'plainText',
        'html': 'html'
    }

    def __init__(self, plain_text=None, html=None):  # noqa: E501
        """WikipediaDataPlot - a model defined in Swagger"""  # noqa: E501
        self._plain_text = None
        self._html = None
        self.discriminator = None
        if plain_text is not None:
            self.plain_text = plain_text
        if html is not None:
            self.html = html

    @property
    def plain_text(self):
        """Gets the plain_text of this WikipediaDataPlot.  # noqa: E501


        :return: The plain_text of this WikipediaDataPlot.  # noqa: E501
        :rtype: str
        """
        return self._plain_text

    @plain_text.setter
    def plain_text(self, plain_text):
        """Sets the plain_text of this WikipediaDataPlot.


        :param plain_text: The plain_text of this WikipediaDataPlot.  # noqa: E501
        :type: str
        """

        self._plain_text = plain_text

    @property
    def html(self):
        """Gets the html of this WikipediaDataPlot.  # noqa: E501


        :return: The html of this WikipediaDataPlot.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this WikipediaDataPlot.


        :param html: The html of this WikipediaDataPlot.  # noqa: E501
        :type: str
        """

        self._html = html

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WikipediaDataPlot, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WikipediaDataPlot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
