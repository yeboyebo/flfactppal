# @class_declaration interna_intervalos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_intervalos(modelos.mtd_intervalos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_intervalos #
class flfactppal_intervalos(interna_intervalos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration intervalos #
class intervalos(flfactppal_intervalos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.intervalos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
