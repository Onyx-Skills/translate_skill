from os.path import dirname, join

from translate_skill.index import translate
from onyx.skills.core import OnyxSkill
from onyx.util.log import getLogger

__author__ = ''

LOGGER = getLogger(__name__)

class TranslateSkill(OnyxSkill):
    def __init__(self):
        super(TranslateSkill, self).__init__(name="TranslateSkill")

    def get_blueprint(self):
        return translate

    def initialize(self):
        LOGGER.info("Translate Skill initialize")

    def stop(self):
        pass

def create_skill():
    return TranslateSkill()
