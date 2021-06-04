from mycroft import MycroftSkill, intent_file_handler
from kodijsonrpc import *
import beepy as beep

class MycroftKodi(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_entity_file('volume.entity')

    @intent_file_handler('kodi.mycroft.volume3.intent')
    def handle_kodi_mycroft_volume3(self, message):

        if volume is not None:
            volumePercents=30;
            server = KodiJSONClient('192.168.1.107', '8080', 'kodi', 'kodi')
            kodiApplication=server.Application
            kodiApplication.SetVolume(volumePercents)
            beep.beep(sound='coin')

    @intent_file_handler('kodi.mycroft.volume.intent')
    def handle_kodi_mycroft(self, message):

        volume = message.data.get('volume')
        if volume is not None:
            volumePercents=int(volume)*10;
            server = KodiJSONClient('192.168.1.107', '8080', 'kodi', 'kodi')
            kodiApplication=server.Application
            kodiApplication.SetVolume(volumePercents)
            beep.beep(sound='coin')

def create_skill():
    return MycroftKodi()

