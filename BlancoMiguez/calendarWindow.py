# Form implementation generated from reading ui file 'calendarWindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_calendar(object):
    def setupUi(self, calendar):
        calendar.setObjectName("calendar")
        calendar.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        calendar.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/calendarday_January_month_calendari_1584.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        calendar.setWindowIcon(icon)
        self.calendari = QtWidgets.QCalendarWidget(parent=calendar)
        self.calendari.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.calendari.setMinimumSize(QtCore.QSize(400, 300))
        self.calendari.setMaximumSize(QtCore.QSize(400, 300))
        self.calendari.setObjectName("calendari")

        self.retranslateUi(calendar)
        QtCore.QMetaObject.connectSlotsByName(calendar)

    def retranslateUi(self, calendar):
        _translate = QtCore.QCoreApplication.translate
        calendar.setWindowTitle(_translate("calendar", "Calendario"))
