# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration flfactppal #
from YBLEGACY.constantes import *


class flfactppal(interna):

    def flfactppal_getDesc(self):
        return "codserie"

    def __init__(self, context=None):
        super().__init__(context)

    def getDesc(self):
        return self.ctx.flfactppal_getDesc()


# @class_declaration head #
class head(flfactppal):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
