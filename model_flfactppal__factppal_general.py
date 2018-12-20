# @class_declaration interna_factppal_general #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_factppal_general(modelos.mtd_factppal_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_factppal_general #
class flfactppal_factppal_general(interna_factppal_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration factppal_general #
class factppal_general(flfactppal_factppal_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.factppal_general_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
