# @class_declaration interna_divisas_imp #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_divisas_imp(modelos.mtd_divisas_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_divisas_imp #
class flfactppal_divisas_imp(interna_divisas_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration divisas_imp #
class divisas_imp(flfactppal_divisas_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.divisas_imp_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
