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
        # API local para desarrollo
        # api_url = "http://127.0.0.1:8005/api/"
        api_url = qsatype.FLUtil.readDBSettingEntry(u"URL_API_PINEBOO")
        if not api_url or api_url == '':
            raise Exception("No hay definida una URL para la API de Pineboo en el formulario de configuración del módulo principal de facturación")
        id_usuario = qsatype.FLUtil.nameUser()
        token = qsatype.FLUtil.sqlSelect("usuarios", "token", "idusuario = '{}'".format(id_usuario))
        if not token or token is None:
            raise Exception("El usuario {} no tiene token creado. Operación cancelada".format(id_usuario))
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
