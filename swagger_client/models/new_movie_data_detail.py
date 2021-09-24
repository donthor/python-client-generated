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

class NewMovieDataDetail(object):
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
        'title': 'str',
        'full_title': 'str',
        'year': 'str',
        'release_state': 'str',
        'image': 'str',
        'runtime_mins': 'str',
        'runtime_str': 'str',
        'plot': 'str',
        'content_rating': 'str',
        'im_db_rating': 'str',
        'im_db_rating_count': 'str',
        'metacritic_rating': 'str',
        'genres': 'str',
        'genre_list': 'list[KeyValueItem]',
        'directors': 'str',
        'director_list': 'list[StarShort]',
        'stars': 'str',
        'star_list': 'list[StarShort]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'full_title': 'fullTitle',
        'year': 'year',
        'release_state': 'releaseState',
        'image': 'image',
        'runtime_mins': 'runtimeMins',
        'runtime_str': 'runtimeStr',
        'plot': 'plot',
        'content_rating': 'contentRating',
        'im_db_rating': 'imDbRating',
        'im_db_rating_count': 'imDbRatingCount',
        'metacritic_rating': 'metacriticRating',
        'genres': 'genres',
        'genre_list': 'genreList',
        'directors': 'directors',
        'director_list': 'directorList',
        'stars': 'stars',
        'star_list': 'starList'
    }

    def __init__(self, id=None, title=None, full_title=None, year=None, release_state=None, image=None, runtime_mins=None, runtime_str=None, plot=None, content_rating=None, im_db_rating=None, im_db_rating_count=None, metacritic_rating=None, genres=None, genre_list=None, directors=None, director_list=None, stars=None, star_list=None):  # noqa: E501
        """NewMovieDataDetail - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._full_title = None
        self._year = None
        self._release_state = None
        self._image = None
        self._runtime_mins = None
        self._runtime_str = None
        self._plot = None
        self._content_rating = None
        self._im_db_rating = None
        self._im_db_rating_count = None
        self._metacritic_rating = None
        self._genres = None
        self._genre_list = None
        self._directors = None
        self._director_list = None
        self._stars = None
        self._star_list = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if full_title is not None:
            self.full_title = full_title
        if year is not None:
            self.year = year
        if release_state is not None:
            self.release_state = release_state
        if image is not None:
            self.image = image
        if runtime_mins is not None:
            self.runtime_mins = runtime_mins
        if runtime_str is not None:
            self.runtime_str = runtime_str
        if plot is not None:
            self.plot = plot
        if content_rating is not None:
            self.content_rating = content_rating
        if im_db_rating is not None:
            self.im_db_rating = im_db_rating
        if im_db_rating_count is not None:
            self.im_db_rating_count = im_db_rating_count
        if metacritic_rating is not None:
            self.metacritic_rating = metacritic_rating
        if genres is not None:
            self.genres = genres
        if genre_list is not None:
            self.genre_list = genre_list
        if directors is not None:
            self.directors = directors
        if director_list is not None:
            self.director_list = director_list
        if stars is not None:
            self.stars = stars
        if star_list is not None:
            self.star_list = star_list

    @property
    def id(self):
        """Gets the id of this NewMovieDataDetail.  # noqa: E501


        :return: The id of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewMovieDataDetail.


        :param id: The id of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this NewMovieDataDetail.  # noqa: E501


        :return: The title of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NewMovieDataDetail.


        :param title: The title of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def full_title(self):
        """Gets the full_title of this NewMovieDataDetail.  # noqa: E501


        :return: The full_title of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._full_title

    @full_title.setter
    def full_title(self, full_title):
        """Sets the full_title of this NewMovieDataDetail.


        :param full_title: The full_title of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._full_title = full_title

    @property
    def year(self):
        """Gets the year of this NewMovieDataDetail.  # noqa: E501


        :return: The year of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this NewMovieDataDetail.


        :param year: The year of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def release_state(self):
        """Gets the release_state of this NewMovieDataDetail.  # noqa: E501


        :return: The release_state of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._release_state

    @release_state.setter
    def release_state(self, release_state):
        """Sets the release_state of this NewMovieDataDetail.


        :param release_state: The release_state of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._release_state = release_state

    @property
    def image(self):
        """Gets the image of this NewMovieDataDetail.  # noqa: E501


        :return: The image of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this NewMovieDataDetail.


        :param image: The image of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def runtime_mins(self):
        """Gets the runtime_mins of this NewMovieDataDetail.  # noqa: E501


        :return: The runtime_mins of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._runtime_mins

    @runtime_mins.setter
    def runtime_mins(self, runtime_mins):
        """Sets the runtime_mins of this NewMovieDataDetail.


        :param runtime_mins: The runtime_mins of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._runtime_mins = runtime_mins

    @property
    def runtime_str(self):
        """Gets the runtime_str of this NewMovieDataDetail.  # noqa: E501


        :return: The runtime_str of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._runtime_str

    @runtime_str.setter
    def runtime_str(self, runtime_str):
        """Sets the runtime_str of this NewMovieDataDetail.


        :param runtime_str: The runtime_str of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._runtime_str = runtime_str

    @property
    def plot(self):
        """Gets the plot of this NewMovieDataDetail.  # noqa: E501


        :return: The plot of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._plot

    @plot.setter
    def plot(self, plot):
        """Sets the plot of this NewMovieDataDetail.


        :param plot: The plot of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._plot = plot

    @property
    def content_rating(self):
        """Gets the content_rating of this NewMovieDataDetail.  # noqa: E501


        :return: The content_rating of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._content_rating

    @content_rating.setter
    def content_rating(self, content_rating):
        """Sets the content_rating of this NewMovieDataDetail.


        :param content_rating: The content_rating of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._content_rating = content_rating

    @property
    def im_db_rating(self):
        """Gets the im_db_rating of this NewMovieDataDetail.  # noqa: E501


        :return: The im_db_rating of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._im_db_rating

    @im_db_rating.setter
    def im_db_rating(self, im_db_rating):
        """Sets the im_db_rating of this NewMovieDataDetail.


        :param im_db_rating: The im_db_rating of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._im_db_rating = im_db_rating

    @property
    def im_db_rating_count(self):
        """Gets the im_db_rating_count of this NewMovieDataDetail.  # noqa: E501


        :return: The im_db_rating_count of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._im_db_rating_count

    @im_db_rating_count.setter
    def im_db_rating_count(self, im_db_rating_count):
        """Sets the im_db_rating_count of this NewMovieDataDetail.


        :param im_db_rating_count: The im_db_rating_count of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._im_db_rating_count = im_db_rating_count

    @property
    def metacritic_rating(self):
        """Gets the metacritic_rating of this NewMovieDataDetail.  # noqa: E501


        :return: The metacritic_rating of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._metacritic_rating

    @metacritic_rating.setter
    def metacritic_rating(self, metacritic_rating):
        """Sets the metacritic_rating of this NewMovieDataDetail.


        :param metacritic_rating: The metacritic_rating of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._metacritic_rating = metacritic_rating

    @property
    def genres(self):
        """Gets the genres of this NewMovieDataDetail.  # noqa: E501


        :return: The genres of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._genres

    @genres.setter
    def genres(self, genres):
        """Sets the genres of this NewMovieDataDetail.


        :param genres: The genres of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._genres = genres

    @property
    def genre_list(self):
        """Gets the genre_list of this NewMovieDataDetail.  # noqa: E501


        :return: The genre_list of this NewMovieDataDetail.  # noqa: E501
        :rtype: list[KeyValueItem]
        """
        return self._genre_list

    @genre_list.setter
    def genre_list(self, genre_list):
        """Sets the genre_list of this NewMovieDataDetail.


        :param genre_list: The genre_list of this NewMovieDataDetail.  # noqa: E501
        :type: list[KeyValueItem]
        """

        self._genre_list = genre_list

    @property
    def directors(self):
        """Gets the directors of this NewMovieDataDetail.  # noqa: E501


        :return: The directors of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._directors

    @directors.setter
    def directors(self, directors):
        """Sets the directors of this NewMovieDataDetail.


        :param directors: The directors of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._directors = directors

    @property
    def director_list(self):
        """Gets the director_list of this NewMovieDataDetail.  # noqa: E501


        :return: The director_list of this NewMovieDataDetail.  # noqa: E501
        :rtype: list[StarShort]
        """
        return self._director_list

    @director_list.setter
    def director_list(self, director_list):
        """Sets the director_list of this NewMovieDataDetail.


        :param director_list: The director_list of this NewMovieDataDetail.  # noqa: E501
        :type: list[StarShort]
        """

        self._director_list = director_list

    @property
    def stars(self):
        """Gets the stars of this NewMovieDataDetail.  # noqa: E501


        :return: The stars of this NewMovieDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this NewMovieDataDetail.


        :param stars: The stars of this NewMovieDataDetail.  # noqa: E501
        :type: str
        """

        self._stars = stars

    @property
    def star_list(self):
        """Gets the star_list of this NewMovieDataDetail.  # noqa: E501


        :return: The star_list of this NewMovieDataDetail.  # noqa: E501
        :rtype: list[StarShort]
        """
        return self._star_list

    @star_list.setter
    def star_list(self, star_list):
        """Sets the star_list of this NewMovieDataDetail.


        :param star_list: The star_list of this NewMovieDataDetail.  # noqa: E501
        :type: list[StarShort]
        """

        self._star_list = star_list

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
        if issubclass(NewMovieDataDetail, dict):
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
        if not isinstance(other, NewMovieDataDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
