import var,sys

class Eventos():

    @staticmethod
    def salir (self):
        try:
            sys.exit(0)

        except Exception as error:
            print(error, "en modulo enventos.")

    @staticmethod
    def abrirCalendar(self):
        try:
            var.calendar.show()
        except Exception as error:
            print(error, "en modulo eneventos")

    @staticmethod
    def cerrarAcercaDe(self):
        try:
            var.acercaDe.hide()
        except Exception as error:
            print(error + " en modulo eventos")
    def abrirAcercaDe(self):
        try:
            var.acercaDe.show()
        except Exception as error:
            print(error + " en modulo eventos")

    @staticmethod
    def abrirSalir(self):
        try:
            var.salir.show()
        except Exception as error:
            print(error + " en modulo eventos")

    @staticmethod
    def cerrarSalir(self):
        try:
            var.salir.hide()
        except Exception as error:
            print(error + " en modulo eventos")

    @staticmethod
    def acercade(self):
        try:
            pass
        except Exception as error:
            print(error + " en abrir acercade")