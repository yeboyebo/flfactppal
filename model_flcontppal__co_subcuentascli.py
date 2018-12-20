# @class_declaration interna_co_subcuentascli #
import importlib

from YBUTILS.viewREST import helpers

from models.flcontppal import models as modelos


class interna_co_subcuentascli(modelos.mtd_co_subcuentascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_co_subcuentascli #
class flfactppal_co_subcuentascli(interna_co_subcuentascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration co_subcuentascli #
class co_subcuentascli(flfactppal_co_subcuentascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcontppal.co_subcuentascli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
