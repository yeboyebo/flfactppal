# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration flfactppal #
from YBLEGACY.constantes import *


class flfactppal(interna):

    def flfactppal_initValidation(self, name, data=None):
        response = True
        return response

    def flfactppal_iniciaValoresLabel(self, model=None, template=None, cursor=None):
        labels = {}
        return labels

    def flfactppal_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def flfactppal_getFilters(self, model, name, template=None):
        filters = []
        return filters

    def flfactppal_getForeignFields(self, model, template=None):
        fields = []
        return fields

    def flfactppal_getDesc(self):
        desc = None
        return desc

    def __init__(self, context=None):
        super(flfactppal, self).__init__(context)

    def initValidation(self, name, data=None):
        return self.ctx.flfactppal_initValidation(name, data)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None):
        return self.ctx.flfactppal_iniciaValoresLabel(model, template, cursor)

    def bChLabel(self, fN=None, cursor=None):
        return self.ctx.flfactppal_bChLabel(fN, cursor)

    def getFilters(self, model, name, template=None):
        return self.ctx.flfactppal_getFilters(model, name, template)

    def getForeignFields(self, model, template=None):
        return self.ctx.flfactppal_getForeignFields(model, template)

    def getDesc(self):
        return self.ctx.flfactppal_getDesc()


# @class_declaration head #
class head(flfactppal):

    def __init__(self, context=None):
        super(head, self).__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super(ifaceCtx, self).__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
