# @class_declaration interna_plazos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_plazos(modelos.mtd_plazos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_plazos #
class flfactppal_plazos(interna_plazos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration plazos #
class plazos(flfactppal_plazos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.plazos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
