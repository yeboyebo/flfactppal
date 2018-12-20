# @class_declaration interna_secuencias #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_secuencias(modelos.mtd_secuencias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_secuencias #
class flfactppal_secuencias(interna_secuencias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration secuencias #
class secuencias(flfactppal_secuencias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.secuencias_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
