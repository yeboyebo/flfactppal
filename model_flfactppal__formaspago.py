# @class_declaration interna_formaspago #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_formaspago(modelos.mtd_formaspago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_formaspago #
class flfactppal_formaspago(interna_formaspago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration formaspago #
class formaspago(flfactppal_formaspago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.formaspago_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
