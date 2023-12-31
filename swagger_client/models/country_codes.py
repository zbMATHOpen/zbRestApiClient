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

class CountryCodes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    INTERNATIONAL_INSTITUTE_FOR_APPLIED_SYSTEMS_ANALYSIS_IIASA_ = "International Institute for Applied Systems Analysis (IIASA)"
    ERITREA = "Eritrea"
    MAYOTTE = "Mayotte"
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = "South Georgia and the South Sandwich Islands"
    FRANCE_METROPOLITAN = "France, Metropolitan"
    ANDORRA = "Andorra"
    NOT_DEFINED = "Not defined"
    UNITED_ARAB_EMIRATES = "United Arab Emirates"
    AFGHANISTAN = "Afghanistan"
    ANTIGUA_AND_BARBADOS = "Antigua and Barbados"
    ALBANIA = "Albania"
    ANGOLA = "Angola"
    ARGENTINA = "Argentina"
    AUSTRIA = "Austria"
    AUSTRALIA = "Australia"
    BARBADOS = "Barbados"
    BANGLADESH = "Bangladesh"
    BELGIUM = "Belgium"
    BURKINA_FASO = "Burkina Faso"
    BULGARIA = "Bulgaria"
    BAHRAIN = "Bahrain"
    BURUNDI = "Burundi"
    BENIN = "Benin"
    BERMUDA = "Bermuda"
    BRUNEI_DARUSSALAM = "Brunei Darussalam"
    BOLIVIA = "Bolivia"
    BRAZIL = "Brazil"
    BAHAMAS = "Bahamas"
    BHUTAN = "Bhutan"
    BURMA = "Burma"
    BOTSWANA = "Botswana"
    BELARUS = "Belarus"
    BELIZE = "Belize"
    CANADA = "Canada"
    CENTRAL_AFRICAN_REPUBLIC = "Central African Republic"
    CONGO = "Congo"
    SWITZERLAND = "Switzerland"
    COTE_D_IVOIRE = "Cote d'Ivoire"
    CHILE = "Chile"
    CAMEROON = "Cameroon"
    CHINA = "China"
    COLOMBIA = "Colombia"
    COSTA_RICA = "Costa Rica"
    CUBA = "Cuba"
    CAPE_VERDE = "Cape Verde"
    CYPRUS = "Cyprus"
    GERMAN_DEMOCRATIC_REPUBLIC = "German Democratic Republic"
    GERMANY = "Germany"
    DJIBOUTI = "Djibouti"
    DENMARK = "Denmark"
    DOMINICA = "Dominica"
    DOMINICAN_REPUBLIC = "Dominican Republic"
    ALGERIA = "Algeria"
    ECUADOR = "Ecuador"
    EGYPT = "Egypt"
    SPAIN = "Spain"
    ETHIOPIA = "Ethiopia"
    FINLAND = "Finland"
    FIJI = "Fiji"
    FRANCE = "France"
    GABON = "Gabon"
    UNITED_KINGDOM = "United Kingdom"
    GRENADA = "Grenada"
    GHANA = "Ghana"
    GAMBIA = "Gambia"
    GUINEA = "Guinea"
    EQUATORIAL_GUINEA = "Equatorial Guinea"
    GREECE = "Greece"
    GUATEMALA = "Guatemala"
    GUINEA_BISSAU = "Guinea-Bissau"
    GUYANA = "Guyana"
    HONG_KONG = "Hong Kong"
    HONDURAS = "Honduras"
    HAITI = "Haiti"
    HUNGARY = "Hungary"
    INDONESIA = "Indonesia"
    IRELAND = "Ireland"
    ISRAEL = "Israel"
    INDIA = "India"
    IRAQ = "Iraq"
    IRAN_ISLAMIC_REPUBLIC_OF_ = "Iran (Islamic Republic of)"
    ICELAND = "Iceland"
    ITALY = "Italy"
    JAMAICA = "Jamaica"
    JORDAN = "Jordan"
    JAPAN = "Japan"
    KENYA = "Kenya"
    CAMBODIA = "Cambodia"
    KIRIBATI = "Kiribati"
    COMOROS = "Comoros"
    KOREA_DEMOCRATIC_PEOPLE_S_REPUBLIC_OF = "Korea, Democratic People's Republic of"
    KOREA_REPUBLIC_OF = "Korea, Republic of"
    KUWAIT = "Kuwait"
    LAO_PEOPLE_S_DEMOCRATIC_REPUBLIC = "Lao People's Democratic Republic"
    LEBANON = "Lebanon"
    SAINTE_LUCIE = "Sainte-Lucie"
    LIECHTENSTEIN = "Liechtenstein"
    SRI_LANKA = "Sri Lanka"
    LIBERIA = "Liberia"
    LESOTHO = "Lesotho"
    LUXEMBOURG = "Luxembourg"
    LIBYAN_ARAB_JAMAHIRIYA = "Libyan Arab Jamahiriya"
    MOROCCO = "Morocco"
    MONACO = "Monaco"
    MADAGASCAR = "Madagascar"
    MALI = "Mali"
    MONGOLIA = "Mongolia"
    MAURITANIA = "Mauritania"
    MALTA = "Malta"
    MAURITIUS = "Mauritius"
    MALDIVES = "Maldives"
    MALAWI = "Malawi"
    MEXICO = "Mexico"
    MALAYSIA = "Malaysia"
    MOZAMBIQUE = "Mozambique"
    NIGER = "Niger"
    NIGERIA = "Nigeria"
    NICARAGUA = "Nicaragua"
    NETHERLANDS = "Netherlands"
    NORWAY = "Norway"
    NEPAL = "Nepal"
    NAURU = "Nauru"
    NEW_ZEALAND = "New Zealand"
    OMAN = "Oman"
    PANAMA = "Panama"
    PERU = "Peru"
    PAPUA_NEW_GUINEA = "Papua New Guinea"
    PHILIPPINES = "Philippines"
    PAKISTAN = "Pakistan"
    POLAND = "Poland"
    PUERTO_RICO = "Puerto Rico"
    PORTUGAL = "Portugal"
    PARAGUAY = "Paraguay"
    QATAR = "Qatar"
    ROMANIA = "Romania"
    RWANDA = "Rwanda"
    SAUDI_ARABIA = "Saudi Arabia"
    SOLOMON_ISLANDS = "Solomon Islands"
    SEYCHELLES = "Seychelles"
    SUDAN = "Sudan"
    SWEDEN = "Sweden"
    SINGAPORE = "Singapore"
    SIERRA_LEONE = "Sierra Leone"
    SAN_MARINO = "San Marino"
    SENEGAL = "Senegal"
    SOMALIA = "Somalia"
    SURINAME = "Suriname"
    SAO_TOME_AND_PRINCIPE = "Sao Tome and Principe"
    USSR = "USSR"
    EL_SALVADOR = "El Salvador"
    SYRIAN_ARAB_REPUBLIC = "Syrian Arab Republic"
    SWAZILAND = "Swaziland"
    CHAD = "Chad"
    TOGO = "Togo"
    THAILAND = "Thailand"
    TUNISIA = "Tunisia"
    TONGA = "Tonga"
    TURKEY = "Turkey"
    TRINIDAD_AND_TOBAGO = "Trinidad and Tobago"
    TUVALU = "Tuvalu"
    TANZANIA_UNITED_REPUBLIC_OF = "Tanzania, United Republic of"
    UKRAINE = "Ukraine"
    UGANDA = "Uganda"
    UNITED_STATES_OF_AMERICA = "United States of America"
    URUGUAY = "Uruguay"
    VATICAN_CITY_STATE = "Vatican City State"
    SAINT_VINCENT_AND_THE_GRENADINES = "Saint Vincent and the Grenadines"
    VENEZUELA = "Venezuela"
    VIET_NAM = "Viet Nam"
    VANUATU = "Vanuatu"
    SAMOA = "Samoa"
    YEMEN_DEMOCRATIC = "Yemen, Democratic"
    YEMEN = "Yemen"
    YUGOSLAVIA = "Yugoslavia"
    SOUTH_AFRICA = "South Africa"
    ZAMBIA = "Zambia"
    ZAIRE = "Zaire"
    ZIMBABWE = "Zimbabwe"
    SERBIA_AND_MONTENEGRO = "Serbia and Montenegro"
    ANGUILLA = "Anguilla"
    NETHERLANDS_ANTILLES = "Netherlands Antilles"
    ANTARCTICA = "Antarctica"
    AMERICAN_SAMOA = "American Samoa"
    ARUBA = "Aruba"
    BOUVET_ISLAND = "Bouvet Island"
    COCOS_KEELING_ISLANDS = "Cocos (Keeling) Islands"
    MYANMAR = "Myanmar"
    COOK_ISLANDS = "Cook Islands"
    CHRISTMAS_ISLAND = "Christmas Island"
    WESTERN_SAHARA = "Western Sahara"
    FALKLAND_ISLANDS_MALVINAS_ = "Falkland Islands (Malvinas)"
    MICRONESIA_FEDERATED_STATES_OF_ = "Micronesia (Federated States of)"
    FAROE_ISLANDS = "Faroe Islands"
    FRENCH_GUIANA = "French Guiana"
    GIBRALTAR = "Gibraltar"
    GREENLAND = "Greenland"
    GUADELOUPE = "Guadeloupe"
    GUAM = "Guam"
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = "Heard Island and McDonald Islands"
    BRITISH_INDIAN_OCEAN_TERRITORY = "British Indian Ocean Territory"
    SAINT_KITTS_AND_NEVIS = "Saint Kitts and Nevis"
    CAYMAN_ISLANDS = "Cayman Islands"
    MARSHALL_ISLANDS = "Marshall Islands"
    MONTSERRAT = "Montserrat"
    NAMIBIA = "Namibia"
    NORFOLK_ISLAND = "Norfolk Island"
    MACAU = "Macau"
    NORTHERN_MARIANA_ISLANDS = "Northern Mariana Islands"
    MARTINIQUE = "Martinique"
    NIUE = "Niue"
    FRENCH_POLYNESIA = "French Polynesia"
    SAINT_PIERRE_AND_MIQUELON = "Saint Pierre and Miquelon"
    PITCAIRN = "Pitcairn"
    PALAU = "Palau"
    REUNION = "Reunion"
    SAINT_HELENA = "Saint Helena"
    SVALBARD_AND_JAN_MAYEN_ISLANDS = "Svalbard and Jan Mayen Islands"
    TURKS_AND_CAICOS_ISLANDS = "Turks and Caicos Islands"
    FRENCH_SOUTHERN_TERRITORIES = "French Southern Territories"
    TOKELAU = "Tokelau"
    EAST_TIMOR = "East Timor"
    TAIWAN_PROVINCE_OF_CHINA = "Taiwan, Province of China"
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = "United States Minor Outlying Islands"
    WALLIS_AND_FUTUNA_ISLANDS = "Wallis and Futuna Islands"
    VIRGIN_ISLANDS_BRITISH_ = "Virgin Islands (British)"
    VIRGIN_ISLANDS_U_S_ = "Virgin Islands (U.S.)"
    LITHUANIA = "Lithuania"
    NEW_CALEDONIA = "New Caledonia"
    INTERNATIONAL_ATOMIC_ENERGY_AGENCY_IAEA_ = "International Atomic Energy Agency (IAEA)"
    EUROPEAN_ORGANIZATION_FOR_NUCLEAR_RESEARCH_CERN_ = "European Organization for Nuclear Research (CERN)"
    OECD_PARIS = "OECD, Paris"
    COMMISSION_OF_THE_EUROPEAN_COMMUNITIES_CEC_ = "Commission of the European Communities (CEC)"
    FOOD_AND_AGRICULTURE_ORGANIZATION_OF_THE_UN_FAO_ = "Food and Agriculture Organization of the UN (FAO)"
    JOINT_INSTITUTE_FOR_NUCLEAR_RESEARCH_JINR_ = "Joint Institute for Nuclear Research (JINR)"
    COUNCIL_FOR_MUTUAL_ECONOMIC_ASSISTANCE_CMEA_ = "Council for Mutual Economic Assistance (CMEA)"
    NUCLEAR_ENERGY_AGENCY_OF_THE_OECD_NEA_ = "Nuclear Energy Agency of the OECD (NEA)"
    INTERNATIONAL_COMMISSION_ON_RADIOLOGICAL_PROTECTION_ICRP_ = "International Commission on Radiological Protection (ICRP)"
    INTERNATIONAL_ORGANIZATION_FOR_STANDARDIZATION_ISO_ = "International Organization for Standardization (ISO)"
    UNITED_NATIONS_UN_ = "United Nations (UN)"
    WORLD_HEALTH_ORGANIZATION_WHO_ = "World Health Organization (WHO)"
    WORLD_ENERGY_CONFERENCE_WEC_ = "World Energy Conference (WEC)"
    INTERNATIONAL_ENERGY_AGENCY_IEA_ = "International Energy Agency (IEA)"
    ARMENIA = "Armenia"
    AZERBAIJAN = "Azerbaijan"
    ESTONIA = "Estonia"
    GEORGIA = "Georgia"
    CROATIA = "Croatia"
    KYRGYZSTAN = "Kyrgyzstan"
    KAZAKHSTAN = "Kazakhstan"
    LATVIA = "Latvia"
    MOLDOVA_REPUBLIC_OF = "Moldova, Republic of"
    NEUTRAL_ZONE = "Neutral Zone"
    RUSSIAN_FEDERATION = "Russian Federation"
    TAJIKISTAN = "Tajikistan"
    TURKMENISTAN = "Turkmenistan"
    UZBEKISTAN = "Uzbekistan"
    SLOVENIA = "Slovenia"
    ARAB_ATOMIC_ENERGY_AGENCY = "Arab Atomic Energy Agency"
    INTERNATIONAL_ORGANISATIONS_WITHOUT_LOCATION = "International Organisations without Location"
    COMPREHENSIVE_NUCLEAR_TEST_BAN_TREATY_ORGANIZATION_CTBTO_ = "Comprehensive Nuclear Test-ban Treaty Organization (CTBTO)"
    UNITED_NATIONS_INDUSTRIAL_DEVELOPMENT_ORGANIZATION_UNIDO_ = "United Nations Industrial Development Organization (UNIDO)"
    CZECH_REPUBLIC = "Czech Republic"
    SLOVAKIA = "Slovakia"
    BOSNIA_AND_HERZEGOVINA = "Bosnia and Herzegovina"
    EURO = "Euro"
    MACEDONIA_THE_FORMER_YUGOSLAV_REPUBLIC_OF = "Macedonia, the former Yugoslav Republic of"
    CONGO_THE_DEMOCRATIC_REPUBLIC_OF = "Congo, the Democratic Republic of"
    OCCUPIED_PALESTINIAN_TERRITORY = "Occupied Palestinian Territory"
    KOSOVO = "Kosovo"
    SERBIA = "Serbia"
    MONTENEGRO = "Montenegro"
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
        """CountryCodes - a model defined in Swagger"""  # noqa: E501
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
        if issubclass(CountryCodes, dict):
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
        if not isinstance(other, CountryCodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
