# @class_declaration interna_divisas #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_divisas(modelos.mtd_divisas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_divisas #
class flfactppal_divisas(interna_divisas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration divisas #
class divisas(flfactppal_divisas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.divisas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
