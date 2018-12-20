# @class_declaration interna_dirclientes #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_dirclientes(modelos.mtd_dirclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_dirclientes #
class flfactppal_dirclientes(interna_dirclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration dirclientes #
class dirclientes(flfactppal_dirclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.dirclientes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
