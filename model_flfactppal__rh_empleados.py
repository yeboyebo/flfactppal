# @class_declaration interna_rh_empleados #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_rh_empleados(modelos.mtd_rh_empleados, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_rh_empleados #
class flfactppal_rh_empleados(interna_rh_empleados, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration rh_empleados #
class rh_empleados(flfactppal_rh_empleados, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.rh_empleados_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
