# @class_declaration interna_impuestos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_impuestos(modelos.mtd_impuestos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_impuestos #
class flfactppal_impuestos(interna_impuestos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration impuestos #
class impuestos(flfactppal_impuestos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.impuestos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
