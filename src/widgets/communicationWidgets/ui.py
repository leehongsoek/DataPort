# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Thu Aug 21 04:46:53 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_commSetWidget(object):
    def setupUi(self, commSetWidget):
        commSetWidget.setObjectName(_fromUtf8("commSetWidget"))
        commSetWidget.resize(161, 311)
        self.groupBox_2 = QtGui.QGroupBox(commSetWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 161, 311))
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 50, 141, 161))
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_7)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 125, 136))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.cb_comPort = QtGui.QComboBox(self.layoutWidget)
        self.cb_comPort.setMinimumSize(QtCore.QSize(65, 0))
        self.cb_comPort.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_comPort.setObjectName(_fromUtf8("cb_comPort"))
        self.horizontalLayout.addWidget(self.cb_comPort)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cb_baudrate = QtGui.QComboBox(self.layoutWidget)
        self.cb_baudrate.setMinimumSize(QtCore.QSize(65, 0))
        self.cb_baudrate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_baudrate.setObjectName(_fromUtf8("cb_baudrate"))
        self.cb_baudrate.addItem(_fromUtf8(""))
        self.cb_baudrate.addItem(_fromUtf8(""))
        self.cb_baudrate.addItem(_fromUtf8(""))
        self.cb_baudrate.addItem(_fromUtf8(""))
        self.cb_baudrate.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cb_baudrate)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(50, 0))
        self.label_6.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.cb_dataBit = QtGui.QComboBox(self.layoutWidget)
        self.cb_dataBit.setMinimumSize(QtCore.QSize(65, 0))
        self.cb_dataBit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_dataBit.setObjectName(_fromUtf8("cb_dataBit"))
        self.cb_dataBit.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.cb_dataBit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.cb_parityBit = QtGui.QComboBox(self.layoutWidget)
        self.cb_parityBit.setMinimumSize(QtCore.QSize(65, 0))
        self.cb_parityBit.setObjectName(_fromUtf8("cb_parityBit"))
        self.cb_parityBit.addItem(_fromUtf8(""))
        self.cb_parityBit.addItem(_fromUtf8(""))
        self.cb_parityBit.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.cb_parityBit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(50, 0))
        self.label_3.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.cb_stopBit = QtGui.QComboBox(self.layoutWidget)
        self.cb_stopBit.setMinimumSize(QtCore.QSize(65, 0))
        self.cb_stopBit.setObjectName(_fromUtf8("cb_stopBit"))
        self.cb_stopBit.addItem(_fromUtf8(""))
        self.cb_stopBit.addItem(_fromUtf8(""))
        self.cb_stopBit.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cb_stopBit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_8.setEnabled(False)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 220, 141, 81))
        self.groupBox_8.setCheckable(False)
        self.groupBox_8.setChecked(False)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.groupBox_8)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 121, 52))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setMinimumSize(QtCore.QSize(30, 0))
        self.label_7.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.le_ipAddress = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.le_ipAddress.setText(_fromUtf8(""))
        self.le_ipAddress.setObjectName(_fromUtf8("le_ipAddress"))
        self.horizontalLayout_7.addWidget(self.le_ipAddress)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setMinimumSize(QtCore.QSize(30, 0))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.le_portNumber = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.le_portNumber.setObjectName(_fromUtf8("le_portNumber"))
        self.horizontalLayout_8.addWidget(self.le_portNumber)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 141, 21))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.rb_serialSelected = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rb_serialSelected.setChecked(True)
        self.rb_serialSelected.setObjectName(_fromUtf8("rb_serialSelected"))
        self.horizontalLayout_5.addWidget(self.rb_serialSelected)
        self.rb_tcpipSelected = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rb_tcpipSelected.setObjectName(_fromUtf8("rb_tcpipSelected"))
        self.horizontalLayout_5.addWidget(self.rb_tcpipSelected)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(commSetWidget)
        QtCore.QObject.connect(self.rb_serialSelected, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox_7.setEnabled)
        QtCore.QObject.connect(self.rb_tcpipSelected, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox_8.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(commSetWidget)

    def retranslateUi(self, commSetWidget):
        commSetWidget.setWindowTitle(_translate("commSetWidget", "Form", None))
        self.groupBox_2.setTitle(_translate("commSetWidget", "통신 설정", None))
        self.groupBox_7.setTitle(_translate("commSetWidget", "Serial", None))
        self.label.setText(_translate("commSetWidget", "Port", None))
        self.label_2.setText(_translate("commSetWidget", "Baudrate", None))
        self.cb_baudrate.setItemText(0, _translate("commSetWidget", "4800", None))
        self.cb_baudrate.setItemText(1, _translate("commSetWidget", "9600", None))
        self.cb_baudrate.setItemText(2, _translate("commSetWidget", "14400", None))
        self.cb_baudrate.setItemText(3, _translate("commSetWidget", "19200", None))
        self.cb_baudrate.setItemText(4, _translate("commSetWidget", "115200", None))
        self.label_6.setText(_translate("commSetWidget", "Data Bit", None))
        self.cb_dataBit.setItemText(0, _translate("commSetWidget", "8", None))
        self.label_4.setText(_translate("commSetWidget", "Parity bit", None))
        self.cb_parityBit.setItemText(0, _translate("commSetWidget", "NONE", None))
        self.cb_parityBit.setItemText(1, _translate("commSetWidget", "EVEN", None))
        self.cb_parityBit.setItemText(2, _translate("commSetWidget", "ODD", None))
        self.label_3.setText(_translate("commSetWidget", "Stop bit", None))
        self.cb_stopBit.setItemText(0, _translate("commSetWidget", "1", None))
        self.cb_stopBit.setItemText(1, _translate("commSetWidget", "1.5", None))
        self.cb_stopBit.setItemText(2, _translate("commSetWidget", "2", None))
        self.groupBox_8.setTitle(_translate("commSetWidget", "TCP/IP", None))
        self.label_7.setText(_translate("commSetWidget", "IP", None))
        self.label_8.setText(_translate("commSetWidget", "Port", None))
        self.rb_serialSelected.setText(_translate("commSetWidget", "Serial", None))
        self.rb_tcpipSelected.setText(_translate("commSetWidget", "TCP/IP", None))

