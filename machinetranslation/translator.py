import json
import pandas
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

from pandas import json_normalize



url = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com'
version_lt = '2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version_lt, authenticator=authenticator)
language_translator.set_service_url(url)



def englishToFrench(englishText):
    """Translates text from English to French"""
    translation_response = language_translator.translate(
        text=englishText, model_id='en-fr')
    translation = translation_response.get_result()
    frenchText = translation['translations'][0]['translation']

    return frenchText


def frenchToEnglish(frenchText):
    """Translates text from French to English"""
    translation_response = language_translator.translate(
        text=frenchText, model_id='fr-en')
    translation = translation_response.get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
