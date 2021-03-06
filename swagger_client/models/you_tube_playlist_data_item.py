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

class YouTubePlaylistDataItem(object):
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
        'video_id': 'str',
        'title': 'str',
        'description': 'str',
        'duration': 'str',
        'upload_date': 'str',
        'image': 'str',
        'url': 'str'
    }

    attribute_map = {
        'video_id': 'videoId',
        'title': 'title',
        'description': 'description',
        'duration': 'duration',
        'upload_date': 'uploadDate',
        'image': 'image',
        'url': 'url'
    }

    def __init__(self, video_id=None, title=None, description=None, duration=None, upload_date=None, image=None, url=None):  # noqa: E501
        """YouTubePlaylistDataItem - a model defined in Swagger"""  # noqa: E501
        self._video_id = None
        self._title = None
        self._description = None
        self._duration = None
        self._upload_date = None
        self._image = None
        self._url = None
        self.discriminator = None
        if video_id is not None:
            self.video_id = video_id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration
        if upload_date is not None:
            self.upload_date = upload_date
        if image is not None:
            self.image = image
        if url is not None:
            self.url = url

    @property
    def video_id(self):
        """Gets the video_id of this YouTubePlaylistDataItem.  # noqa: E501


        :return: The video_id of this YouTubePlaylistDataItem.  # noqa: E501
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this YouTubePlaylistDataItem.


        :param video_id: The video_id of this YouTubePlaylistDataItem.  # noqa: E501
        :type: str
        """

        self._video_id = video_id

    @property
    def title(self):
        """Gets the title of this YouTubePlaylistDataItem.  # noqa: E501


        :return: The title of this YouTubePlaylistDataItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this YouTubePlaylistDataItem.


        :param title: The title of this YouTubePlaylistDataItem.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this YouTubePlaylistDataItem.  # noqa: E501


        :return: The description of this YouTubePlaylistDataItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this YouTubePlaylistDataItem.


        :param description: The description of this YouTubePlaylistDataItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def duration(self):
        """Gets the duration of this YouTubePlaylistDataItem.  # noqa: E501


        :return: The duration of this YouTubePlaylistDataItem.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this YouTubePlaylistDataItem.


        :param duration: The duration of this YouTubePlaylistDataItem.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def upload_date(self):
        """Gets the upload_date of this YouTubePlaylistDataItem.  # noqa: E501


        :return: The upload_date of this YouTubePlaylistDataItem.  # noqa: E501
        :rtype: str
        """
        return self._upload_date

    @upload_date.setter
    def upload_date(self, upload_date):
        """Sets the upload_date of this YouTubePlaylistDataItem.


        :param upload_date: The upload_date of this YouTubePlaylistDataItem.  # noqa: E501
        :type: str
        """

        self._upload_date = upload_date

    @property
    def image(self):
        """Gets the image of this YouTubePlaylistDataItem.  # noqa: E501


        :return: The image of this YouTubePlaylistDataItem.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this YouTubePlaylistDataItem.


        :param image: The image of this YouTubePlaylistDataItem.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def url(self):
        """Gets the url of this YouTubePlaylistDataItem.  # noqa: E501


        :return: The url of this YouTubePlaylistDataItem.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this YouTubePlaylistDataItem.


        :param url: The url of this YouTubePlaylistDataItem.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(YouTubePlaylistDataItem, dict):
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
        if not isinstance(other, YouTubePlaylistDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
