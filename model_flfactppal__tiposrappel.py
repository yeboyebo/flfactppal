# @class_declaration interna_tiposrappel #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_tiposrappel(modelos.mtd_tiposrappel, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_tiposrappel #
class flfactppal_tiposrappel(interna_tiposrappel, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tiposrappel #
class tiposrappel(flfactppal_tiposrappel, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.tiposrappel_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
