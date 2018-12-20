# @class_declaration interna_paises_imp #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_paises_imp(modelos.mtd_paises_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_paises_imp #
class flfactppal_paises_imp(interna_paises_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration paises_imp #
class paises_imp(flfactppal_paises_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.paises_imp_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
