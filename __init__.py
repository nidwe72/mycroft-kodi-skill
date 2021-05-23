from mycroft import MycroftSkill, intent_file_handler


class MycroftKodi(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_entity_file('volume.entity')

    @intent_file_handler('kodi.mycroft.intent')
    def handle_kodi_mycroft(self, message):
        self.speak_dialog('kodi.mycroft')

    def converse(self, utterances, lang):
            if utterances and self.voc_match(utterances[0], 'pegel vier'):
                self.speak_dialog('vier')
                return True
            elif utterances and self.voc_match(utterances[0], 'pegel drei'):
                self.speak_dialog('drei')
                return True

            else:
                return False

def create_skill():
    return MycroftKodi()

