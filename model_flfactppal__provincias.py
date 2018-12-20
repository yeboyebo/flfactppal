# @class_declaration interna_provincias #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_provincias(modelos.mtd_provincias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_provincias #
class flfactppal_provincias(interna_provincias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration provincias #
class provincias(flfactppal_provincias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.provincias_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
