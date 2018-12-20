# @class_declaration interna_intervalosrappel #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_intervalosrappel(modelos.mtd_intervalosrappel, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_intervalosrappel #
class flfactppal_intervalosrappel(interna_intervalosrappel, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration intervalosrappel #
class intervalosrappel(flfactppal_intervalosrappel, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.intervalosrappel_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
