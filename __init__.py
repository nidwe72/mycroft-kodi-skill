from mycroft import MycroftSkill, intent_file_handler
from kodijsonrpc import *

class MycroftKodi(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_entity_file('volume.entity')

    @intent_file_handler('kodi.mycroft.volume.intent')
    def handle_kodi_mycroft(self, message):
        volume = message.data.get('volume')
        if volume is not None:
            server = KodiJSONClient('192.168.1.107', '8080', 'kodi', 'kodi')
            kodiApplication=server.Application
            kodiApplication.SetVolume(100)
            self.speak('die lautstärke von kodi wird auf '+volume+' gesetzt')

def create_skill():
    return MycroftKodi()

