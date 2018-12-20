# @class_declaration interna_ejercicios #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_ejercicios(modelos.mtd_ejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_ejercicios #
class flfactppal_ejercicios(interna_ejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration ejercicios #
class ejercicios(flfactppal_ejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.ejercicios_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
