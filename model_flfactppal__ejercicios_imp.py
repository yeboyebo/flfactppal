# @class_declaration interna_ejercicios_imp #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_ejercicios_imp(modelos.mtd_ejercicios_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_ejercicios_imp #
class flfactppal_ejercicios_imp(interna_ejercicios_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration ejercicios_imp #
class ejercicios_imp(flfactppal_ejercicios_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.ejercicios_imp_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
