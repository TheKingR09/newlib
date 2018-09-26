# -*- coding: utf-8 -*-
from akad.ttypes import Message
from .auth import Auth
from .models import Models
from .talk import Talk
from .square import Square
from .call import Call
from .timeline import Timeline
from .server import Server
from .shop import Shop

class LINE(Auth, Models, Talk, Square, Call, Timeline, Shop):

    def __init__(self, idOrAuthToken=None, passwd=None, certificate=None, systemName=None, appType=None, appName=None, showQr=False, channelId=None, keepLoggedIn=True):
        Auth.__init__(self, appType)
        if not (idOrAuthToken or idOrAuthToken and passwd):
            self.loginWithQrCode(keepLoggedIn=keepLoggedIn, systemName=systemName, appName=appName, showQr=showQr)
        if idOrAuthToken and passwd:
            self.loginWithCredential(_id=idOrAuthToken, passwd=passwd, certificate=certificate, systemName=systemName, appName=appName, keepLoggedIn=keepLoggedIn)
        elif idOrAuthToken and not passwd:
            self.loginWithAuthToken(authToken=idOrAuthToken, appName=appName)
        self.channelId = channelId
        self.__initAll()

    def __initAll(self):

        self.profile    = self.talk.getProfile()
        self.userTicket = self.generateUserTicket()
        self.groups     = self.talk.getGroupIdsJoined()

        Models.__init__(self)
        Talk.__init__(self)
        Square.__init__(self)
        Call.__init__(self)
        Timeline.__init__(self)
        Shop.__init__(self)
