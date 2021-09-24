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

class ReviewDetail(object):
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
        'username': 'str',
        'user_url': 'str',
        'review_link': 'str',
        'warning_spoilers': 'bool',
        '_date': 'str',
        'rate': 'str',
        'helpful': 'str',
        'title': 'str',
        'content': 'str'
    }

    attribute_map = {
        'username': 'username',
        'user_url': 'userUrl',
        'review_link': 'reviewLink',
        'warning_spoilers': 'warningSpoilers',
        '_date': 'date',
        'rate': 'rate',
        'helpful': 'helpful',
        'title': 'title',
        'content': 'content'
    }

    def __init__(self, username=None, user_url=None, review_link=None, warning_spoilers=None, _date=None, rate=None, helpful=None, title=None, content=None):  # noqa: E501
        """ReviewDetail - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._user_url = None
        self._review_link = None
        self._warning_spoilers = None
        self.__date = None
        self._rate = None
        self._helpful = None
        self._title = None
        self._content = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if user_url is not None:
            self.user_url = user_url
        if review_link is not None:
            self.review_link = review_link
        if warning_spoilers is not None:
            self.warning_spoilers = warning_spoilers
        if _date is not None:
            self._date = _date
        if rate is not None:
            self.rate = rate
        if helpful is not None:
            self.helpful = helpful
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content

    @property
    def username(self):
        """Gets the username of this ReviewDetail.  # noqa: E501


        :return: The username of this ReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ReviewDetail.


        :param username: The username of this ReviewDetail.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def user_url(self):
        """Gets the user_url of this ReviewDetail.  # noqa: E501


        :return: The user_url of this ReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._user_url

    @user_url.setter
    def user_url(self, user_url):
        """Sets the user_url of this ReviewDetail.


        :param user_url: The user_url of this ReviewDetail.  # noqa: E501
        :type: str
        """

        self._user_url = user_url

    @property
    def review_link(self):
        """Gets the review_link of this ReviewDetail.  # noqa: E501


        :return: The review_link of this ReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._review_link

    @review_link.setter
    def review_link(self, review_link):
        """Sets the review_link of this ReviewDetail.


        :param review_link: The review_link of this ReviewDetail.  # noqa: E501
        :type: str
        """

        self._review_link = review_link

    @property
    def warning_spoilers(self):
        """Gets the warning_spoilers of this ReviewDetail.  # noqa: E501


        :return: The warning_spoilers of this ReviewDetail.  # noqa: E501
        :rtype: bool
        """
        return self._warning_spoilers

    @warning_spoilers.setter
    def warning_spoilers(self, warning_spoilers):
        """Sets the warning_spoilers of this ReviewDetail.


        :param warning_spoilers: The warning_spoilers of this ReviewDetail.  # noqa: E501
        :type: bool
        """

        self._warning_spoilers = warning_spoilers

    @property
    def _date(self):
        """Gets the _date of this ReviewDetail.  # noqa: E501


        :return: The _date of this ReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ReviewDetail.


        :param _date: The _date of this ReviewDetail.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def rate(self):
        """Gets the rate of this ReviewDetail.  # noqa: E501


        :return: The rate of this ReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this ReviewDetail.


        :param rate: The rate of this ReviewDetail.  # noqa: E501
        :type: str
        """

        self._rate = rate

    @property
    def helpful(self):
        """Gets the helpful of this ReviewDetail.  # noqa: E501


        :return: The helpful of this ReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._helpful

    @helpful.setter
    def helpful(self, helpful):
        """Sets the helpful of this ReviewDetail.


        :param helpful: The helpful of this ReviewDetail.  # noqa: E501
        :type: str
        """

        self._helpful = helpful

    @property
    def title(self):
        """Gets the title of this ReviewDetail.  # noqa: E501


        :return: The title of this ReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ReviewDetail.


        :param title: The title of this ReviewDetail.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def content(self):
        """Gets the content of this ReviewDetail.  # noqa: E501


        :return: The content of this ReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ReviewDetail.


        :param content: The content of this ReviewDetail.  # noqa: E501
        :type: str
        """

        self._content = content

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
        if issubclass(ReviewDetail, dict):
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
        if not isinstance(other, ReviewDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other