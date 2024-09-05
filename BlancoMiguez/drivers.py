from datetime import datetime
import var

class Drivers():

    def limpiarPanel(self):
        try:
            listawidgets=[var.ui.txtDNI, var.ui.txtfecha, var.ui.txtapellidos, var.ui.txtnombre,
                          var.ui.txtdir, var.ui.txtmovil, var.ui.txtsalario, var.ui.lblValidarDNI]
            for i in listawidgets:
                i.setText(None)
        except Exception as error:
            print(str(error) + " en validar drivers")
    def cargaFecha(qDate):
        try:
            data=('{:02d}/{:02d}/{:4d}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.txtfecha.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print(str(error) + " en validar drivers")
    def validarDNI(self=None):
        try:
            dni = var.ui.txtDNI.text()
            dni = dni.upper()
            var.ui.txtDNI.setText(dni)  # Corrección aquí
            tabla = "TRWAGMYFPDXBNJZSKVHLCKE"
            digExt = "XYZ"
            reempDigExt = {"X": '0', "Y": '1', "Z": '2'}
            numeros = "1234567890"

            if len(dni) == 9:
                digControl = dni[8]
                dni = dni[:8]
                if dni[0] in digExt:
                    dni = dni.replace(dni[0], reempDigExt[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == digControl:
                    var.ui.lblValidarDNI.setStyleSheet('color:green;')
                    var.ui.lblValidarDNI.setText('V')
                    var.ui.lblValidarDNI.setStyleSheet('background-color: white;')
                    var.ui.txtfecha.setFocus()
                else:
                    var.ui.lblValidarDNI.setStyleSheet('color:red;')
                    var.ui.lblValidarDNI.setText('X')
                    var.ui.lblValidarDNI.setStyleSheet('background-color: white;')
                    var.ui.txtDNI.setText(None)
                    var.ui.txtDNI.setFocus()
            else:
                var.ui.lblValidarDNI.setStyleSheet('color:red;')
                var.ui.lblValidarDNI.setText('X')
                var.ui.lblValidarDNI.setStyleSheet('background-color: white;')
                var.ui.txtDNI.setText(None)
                var.ui.txtDNI.setFocus()
        except Exception as error:
            print(str(error) + " en validar drivers")
