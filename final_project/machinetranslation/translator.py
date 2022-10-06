""" Translator module using the IBM Watson Language Translator"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey= os.environ['apikey']
url= os.environ['url']

authenticator_priya = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-10-06',
    authenticator=authenticator_priya,
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """This function is used to convert Englih Text to French Text
    using the IBM Language Translator service"""
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    #print(translation)
    french_text = translation["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    """This function is used to convert French Text to English Text
    using the IBM Language Translator service"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    #print(translation)
    english_text = translation["translations"][0]["translation"]
    return english_text
