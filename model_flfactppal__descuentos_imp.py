# @class_declaration interna_descuentos_imp #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_descuentos_imp(modelos.mtd_descuentos_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_descuentos_imp #
class flfactppal_descuentos_imp(interna_descuentos_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration descuentos_imp #
class descuentos_imp(flfactppal_descuentos_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.descuentos_imp_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
