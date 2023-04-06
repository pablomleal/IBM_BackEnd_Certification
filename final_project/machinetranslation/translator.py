"""This module authenticates and instantiates IBM Watson Machine translation service.
It also contains the functions necessary to translate a given text from EN to FR and viceversa.
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


#Following code excerpted from IBM Watson Docs
#from ibm_watson import LanguageTranslatorV3
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    """This function takes a text in English as input and returns it translated to French"""
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr')
    response_json = translation.get_result()
    french_text = response_json['translations'][0]['translation']
    return french_text

#frenchText = english_to_french('hello')
#print(frenchText)

def french_to_english(french_text):
    """This function takes a text in French as input and returns it translated to English"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en')
    response_json = translation.get_result()
    english_text = response_json['translations'][0]['translation']
    return english_text

