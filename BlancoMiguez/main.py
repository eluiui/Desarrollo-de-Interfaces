import eventos
from mainWindows import *
from calendarWindow import *
from acercaWindow import *
from salirWindow import *
from datetime import datetime

import sys, var, eventos, drivers



class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_calendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.calendar.calendari.setSelectedDate(QtCore.QDate(ano,mes,dia))
        var.calendar.calendari.clicked.connect(drivers.Drivers.cargaFecha)
class AcercaDe(QtWidgets.QDialog):
    def __init__(self):
        super(AcercaDe, self).__init__()
        var.acercaDe = Ui_acercaWind()
        var.acercaDe.setupUi(self)

        var.acercaDe.btnaceptar.clicked.connect(eventos.Eventos.cerrarAcercaDe)


class Salir(QtWidgets.QDialog):
    def __init__(self):
        super(Salir, self).__init__()
        var.salir = Ui_salirwind()
        var.salir.setupUi(self)

        var.salir.btnSalir.clicked.connect(eventos.Eventos.salir)
        var.salir.btnCancelar.clicked.connect(eventos.Eventos.cerrarSalir)

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)  # Encargado de la interfaz
        var.calendar=Calendar()
        var.salir=Salir()
        var.acercaDe=AcercaDe()


        '''
        Eventos Botones
        '''

        var.ui.btnCalendario.clicked.connect(eventos.Eventos.abrirCalendar)

        '''
        zona eventos menu bar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.abrirSalir)
        var.ui.actionAcercaDe.triggered.connect(eventos.Eventos.abrirAcercaDe)

        '''
        Eventos cajas texto
        '''
        var.ui.txtDNI.editingFinished.connect(drivers.Drivers.validarDNI)
        '''
        Eventos cajas texto
         '''
        var.ui.actionvarsalir.triggered.connect(eventos.Eventos.abrirSalir)
        var.ui.actionlimpiarPanel.triggered.connect(drivers.Drivers.limpiarPanel)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
