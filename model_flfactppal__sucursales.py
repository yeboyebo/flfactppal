# @class_declaration interna_sucursales #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_sucursales(modelos.mtd_sucursales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_sucursales #
class flfactppal_sucursales(interna_sucursales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration sucursales #
class sucursales(flfactppal_sucursales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.sucursales_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
