# @class_declaration interna_proveedores #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_proveedores(modelos.mtd_proveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_proveedores #
class flfactppal_proveedores(interna_proveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration proveedores #
class proveedores(flfactppal_proveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.proveedores_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
