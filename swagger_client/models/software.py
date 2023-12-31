# coding: utf-8

"""
    REST API for zbMATH Open

    a REST api for zbMATH Open, currently with endpoints for authors, classifications, documents, serials and software  # noqa: E501

    OpenAPI spec version: v0.4.3rc0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Software(object):
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
        'articles_count': 'int',
        'authors': 'list[object]',
        'classification': 'list[object]',
        'dependencies': 'str',
        'description': 'str',
        'homepage': 'str',
        'id': 'int',
        'keywords': 'list[object]',
        'license_terms': 'str',
        'name': 'str',
        'operating_systems': 'str',
        'orms_id': 'str',
        'programming_languages': 'str',
        'related_software': 'list[RelatedSoftware]',
        'source_code': 'str',
        'standard_articles': 'list[StandardArticle]',
        'zbmath_url': 'str',
        'data_source': 'object'
    }

    attribute_map = {
        'articles_count': 'articles_count',
        'authors': 'authors',
        'classification': 'classification',
        'dependencies': 'dependencies',
        'description': 'description',
        'homepage': 'homepage',
        'id': 'id',
        'keywords': 'keywords',
        'license_terms': 'license_terms',
        'name': 'name',
        'operating_systems': 'operating_systems',
        'orms_id': 'orms_id',
        'programming_languages': 'programming_languages',
        'related_software': 'related_software',
        'source_code': 'source_code',
        'standard_articles': 'standard_articles',
        'zbmath_url': 'zbmath_url',
        'data_source': 'data_source'
    }

    def __init__(self, articles_count=None, authors=None, classification=None, dependencies=None, description=None, homepage=None, id=None, keywords=None, license_terms=None, name=None, operating_systems=None, orms_id=None, programming_languages=None, related_software=None, source_code=None, standard_articles=None, zbmath_url=None, data_source=None):  # noqa: E501
        """Software - a model defined in Swagger"""  # noqa: E501
        self._articles_count = None
        self._authors = None
        self._classification = None
        self._dependencies = None
        self._description = None
        self._homepage = None
        self._id = None
        self._keywords = None
        self._license_terms = None
        self._name = None
        self._operating_systems = None
        self._orms_id = None
        self._programming_languages = None
        self._related_software = None
        self._source_code = None
        self._standard_articles = None
        self._zbmath_url = None
        self._data_source = None
        self.discriminator = None
        if articles_count is not None:
            self.articles_count = articles_count
        if authors is not None:
            self.authors = authors
        if classification is not None:
            self.classification = classification
        if dependencies is not None:
            self.dependencies = dependencies
        if description is not None:
            self.description = description
        if homepage is not None:
            self.homepage = homepage
        if id is not None:
            self.id = id
        if keywords is not None:
            self.keywords = keywords
        if license_terms is not None:
            self.license_terms = license_terms
        if name is not None:
            self.name = name
        if operating_systems is not None:
            self.operating_systems = operating_systems
        if orms_id is not None:
            self.orms_id = orms_id
        if programming_languages is not None:
            self.programming_languages = programming_languages
        if related_software is not None:
            self.related_software = related_software
        if source_code is not None:
            self.source_code = source_code
        if standard_articles is not None:
            self.standard_articles = standard_articles
        if zbmath_url is not None:
            self.zbmath_url = zbmath_url
        if data_source is not None:
            self.data_source = data_source

    @property
    def articles_count(self):
        """Gets the articles_count of this Software.  # noqa: E501


        :return: The articles_count of this Software.  # noqa: E501
        :rtype: int
        """
        return self._articles_count

    @articles_count.setter
    def articles_count(self, articles_count):
        """Sets the articles_count of this Software.


        :param articles_count: The articles_count of this Software.  # noqa: E501
        :type: int
        """

        self._articles_count = articles_count

    @property
    def authors(self):
        """Gets the authors of this Software.  # noqa: E501


        :return: The authors of this Software.  # noqa: E501
        :rtype: list[object]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this Software.


        :param authors: The authors of this Software.  # noqa: E501
        :type: list[object]
        """

        self._authors = authors

    @property
    def classification(self):
        """Gets the classification of this Software.  # noqa: E501


        :return: The classification of this Software.  # noqa: E501
        :rtype: list[object]
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this Software.


        :param classification: The classification of this Software.  # noqa: E501
        :type: list[object]
        """

        self._classification = classification

    @property
    def dependencies(self):
        """Gets the dependencies of this Software.  # noqa: E501


        :return: The dependencies of this Software.  # noqa: E501
        :rtype: str
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this Software.


        :param dependencies: The dependencies of this Software.  # noqa: E501
        :type: str
        """

        self._dependencies = dependencies

    @property
    def description(self):
        """Gets the description of this Software.  # noqa: E501


        :return: The description of this Software.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Software.


        :param description: The description of this Software.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def homepage(self):
        """Gets the homepage of this Software.  # noqa: E501


        :return: The homepage of this Software.  # noqa: E501
        :rtype: str
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this Software.


        :param homepage: The homepage of this Software.  # noqa: E501
        :type: str
        """

        self._homepage = homepage

    @property
    def id(self):
        """Gets the id of this Software.  # noqa: E501


        :return: The id of this Software.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Software.


        :param id: The id of this Software.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def keywords(self):
        """Gets the keywords of this Software.  # noqa: E501


        :return: The keywords of this Software.  # noqa: E501
        :rtype: list[object]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Software.


        :param keywords: The keywords of this Software.  # noqa: E501
        :type: list[object]
        """

        self._keywords = keywords

    @property
    def license_terms(self):
        """Gets the license_terms of this Software.  # noqa: E501


        :return: The license_terms of this Software.  # noqa: E501
        :rtype: str
        """
        return self._license_terms

    @license_terms.setter
    def license_terms(self, license_terms):
        """Sets the license_terms of this Software.


        :param license_terms: The license_terms of this Software.  # noqa: E501
        :type: str
        """

        self._license_terms = license_terms

    @property
    def name(self):
        """Gets the name of this Software.  # noqa: E501


        :return: The name of this Software.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Software.


        :param name: The name of this Software.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def operating_systems(self):
        """Gets the operating_systems of this Software.  # noqa: E501


        :return: The operating_systems of this Software.  # noqa: E501
        :rtype: str
        """
        return self._operating_systems

    @operating_systems.setter
    def operating_systems(self, operating_systems):
        """Sets the operating_systems of this Software.


        :param operating_systems: The operating_systems of this Software.  # noqa: E501
        :type: str
        """

        self._operating_systems = operating_systems

    @property
    def orms_id(self):
        """Gets the orms_id of this Software.  # noqa: E501


        :return: The orms_id of this Software.  # noqa: E501
        :rtype: str
        """
        return self._orms_id

    @orms_id.setter
    def orms_id(self, orms_id):
        """Sets the orms_id of this Software.


        :param orms_id: The orms_id of this Software.  # noqa: E501
        :type: str
        """

        self._orms_id = orms_id

    @property
    def programming_languages(self):
        """Gets the programming_languages of this Software.  # noqa: E501


        :return: The programming_languages of this Software.  # noqa: E501
        :rtype: str
        """
        return self._programming_languages

    @programming_languages.setter
    def programming_languages(self, programming_languages):
        """Sets the programming_languages of this Software.


        :param programming_languages: The programming_languages of this Software.  # noqa: E501
        :type: str
        """

        self._programming_languages = programming_languages

    @property
    def related_software(self):
        """Gets the related_software of this Software.  # noqa: E501


        :return: The related_software of this Software.  # noqa: E501
        :rtype: list[RelatedSoftware]
        """
        return self._related_software

    @related_software.setter
    def related_software(self, related_software):
        """Sets the related_software of this Software.


        :param related_software: The related_software of this Software.  # noqa: E501
        :type: list[RelatedSoftware]
        """

        self._related_software = related_software

    @property
    def source_code(self):
        """Gets the source_code of this Software.  # noqa: E501


        :return: The source_code of this Software.  # noqa: E501
        :rtype: str
        """
        return self._source_code

    @source_code.setter
    def source_code(self, source_code):
        """Sets the source_code of this Software.


        :param source_code: The source_code of this Software.  # noqa: E501
        :type: str
        """

        self._source_code = source_code

    @property
    def standard_articles(self):
        """Gets the standard_articles of this Software.  # noqa: E501


        :return: The standard_articles of this Software.  # noqa: E501
        :rtype: list[StandardArticle]
        """
        return self._standard_articles

    @standard_articles.setter
    def standard_articles(self, standard_articles):
        """Sets the standard_articles of this Software.


        :param standard_articles: The standard_articles of this Software.  # noqa: E501
        :type: list[StandardArticle]
        """

        self._standard_articles = standard_articles

    @property
    def zbmath_url(self):
        """Gets the zbmath_url of this Software.  # noqa: E501


        :return: The zbmath_url of this Software.  # noqa: E501
        :rtype: str
        """
        return self._zbmath_url

    @zbmath_url.setter
    def zbmath_url(self, zbmath_url):
        """Sets the zbmath_url of this Software.


        :param zbmath_url: The zbmath_url of this Software.  # noqa: E501
        :type: str
        """

        self._zbmath_url = zbmath_url

    @property
    def data_source(self):
        """Gets the data_source of this Software.  # noqa: E501


        :return: The data_source of this Software.  # noqa: E501
        :rtype: object
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this Software.


        :param data_source: The data_source of this Software.  # noqa: E501
        :type: object
        """

        self._data_source = data_source

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
        if issubclass(Software, dict):
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
        if not isinstance(other, Software):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
