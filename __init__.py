from mycroft import MycroftSkill, intent_file_handler


class MycroftKodi(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_entity_file('volume.entity')

    @intent_file_handler('kodi.mycroft.intent')
    def handle_kodi_mycroft(self, message):
        volume = message.data.get('volume')
        if volume is not None:
            self.speak('ds volumen von kodi wird auf '+volume+' gesetzt')

def create_skill():
    return MycroftKodi()

