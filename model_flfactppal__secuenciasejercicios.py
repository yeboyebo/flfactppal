# @class_declaration interna_secuenciasejercicios #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_secuenciasejercicios(modelos.mtd_secuenciasejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_secuenciasejercicios #
class flfactppal_secuenciasejercicios(interna_secuenciasejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration secuenciasejercicios #
class secuenciasejercicios(flfactppal_secuenciasejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.secuenciasejercicios_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
