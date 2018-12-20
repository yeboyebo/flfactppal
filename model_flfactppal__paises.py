# @class_declaration interna_paises #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_paises(modelos.mtd_paises, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_paises #
class flfactppal_paises(interna_paises, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration paises #
class paises(flfactppal_paises, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.paises_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
