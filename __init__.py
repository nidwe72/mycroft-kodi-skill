from mycroft import MycroftSkill, intent_file_handler


class MycroftKodi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('kodi.mycroft.intent')
    def handle_kodi_mycroft(self, message):
        self.speak_dialog('kodi.mycroft')


def create_skill():
    return MycroftKodi()

