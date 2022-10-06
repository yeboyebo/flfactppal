# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration flfactppal #
from YBLEGACY.constantes import *
import requests


class flfactppal(interna):

    def __init__(self, context=None):
        super().__init__(context)

    def llamaAPI(self, url, verbo, params=None):
        res = {}
        api_url = "http://127.0.0.1:8005/api/"
        # api_url = "http://172.65.0.1:8005/api/"
        token = 'd12e36e5b04b5c060451722c460c47a1178fd61e'
        header = {"Content-Type": "application/json", "Authorization": "Token {}".format(token)}
        if verbo == "post":
            res = requests.post(api_url + url, headers=header, data=params)
        elif verbo == "get":
            # Esta sin probar de momento. Fecha 06-10-2022
            res = requests.get(api_url + url, headers=header, params=params)

        return res


# @class_declaration head #
class head(flfactppal):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)


form = FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
iface = form.iface
