from mycroft import MycroftSkill, intent_file_handler
from kodijsonrpc import *
import beepy as beep
#https://github.com/quentinsf/qhue
from qhue import Bridge

class MycroftKodi(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_entity_file('volume.entity')

#    @intent_file_handler('kodi.mycroft.volume3.intent')
#    def handle_kodi_mycroft_volume3(self, message):

#        volumePercents=30
#        server = KodiJSONClient('192.168.1.107', '8080', 'kodi', 'kodi')
#        kodiApplication=server.Application
#        kodiApplication.SetVolume(volumePercents)
#        beep.beep(sound='coin')

#    @intent_file_handler('kodi.mycroft.volume8.intent')
#    def handle_kodi_mycroft_volume3(self, message):

#        volumePercents=80
#        server = KodiJSONClient('192.168.1.107', '8080', 'kodi', 'kodi')
#        kodiApplication=server.Application
#        kodiApplication.SetVolume(volumePercents)
#        beep.beep(sound='coin')



    @intent_file_handler('kodi.mycroft.volume.intent')
    def handle_kodi_mycroft(self, message):

        volume = message.data.get('volume')
        if volume is not None:
            beep.beep(sound='coin')
            volumePercents=int(volume)*10;
            server = KodiJSONClient('192.168.1.107', '8080', 'kodi', 'kodi')
            kodiApplication=server.Application
            kodiApplication.SetVolume(volumePercents)


    @intent_file_handler('kodi.mycroft.turnOnLights.intent')
    def handle_kodi_mycroft(self, message):
        beep.beep(sound='coin')
        b = Bridge("192.168.1.101", 'DexVLlzvvv5jIYCVmBNKlX4GNdP3nPsXyzm-kTRM')

        b.lights[1].state(on=True)
        b.lights[1].state(bri=216, hue=7613,sat=203)

        b.lights[2].state(on=True)
        b.lights[2].state(bri=216, hue=7613,sat=203)

        b.lights[6].state(on=True)
        b.lights[6].state(bri=130, hue=7613,sat=203)

        b.lights[7].state(on=True)
        b.lights[7].state(bri=28, hue=7613,sat=203)

    @intent_file_handler('kodi.mycroft.turnOffLights.intent')
    def handle_kodi_mycroft(self, message):
        beep.beep(sound='coin')
        b = Bridge("192.168.1.101", 'DexVLlzvvv5jIYCVmBNKlX4GNdP3nPsXyzm-kTRM')

        b.lights[1].state(on=False)
        b.lights[2].state(on=False)
        b.lights[6].state(on=False)
        b.lights[7].state(on=False)


        


def create_skill():
    return MycroftKodi()

