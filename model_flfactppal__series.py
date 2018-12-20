# @class_declaration interna_series #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_series(modelos.mtd_series, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_series #
class flfactppal_series(interna_series, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration series #
class series(flfactppal_series, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.series_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
