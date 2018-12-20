# @class_declaration interna_co_subcuentas #
import importlib

from YBUTILS.viewREST import helpers

from models.flcontppal import models as modelos


class interna_co_subcuentas(modelos.mtd_co_subcuentas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_co_subcuentas #
class flfactppal_co_subcuentas(interna_co_subcuentas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration co_subcuentas #
class co_subcuentas(flfactppal_co_subcuentas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcontppal.co_subcuentas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
