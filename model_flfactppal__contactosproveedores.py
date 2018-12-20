# @class_declaration interna_contactosproveedores #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_contactosproveedores(modelos.mtd_contactosproveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_contactosproveedores #
class flfactppal_contactosproveedores(interna_contactosproveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration contactosproveedores #
class contactosproveedores(flfactppal_contactosproveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.contactosproveedores_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
