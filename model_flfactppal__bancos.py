# @class_declaration interna_bancos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_bancos(modelos.mtd_bancos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_bancos #
class flfactppal_bancos(interna_bancos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration bancos #
class bancos(flfactppal_bancos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.bancos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
