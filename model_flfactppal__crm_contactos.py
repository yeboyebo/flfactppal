# @class_declaration interna_crm_contactos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_crm_contactos(modelos.mtd_crm_contactos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactppal_crm_contactos #
class flfactppal_crm_contactos(interna_crm_contactos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration crm_contactos #
class crm_contactos(flfactppal_crm_contactos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.crm_contactos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
