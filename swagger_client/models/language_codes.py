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

class LanguageCodes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    AFRIKAANS = "Afrikaans"
    ARABIC = "Arabic"
    BULGARIAN = "Bulgarian"
    BYELORUSSIAN = "Byelorussian"
    CHINESE = "Chinese"
    CZECH = "Czech"
    DANISH = "Danish"
    DUTCH = "Dutch"
    ENGLISH = "English"
    FINNISH = "Finnish"
    FRENCH = "French"
    GERMAN = "German"
    HINDI = "Hindi"
    HUNGARIAN = "Hungarian"
    INDONESIAN = "Indonesian"
    ITALIAN = "Italian"
    JAPANESE = "Japanese"
    KOREAN = "Korean"
    LITHUANIAN = "Lithuanian"
    MALAY = "Malay"
    NORWEGIAN = "Norwegian"
    PERSIAN = "Persian"
    POLISH = "Polish"
    PORTUGUESE = "Portuguese"
    ROMANIAN = "Romanian"
    RUSSIAN = "Russian"
    SERBO_CROAT = "Serbo-Croat"
    SLOVAK = "Slovak"
    SPANISH = "Spanish"
    SWEDISH = "Swedish"
    THAI = "Thai"
    TURKISH = "Turkish"
    UKRAINIAN = "Ukrainian"
    WELSH = "Welsh"
    PUNJABI = "Punjabi"
    URDU = "Urdu"
    POLYGLOTT_ = "Polyglott?"
    NOT_DEFINED = "Not defined"
    TAMIL = "Tamil"
    GREEK = "Greek"
    HEBREW = "Hebrew"
    SLOVENIAN = "Slovenian"
    LATIN = "Latin"
    GEORGIAN = "Georgian"
    SERBIAN = "Serbian"
    MOLDAVIAN = "Moldavian"
    LATVIAN = "Latvian"
    ESTONIAN = "Estonian"
    CATALAN = "Catalan"
    AZERBAIJANI = "Azerbaijani"
    ESPERANTO = "Esperanto"
    CROATIAN = "Croatian"
    MACEDONIAN = "Macedonian"
    VIETNAMESE = "Vietnamese"
    FRISIAN = "Frisian"
    SANSKRIT = "Sanskrit"
    BASQUE = "Basque"
    ICELANDIC = "Icelandic"
    AYMARA = "Aymara"
    BASHKIR = "Bashkir"
    BIHARI = "Bihari"
    BISLAMA = "Bislama"
    BENGALI = "Bengali"
    TIBETAN = "Tibetan"
    CORSICAN = "Corsican"
    JAVANESE = "Javanese"
    SAMOAN = "Samoan"
    FAROESE = "Faroese"
    MONGOLIAN = "Mongolian"
    IRISH = "Irish"
    SCOTS_GAELIC = "Scots Gaelic"
    GALICIAN = "Galician"
    BRETON = "Breton"
    AFAR = "Afar"
    ABKHAZIAN = "Abkhazian"
    AMHARIC = "Amharic"
    ASSAMESE = "Assamese"
    ARMENIAN = "Armenian"
    TURKMEN = "Turkmen"
    KAZAKH = "Kazakh"
    UZBEK = "Uzbek"
    INTERLINGUA = "Interlingua"
    ALBANIAN = "Albanian"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """LanguageCodes - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(LanguageCodes, dict):
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
        if not isinstance(other, LanguageCodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
