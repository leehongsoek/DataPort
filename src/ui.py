# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Sat Apr 26 09:56:10 2014
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(835, 712)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, 30, 821, 641))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 6))
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 161, 341))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 20, 141, 191))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_7)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 123, 165))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_Comport = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_Comport.setObjectName(_fromUtf8("comboBox_Comport"))
        self.horizontalLayout.addWidget(self.comboBox_Comport)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_Baudrate = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_Baudrate.setObjectName(_fromUtf8("comboBox_Baudrate"))
        self.comboBox_Baudrate.addItem(_fromUtf8(""))
        self.comboBox_Baudrate.addItem(_fromUtf8(""))
        self.comboBox_Baudrate.addItem(_fromUtf8(""))
        self.comboBox_Baudrate.addItem(_fromUtf8(""))
        self.comboBox_Baudrate.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_Baudrate)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.comboBox_stopBit_2 = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_stopBit_2.setObjectName(_fromUtf8("comboBox_stopBit_2"))
        self.comboBox_stopBit_2.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.comboBox_stopBit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_parityBit = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_parityBit.setObjectName(_fromUtf8("comboBox_parityBit"))
        self.comboBox_parityBit.addItem(_fromUtf8(""))
        self.comboBox_parityBit.addItem(_fromUtf8(""))
        self.comboBox_parityBit.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.comboBox_parityBit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_stopBit = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_stopBit.setObjectName(_fromUtf8("comboBox_stopBit"))
        self.comboBox_stopBit.addItem(_fromUtf8(""))
        self.comboBox_stopBit.addItem(_fromUtf8(""))
        self.comboBox_stopBit.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboBox_stopBit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_connect = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.verticalLayout.addWidget(self.pushButton_connect)
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 220, 141, 111))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.groupBox_8)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 121, 81))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_8.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 360, 791, 241))
        self.groupBox.setMinimumSize(QtCore.QSize(124, 0))
        self.groupBox.setBaseSize(QtCore.QSize(86, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.groupBox.setPalette(palette)
        self.groupBox.setToolTip(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 20, 601, 161))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.groupBox_9.setPalette(palette)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.groupBox_9)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 581, 21))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.radioButton = QtGui.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_9.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_9.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_9.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_9.addWidget(self.radioButton_4)
        self.radioButton_5 = QtGui.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.horizontalLayout_9.addWidget(self.radioButton_5)
        self.horizontalLayoutWidget_5 = QtGui.QWidget(self.groupBox_9)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 50, 581, 22))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.comboBox_HexOrAscii = QtGui.QComboBox(self.horizontalLayoutWidget_5)
        self.comboBox_HexOrAscii.setMinimumSize(QtCore.QSize(5, 0))
        self.comboBox_HexOrAscii.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_HexOrAscii.setObjectName(_fromUtf8("comboBox_HexOrAscii"))
        self.comboBox_HexOrAscii.addItem(_fromUtf8(""))
        self.comboBox_HexOrAscii.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.comboBox_HexOrAscii)
        self.lineEdit_head1 = QtGui.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_head1.setMaximumSize(QtCore.QSize(45, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_head1.setPalette(palette)
        font = QtGui.QFont()
        font.setItalic(False)
        self.lineEdit_head1.setFont(font)
        self.lineEdit_head1.setToolTip(_fromUtf8(""))
        self.lineEdit_head1.setAutoFillBackground(True)
        self.lineEdit_head1.setText(_fromUtf8(""))
        self.lineEdit_head1.setObjectName(_fromUtf8("lineEdit_head1"))
        self.horizontalLayout_10.addWidget(self.lineEdit_head1)
        self.lineEdit_head2 = QtGui.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_head2.setMaximumSize(QtCore.QSize(45, 16777215))
        self.lineEdit_head2.setObjectName(_fromUtf8("lineEdit_head2"))
        self.horizontalLayout_10.addWidget(self.lineEdit_head2)
        self.lineEdit_protocol = QtGui.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_protocol.setMinimumSize(QtCore.QSize(244, 0))
        self.lineEdit_protocol.setMaximumSize(QtCore.QSize(312, 16777215))
        self.lineEdit_protocol.setObjectName(_fromUtf8("lineEdit_protocol"))
        self.horizontalLayout_10.addWidget(self.lineEdit_protocol)
        self.lineEdit_tail1 = QtGui.QLineEdit(self.horizontalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tail1.sizePolicy().hasHeightForWidth())
        self.lineEdit_tail1.setSizePolicy(sizePolicy)
        self.lineEdit_tail1.setMaximumSize(QtCore.QSize(45, 16777215))
        self.lineEdit_tail1.setObjectName(_fromUtf8("lineEdit_tail1"))
        self.horizontalLayout_10.addWidget(self.lineEdit_tail1)
        self.lineEdit_tail2 = QtGui.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_tail2.setMaximumSize(QtCore.QSize(45, 16777215))
        self.lineEdit_tail2.setObjectName(_fromUtf8("lineEdit_tail2"))
        self.horizontalLayout_10.addWidget(self.lineEdit_tail2)
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.groupBox_9)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 130, 581, 27))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_11.setMargin(0)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.checkBox_autoSending = QtGui.QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_autoSending.setObjectName(_fromUtf8("checkBox_autoSending"))
        self.horizontalLayout_11.addWidget(self.checkBox_autoSending)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(12, 0))
        self.label_9.setMaximumSize(QtCore.QSize(68, 16777215))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.spinBox_intervalTime = QtGui.QSpinBox(self.horizontalLayoutWidget_6)
        self.spinBox_intervalTime.setMaximum(999999999)
        self.spinBox_intervalTime.setObjectName(_fromUtf8("spinBox_intervalTime"))
        self.horizontalLayout_5.addWidget(self.spinBox_intervalTime)
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(23, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_5)
        self.line = QtGui.QFrame(self.groupBox_9)
        self.line.setGeometry(QtCore.QRect(10, 120, 581, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_9)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 411, 22))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_12.setMargin(0)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.comboBox_checkList = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_checkList.setMinimumSize(QtCore.QSize(140, 0))
        self.comboBox_checkList.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox_checkList.setObjectName(_fromUtf8("comboBox_checkList"))
        self.comboBox_checkList.addItem(_fromUtf8(""))
        self.comboBox_checkList.addItem(_fromUtf8(""))
        self.comboBox_checkList.addItem(_fromUtf8(""))
        self.comboBox_checkList.addItem(_fromUtf8(""))
        self.horizontalLayout_12.addWidget(self.comboBox_checkList)
        self.label_10 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_12.addWidget(self.label_10)
        self.lineEdit_checkStartIndex = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_checkStartIndex.setObjectName(_fromUtf8("lineEdit_checkStartIndex"))
        self.horizontalLayout_12.addWidget(self.lineEdit_checkStartIndex)
        self.label_11 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_12.addWidget(self.label_11)
        self.lineEdit_checkEndIndex = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_checkEndIndex.setObjectName(_fromUtf8("lineEdit_checkEndIndex"))
        self.horizontalLayout_12.addWidget(self.lineEdit_checkEndIndex)
        self.label_12 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_12.addWidget(self.label_12)
        self.lineEdit_checkPosition = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_checkPosition.setObjectName(_fromUtf8("lineEdit_checkPosition"))
        self.horizontalLayout_12.addWidget(self.lineEdit_checkPosition)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 20, 161, 161))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 141, 135))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout_2.addWidget(self.comboBox)
        self.lineEdit_protocolName = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_protocolName.setObjectName(_fromUtf8("lineEdit_protocolName"))
        self.verticalLayout_2.addWidget(self.lineEdit_protocolName)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 190, 771, 41))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(460, 10, 341, 341))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.toolBox_2 = QtGui.QToolBox(self.groupBox_4)
        self.toolBox_2.setGeometry(QtCore.QRect(10, 20, 321, 311))
        self.toolBox_2.setObjectName(_fromUtf8("toolBox_2"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 321, 259))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.textEdit_3 = QtGui.QTextEdit(self.page_3)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 0, 321, 251))
        self.textEdit_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.textEdit_3.setTabChangesFocus(True)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setOverwriteMode(False)
        self.textEdit_3.setAcceptRichText(True)
        self.textEdit_3.setCursorWidth(1)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.toolBox_2.addItem(self.page_3, _fromUtf8(""))
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 321, 259))
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.textEdit_2 = QtGui.QTextEdit(self.page_4)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 321, 251))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.toolBox_2.addItem(self.page_4, _fromUtf8(""))
        self.groupBox_5 = QtGui.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(180, 10, 271, 341))
        self.groupBox_5.setAutoFillBackground(False)
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.toolBox = QtGui.QToolBox(self.groupBox_5)
        self.toolBox.setGeometry(QtCore.QRect(10, 20, 251, 311))
        self.toolBox.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.RepublicOfKorea))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 251, 259))
        self.page.setObjectName(_fromUtf8("page"))
        self.textEdit_1 = QtGui.QTextEdit(self.page)
        self.textEdit_1.setGeometry(QtCore.QRect(0, 0, 251, 251))
        self.textEdit_1.setReadOnly(True)
        self.textEdit_1.setObjectName(_fromUtf8("textEdit_1"))
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 251, 259))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.textEdit_4 = QtGui.QTextEdit(self.page_2)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 0, 251, 251))
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Protocol = QtGui.QAction(MainWindow)
        self.actionNew_Protocol.setObjectName(_fromUtf8("actionNew_Protocol"))
        self.actionOpen_Protocol = QtGui.QAction(MainWindow)
        self.actionOpen_Protocol.setObjectName(_fromUtf8("actionOpen_Protocol"))
        self.actionSave_Protocol = QtGui.QAction(MainWindow)
        self.actionSave_Protocol.setObjectName(_fromUtf8("actionSave_Protocol"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.menuFile.addAction(self.actionNew_Protocol)
        self.menuFile.addAction(self.actionOpen_Protocol)
        self.menuFile.addAction(self.actionSave_Protocol)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)
        QtCore.QObject.connect(self.textEdit_1, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.textEdit_1.setModified)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "통신 설정", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Serial", None))
        self.label.setText(_translate("MainWindow", "Port", None))
        self.label_2.setText(_translate("MainWindow", "Baudrate", None))
        self.comboBox_Baudrate.setItemText(0, _translate("MainWindow", "4800", None))
        self.comboBox_Baudrate.setItemText(1, _translate("MainWindow", "9600", None))
        self.comboBox_Baudrate.setItemText(2, _translate("MainWindow", "14400", None))
        self.comboBox_Baudrate.setItemText(3, _translate("MainWindow", "19200", None))
        self.comboBox_Baudrate.setItemText(4, _translate("MainWindow", "115200", None))
        self.label_6.setText(_translate("MainWindow", "Data Bit", None))
        self.comboBox_stopBit_2.setItemText(0, _translate("MainWindow", "8", None))
        self.label_4.setText(_translate("MainWindow", "Parity bit", None))
        self.comboBox_parityBit.setItemText(0, _translate("MainWindow", "NONE", None))
        self.comboBox_parityBit.setItemText(1, _translate("MainWindow", "EVEN", None))
        self.comboBox_parityBit.setItemText(2, _translate("MainWindow", "ODD", None))
        self.label_3.setText(_translate("MainWindow", "Stop bit", None))
        self.comboBox_stopBit.setItemText(0, _translate("MainWindow", "1", None))
        self.comboBox_stopBit.setItemText(1, _translate("MainWindow", "1.5", None))
        self.comboBox_stopBit.setItemText(2, _translate("MainWindow", "2", None))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "TCP/IP", None))
        self.label_7.setText(_translate("MainWindow", "IP", None))
        self.label_8.setText(_translate("MainWindow", "Port", None))
        self.pushButton_2.setText(_translate("MainWindow", "Connect", None))
        self.groupBox.setTitle(_translate("MainWindow", "입력", None))
        self.groupBox_9.setTitle(_translate("MainWindow", "프로토콜", None))
        self.radioButton.setText(_translate("MainWindow", "없음", None))
        self.radioButton_2.setText(_translate("MainWindow", "CR (0x0D)", None))
        self.radioButton_3.setText(_translate("MainWindow", "LF (0x0A)", None))
        self.radioButton_4.setText(_translate("MainWindow", "CR + LF (0x0D + 0x0A)", None))
        self.radioButton_5.setText(_translate("MainWindow", "STX + ETX + CRLF(0x02, 0x03)", None))
        self.comboBox_HexOrAscii.setItemText(0, _translate("MainWindow", "HEX", None))
        self.comboBox_HexOrAscii.setItemText(1, _translate("MainWindow", "ASCII", None))
        self.checkBox_autoSending.setText(_translate("MainWindow", "자동 전송", None))
        self.label_9.setText(_translate("MainWindow", "전송 간격", None))
        self.label_5.setText(_translate("MainWindow", "ms", None))
        self.comboBox_checkList.setItemText(0, _translate("MainWindow", "NONE", None))
        self.comboBox_checkList.setItemText(1, _translate("MainWindow", "CHECKSUM(1Byte)", None))
        self.comboBox_checkList.setItemText(2, _translate("MainWindow", "CRC16", None))
        self.comboBox_checkList.setItemText(3, _translate("MainWindow", "CheckXorSum(2Byte)", None))
        self.label_10.setText(_translate("MainWindow", "시작", None))
        self.label_11.setText(_translate("MainWindow", "끝", None))
        self.label_12.setText(_translate("MainWindow", "위치", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "프로토콜 관리", None))
        self.pushButton.setText(_translate("MainWindow", "프로토콜 불러오기", None))
        self.pushButton_4.setText(_translate("MainWindow", "프로토콜 추가하기", None))
        self.pushButton_5.setText(_translate("MainWindow", "프로토콜 삭제하기", None))
        self.pushButton_3.setText(_translate("MainWindow", "전송", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "수신", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), _translate("MainWindow", "Hex", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), _translate("MainWindow", "Ascii", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "송신", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Hex", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Ascii", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.menuFile.setTitle(_translate("MainWindow", "파일", None))
        self.menu.setTitle(_translate("MainWindow", "보기", None))
        self.menu_2.setTitle(_translate("MainWindow", "창", None))
        self.menu_3.setTitle(_translate("MainWindow", "도움말", None))
        self.actionNew_Protocol.setText(_translate("MainWindow", "New Protocol", None))
        self.actionOpen_Protocol.setText(_translate("MainWindow", "Open Protocol", None))
        self.actionSave_Protocol.setText(_translate("MainWindow", "Save Protocol", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.action.setText(_translate("MainWindow", "실황 화면", None))

