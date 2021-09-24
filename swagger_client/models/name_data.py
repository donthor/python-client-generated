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

class NameData(object):
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
        'id': 'str',
        'name': 'str',
        'role': 'str',
        'image': 'str',
        'summary': 'str',
        'birth_date': 'str',
        'death_date': 'str',
        'awards': 'str',
        'height': 'str',
        'known_for': 'list[KnownFor]',
        'cast_movies': 'list[CastMovie]',
        'error_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'image': 'image',
        'summary': 'summary',
        'birth_date': 'birthDate',
        'death_date': 'deathDate',
        'awards': 'awards',
        'height': 'height',
        'known_for': 'knownFor',
        'cast_movies': 'castMovies',
        'error_message': 'errorMessage'
    }

    def __init__(self, id=None, name=None, role=None, image=None, summary=None, birth_date=None, death_date=None, awards=None, height=None, known_for=None, cast_movies=None, error_message=None):  # noqa: E501
        """NameData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._role = None
        self._image = None
        self._summary = None
        self._birth_date = None
        self._death_date = None
        self._awards = None
        self._height = None
        self._known_for = None
        self._cast_movies = None
        self._error_message = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if image is not None:
            self.image = image
        if summary is not None:
            self.summary = summary
        if birth_date is not None:
            self.birth_date = birth_date
        if death_date is not None:
            self.death_date = death_date
        if awards is not None:
            self.awards = awards
        if height is not None:
            self.height = height
        if known_for is not None:
            self.known_for = known_for
        if cast_movies is not None:
            self.cast_movies = cast_movies
        if error_message is not None:
            self.error_message = error_message

    @property
    def id(self):
        """Gets the id of this NameData.  # noqa: E501


        :return: The id of this NameData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NameData.


        :param id: The id of this NameData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NameData.  # noqa: E501


        :return: The name of this NameData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NameData.


        :param name: The name of this NameData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def role(self):
        """Gets the role of this NameData.  # noqa: E501


        :return: The role of this NameData.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this NameData.


        :param role: The role of this NameData.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def image(self):
        """Gets the image of this NameData.  # noqa: E501


        :return: The image of this NameData.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this NameData.


        :param image: The image of this NameData.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def summary(self):
        """Gets the summary of this NameData.  # noqa: E501


        :return: The summary of this NameData.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this NameData.


        :param summary: The summary of this NameData.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def birth_date(self):
        """Gets the birth_date of this NameData.  # noqa: E501


        :return: The birth_date of this NameData.  # noqa: E501
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this NameData.


        :param birth_date: The birth_date of this NameData.  # noqa: E501
        :type: str
        """

        self._birth_date = birth_date

    @property
    def death_date(self):
        """Gets the death_date of this NameData.  # noqa: E501


        :return: The death_date of this NameData.  # noqa: E501
        :rtype: str
        """
        return self._death_date

    @death_date.setter
    def death_date(self, death_date):
        """Sets the death_date of this NameData.


        :param death_date: The death_date of this NameData.  # noqa: E501
        :type: str
        """

        self._death_date = death_date

    @property
    def awards(self):
        """Gets the awards of this NameData.  # noqa: E501


        :return: The awards of this NameData.  # noqa: E501
        :rtype: str
        """
        return self._awards

    @awards.setter
    def awards(self, awards):
        """Sets the awards of this NameData.


        :param awards: The awards of this NameData.  # noqa: E501
        :type: str
        """

        self._awards = awards

    @property
    def height(self):
        """Gets the height of this NameData.  # noqa: E501


        :return: The height of this NameData.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this NameData.


        :param height: The height of this NameData.  # noqa: E501
        :type: str
        """

        self._height = height

    @property
    def known_for(self):
        """Gets the known_for of this NameData.  # noqa: E501


        :return: The known_for of this NameData.  # noqa: E501
        :rtype: list[KnownFor]
        """
        return self._known_for

    @known_for.setter
    def known_for(self, known_for):
        """Sets the known_for of this NameData.


        :param known_for: The known_for of this NameData.  # noqa: E501
        :type: list[KnownFor]
        """

        self._known_for = known_for

    @property
    def cast_movies(self):
        """Gets the cast_movies of this NameData.  # noqa: E501


        :return: The cast_movies of this NameData.  # noqa: E501
        :rtype: list[CastMovie]
        """
        return self._cast_movies

    @cast_movies.setter
    def cast_movies(self, cast_movies):
        """Sets the cast_movies of this NameData.


        :param cast_movies: The cast_movies of this NameData.  # noqa: E501
        :type: list[CastMovie]
        """

        self._cast_movies = cast_movies

    @property
    def error_message(self):
        """Gets the error_message of this NameData.  # noqa: E501


        :return: The error_message of this NameData.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this NameData.


        :param error_message: The error_message of this NameData.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(NameData, dict):
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
        if not isinstance(other, NameData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
