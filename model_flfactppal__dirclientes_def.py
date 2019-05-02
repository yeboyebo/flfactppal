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
        return "descripcion"

    def flfactppal_getDireccionCliente(self, model, oParam):
        data = []

        codcliente = oParam['codcliente']
        if codcliente:
            q = qsatype.FLSqlQuery()
            q.setTablesList(u"dirclientes")
            q.setSelect("id,ciudad,dirtipovia,direccion,dirnum")
            q.setFrom("dirclientes")

            q.setWhere(ustr(u"codcliente = '", codcliente, u"' ORDER BY id"))

            if not q.exec_():
                return []

            while q.next():
                ciudad = q.value(1)
                if ciudad is None:
                    ciudad = ""
                dirtipovia = q.value(2)
                if dirtipovia is None:
                    dirtipovia = ""
                direccion = q.value(3)
                if direccion is None:
                    direccion = ""
                dirnum = q.value(4)
                if dirnum is None:
                    dirnum = ""
                descripcion = str(ciudad) + ", " + str(dirtipovia) + " " + str(direccion) + " " + str(dirnum)
                data.append({"id": str(q.value(0)), "descripcion": descripcion})

        return data

    def __init__(self, context=None):
        super().__init__(context)

    def getDesc(self):
        return self.ctx.flfactppal_getDesc()

    def getDireccionCliente(self, model, oParam):
        return self.ctx.flfactppal_getDireccionCliente(model, oParam)


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
