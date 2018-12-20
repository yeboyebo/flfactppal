# @class_declaration interna_cuentasbcopro #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_cuentasbcopro(modelos.mtd_cuentasbcopro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_cuentasbcopro #
class flfactppal_cuentasbcopro(interna_cuentasbcopro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration cuentasbcopro #
class cuentasbcopro(flfactppal_cuentasbcopro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.cuentasbcopro_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
