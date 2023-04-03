'''
    Translating API Watson
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    Translating english to french
    '''
    #englishText = input('Please write the text you want to translate - ')
    if english_text == " " or not(isinstance(english_text,str)):
        return "Please enter text..."

    try:
        translation = language_translator.translate(text=english_text, model_id="en-fr")\
            .get_result()
        english_text = translation['translations'][0]['translation']
    except Exception as e:
        return e

    #print(frenchText)
    return english_text

def french_to_english(french_text):
    '''
    Translating french to english
    '''
    #french_text = input('Écrivez votre texte à traduire ici - ')
    if french_text == " " or not(isinstance(french_text,str)):
        return "Please enter text..."

    try:
        translation = language_translator.translate(text=french_text, model_id="fr-en").get_result()
        french_text = translation['translations'][0]['translation']
    except Exception as e:
        return e

    #print(frenchText)
    return french_text

if __name__ == '__main__':
    #print(english_to_french())
    print(english_to_french(''))
