# @class_declaration interna_zonasgeo #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_zonasgeo(modelos.mtd_zonasgeo, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_zonasgeo #
class flfactppal_zonasgeo(interna_zonasgeo, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration zonasgeo #
class zonasgeo(flfactppal_zonasgeo, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.zonasgeo_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
