# @class_declaration interna_descuentos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_descuentos(modelos.mtd_descuentos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_descuentos #
class flfactppal_descuentos(interna_descuentos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration descuentos #
class descuentos(flfactppal_descuentos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.descuentos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
