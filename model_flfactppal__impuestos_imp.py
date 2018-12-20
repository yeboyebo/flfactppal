# @class_declaration interna_impuestos_imp #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_impuestos_imp(modelos.mtd_impuestos_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_impuestos_imp #
class flfactppal_impuestos_imp(interna_impuestos_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration impuestos_imp #
class impuestos_imp(flfactppal_impuestos_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.impuestos_imp_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
