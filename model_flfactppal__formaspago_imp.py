# @class_declaration interna_formaspago_imp #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_formaspago_imp(modelos.mtd_formaspago_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_formaspago_imp #
class flfactppal_formaspago_imp(interna_formaspago_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration formaspago_imp #
class formaspago_imp(flfactppal_formaspago_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.formaspago_imp_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
