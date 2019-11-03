from os.path import dirname, join
from adapt.intent import IntentBuilder

from translate_skill.index import translate as blueprint
from onyx.skills.core import OnyxSkill
from onyx.util.log import getLogger

from mtranslate import translate

__author__ = ''

LOGGER = getLogger(__name__)

class TranslateSkill(OnyxSkill):
    def __init__(self):
        super(TranslateSkill, self).__init__(name="TranslateSkill")

    def get_blueprint(self):
        return blueprint

    def initialize(self):
        LOGGER.info("Translate Skill initialize")

        self.load_data_files(dirname(__file__))
        self.load_regex_files(join(dirname(__file__), 'regex', self.lang))


        intent = IntentBuilder('TranslateIntent')\
            .require('TranslateKeyword') \
            .require('LanguageKeyword') \
            .require('phrase') \
            .build()
        self.register_intent(intent, self.handle_translate)

        intent = IntentBuilder('TranslateToIntent')\
            .require('TranslateKeyword') \
            .require('translate') \
            .require('ToKeyword') \
            .require('LanguageKeyword') \
            .build()
        self.register_intent(intent, self.handle_translate_to)

    def handle_translate(self, message):
    	word = message.data.get("TranslateKeyword")
    	lang = message.data.get("LanguageKeyword")
    	sentence = message.data.get("phrase")

    	translated = translate(sentence, lang)

    	self.say(translated,lang)

    def handle_translate_to(self, message):
    	lang = message.data.get("LanguageKeyword")
    	sentence = message.data.get("translate")
    	to = message.data.get("ToKeyword")

    	translated = translate(sentence, lang)

    	self.say(translated,lang)


    def say(self,sentence,lang):
    	print("TRANSLATED PHRASE:",sentence )
    	self.speak(sentence, lang)

    def stop(self):
        pass

def create_skill():
    return TranslateSkill()
