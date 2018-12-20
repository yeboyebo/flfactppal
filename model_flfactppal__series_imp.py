# @class_declaration interna_series_imp #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_series_imp(modelos.mtd_series_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_series_imp #
class flfactppal_series_imp(interna_series_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration series_imp #
class series_imp(flfactppal_series_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.series_imp_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
