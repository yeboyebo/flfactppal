# @class_declaration interna_clientes #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_clientes(modelos.mtd_clientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_clientes #
class flfactppal_clientes(interna_clientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration clientes #
class clientes(flfactppal_clientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.clientes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
