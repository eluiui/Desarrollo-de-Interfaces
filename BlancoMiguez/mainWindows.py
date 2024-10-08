# Form implementation generated from reading ui file 'mainWindows.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 742)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/img/icono.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.mainTab = QtWidgets.QTabWidget(parent=self.gridFrame)
        self.mainTab.setMinimumSize(QtCore.QSize(980, 700))
        self.mainTab.setStyleSheet("")
        self.mainTab.setObjectName("mainTab")
        self.tabDrivers = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabDrivers.sizePolicy().hasHeightForWidth())
        self.tabDrivers.setSizePolicy(sizePolicy)
        self.tabDrivers.setObjectName("tabDrivers")
        self.frame = QtWidgets.QFrame(parent=self.tabDrivers)
        self.frame.setGeometry(QtCore.QRect(70, 50, 851, 141))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lblapellidos = QtWidgets.QLabel(parent=self.frame)
        self.lblapellidos.setGeometry(QtCore.QRect(10, 50, 60, 20))
        self.lblapellidos.setMinimumSize(QtCore.QSize(60, 20))
        self.lblapellidos.setObjectName("lblapellidos")
        self.txtapellidos = QtWidgets.QLineEdit(parent=self.frame)
        self.txtapellidos.setGeometry(QtCore.QRect(70, 50, 300, 20))
        self.txtapellidos.setMinimumSize(QtCore.QSize(300, 20))
        self.txtapellidos.setObjectName("txtapellidos")
        self.lblcodigo = QtWidgets.QLabel(parent=self.frame)
        self.lblcodigo.setGeometry(QtCore.QRect(10, 10, 50, 20))
        self.lblcodigo.setMinimumSize(QtCore.QSize(50, 20))
        self.lblcodigo.setObjectName("lblcodigo")
        self.lblcodigoDB = QtWidgets.QLabel(parent=self.frame)
        self.lblcodigoDB.setGeometry(QtCore.QRect(50, 10, 91, 16))
        self.lblcodigoDB.setStyleSheet("background:  rgb(255, 254, 196)")
        self.lblcodigoDB.setText("")
        self.lblcodigoDB.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblcodigoDB.setObjectName("lblcodigoDB")
        self.lblDNI = QtWidgets.QLabel(parent=self.frame)
        self.lblDNI.setGeometry(QtCore.QRect(170, 10, 50, 20))
        self.lblDNI.setMinimumSize(QtCore.QSize(50, 20))
        self.lblDNI.setObjectName("lblDNI")
        self.txtDNI = QtWidgets.QLineEdit(parent=self.frame)
        self.txtDNI.setGeometry(QtCore.QRect(200, 10, 120, 20))
        self.txtDNI.setMinimumSize(QtCore.QSize(120, 20))
        self.txtDNI.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDNI.setObjectName("txtDNI")
        self.lblcodigo_2 = QtWidgets.QLabel(parent=self.frame)
        self.lblcodigo_2.setGeometry(QtCore.QRect(410, 50, 50, 20))
        self.lblcodigo_2.setMinimumSize(QtCore.QSize(50, 20))
        self.lblcodigo_2.setObjectName("lblcodigo_2")
        self.txtnombre = QtWidgets.QLineEdit(parent=self.frame)
        self.txtnombre.setGeometry(QtCore.QRect(470, 50, 201, 20))
        self.txtnombre.setMinimumSize(QtCore.QSize(0, 20))
        self.txtnombre.setObjectName("txtnombre")
        self.lblcodigo_3 = QtWidgets.QLabel(parent=self.frame)
        self.lblcodigo_3.setGeometry(QtCore.QRect(410, 10, 71, 20))
        self.lblcodigo_3.setMinimumSize(QtCore.QSize(50, 20))
        self.lblcodigo_3.setObjectName("lblcodigo_3")
        self.txtfecha = QtWidgets.QLineEdit(parent=self.frame)
        self.txtfecha.setGeometry(QtCore.QRect(510, 10, 120, 20))
        self.txtfecha.setMinimumSize(QtCore.QSize(120, 20))
        self.txtfecha.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtfecha.setObjectName("txtfecha")
        self.btnCalendario = QtWidgets.QPushButton(parent=self.frame)
        self.btnCalendario.setGeometry(QtCore.QRect(650, 10, 21, 21))
        self.btnCalendario.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/calendarday_January_month_calendari_1584.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalendario.setIcon(icon1)
        self.btnCalendario.setObjectName("btnCalendario")
        self.lblValidarDNI = QtWidgets.QLabel(parent=self.frame)
        self.lblValidarDNI.setGeometry(QtCore.QRect(330, 10, 31, 21))
        self.lblValidarDNI.setMinimumSize(QtCore.QSize(0, 0))
        self.lblValidarDNI.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblValidarDNI.setFont(font)
        self.lblValidarDNI.setText("")
        self.lblValidarDNI.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblValidarDNI.setObjectName("lblValidarDNI")
        self.lbldir = QtWidgets.QLabel(parent=self.frame)
        self.lbldir.setGeometry(QtCore.QRect(10, 80, 47, 13))
        self.lbldir.setObjectName("lbldir")
        self.txtdir = QtWidgets.QLineEdit(parent=self.frame)
        self.txtdir.setGeometry(QtCore.QRect(70, 80, 300, 20))
        self.txtdir.setMinimumSize(QtCore.QSize(300, 20))
        self.txtdir.setObjectName("txtdir")
        self.lblmovil = QtWidgets.QLabel(parent=self.frame)
        self.lblmovil.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.lblmovil.setObjectName("lblmovil")
        self.txtmovil = QtWidgets.QLineEdit(parent=self.frame)
        self.txtmovil.setGeometry(QtCore.QRect(70, 110, 121, 20))
        self.txtmovil.setMinimumSize(QtCore.QSize(0, 20))
        self.txtmovil.setObjectName("txtmovil")
        self.lblmovil_2 = QtWidgets.QLabel(parent=self.frame)
        self.lblmovil_2.setGeometry(QtCore.QRect(640, 80, 51, 16))
        self.lblmovil_2.setObjectName("lblmovil_2")
        self.cmblocalidad = QtWidgets.QComboBox(parent=self.frame)
        self.cmblocalidad.setGeometry(QtCore.QRect(690, 80, 150, 20))
        self.cmblocalidad.setMinimumSize(QtCore.QSize(150, 20))
        self.cmblocalidad.setMaximumSize(QtCore.QSize(150, 20))
        self.cmblocalidad.setObjectName("cmblocalidad")
        self.lblmovil_3 = QtWidgets.QLabel(parent=self.frame)
        self.lblmovil_3.setGeometry(QtCore.QRect(410, 80, 51, 16))
        self.lblmovil_3.setObjectName("lblmovil_3")
        self.cmbprovincia = QtWidgets.QComboBox(parent=self.frame)
        self.cmbprovincia.setGeometry(QtCore.QRect(480, 80, 150, 20))
        self.cmbprovincia.setMinimumSize(QtCore.QSize(150, 20))
        self.cmbprovincia.setMaximumSize(QtCore.QSize(150, 20))
        self.cmbprovincia.setObjectName("cmbprovincia")
        self.lblmovil_4 = QtWidgets.QLabel(parent=self.frame)
        self.lblmovil_4.setGeometry(QtCore.QRect(200, 110, 47, 13))
        self.lblmovil_4.setObjectName("lblmovil_4")
        self.txtsalario = QtWidgets.QLineEdit(parent=self.frame)
        self.txtsalario.setGeometry(QtCore.QRect(240, 110, 111, 20))
        self.txtsalario.setMinimumSize(QtCore.QSize(0, 20))
        self.txtsalario.setObjectName("txtsalario")
        self.lbldolar = QtWidgets.QLabel(parent=self.frame)
        self.lbldolar.setGeometry(QtCore.QRect(360, 110, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbldolar.setFont(font)
        self.lbldolar.setObjectName("lbldolar")
        self.mainTab.addTab(self.tabDrivers, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 131, 16))
        self.label_2.setObjectName("label_2")
        self.mainTab.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.mainTab, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.gridFrame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1112, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(20, 20))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionSalir = QtGui.QAction(parent=MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcercaDe = QtGui.QAction(parent=MainWindow)
        self.actionAcercaDe.setObjectName("actionAcercaDe")
        self.actionvarsalir = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/logout_90894.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionvarsalir.setIcon(icon2)
        self.actionvarsalir.setObjectName("actionvarsalir")
        self.actionlimpiarPanel = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/reload_11067.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionlimpiarPanel.setIcon(icon3)
        self.actionlimpiarPanel.setObjectName("actionlimpiarPanel")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHelp.addAction(self.actionAcercaDe)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionvarsalir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionlimpiarPanel)

        self.retranslateUi(MainWindow)
        self.mainTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtDNI, self.txtfecha)
        MainWindow.setTabOrder(self.txtfecha, self.btnCalendario)
        MainWindow.setTabOrder(self.btnCalendario, self.txtapellidos)
        MainWindow.setTabOrder(self.txtapellidos, self.txtnombre)
        MainWindow.setTabOrder(self.txtnombre, self.txtdir)
        MainWindow.setTabOrder(self.txtdir, self.cmbprovincia)
        MainWindow.setTabOrder(self.cmbprovincia, self.cmblocalidad)
        MainWindow.setTabOrder(self.cmblocalidad, self.txtmovil)
        MainWindow.setTabOrder(self.txtmovil, self.txtsalario)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CarTeis"))
        self.lblapellidos.setText(_translate("MainWindow", "Apellidos"))
        self.lblcodigo.setText(_translate("MainWindow", "Codigo"))
        self.lblDNI.setText(_translate("MainWindow", "DNI"))
        self.lblcodigo_2.setText(_translate("MainWindow", "Nombre"))
        self.lblcodigo_3.setText(_translate("MainWindow", "Fecha de Alta"))
        self.lbldir.setText(_translate("MainWindow", "Direccion: "))
        self.lblmovil.setText(_translate("MainWindow", "Movil"))
        self.lblmovil_2.setText(_translate("MainWindow", "Localidad"))
        self.lblmovil_3.setText(_translate("MainWindow", "Provincia"))
        self.lblmovil_4.setText(_translate("MainWindow", "Salario"))
        self.lbldolar.setText(_translate("MainWindow", "$"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tabDrivers), _translate("MainWindow", "CONDUCTORES"))
        self.label_2.setText(_translate("MainWindow", "Esta es la pestaña 2"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHelp.setTitle(_translate("MainWindow", "Ayuda"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionAcercaDe.setText(_translate("MainWindow", "Acerca de..."))
        self.actionvarsalir.setText(_translate("MainWindow", "varsalir"))
        self.actionlimpiarPanel.setText(_translate("MainWindow", "limpiarPanel"))
