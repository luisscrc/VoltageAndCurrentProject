# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Graficas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(723, 443)
        MainWindow.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.doubleSpinBox_umbral = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_umbral.setObjectName(u"doubleSpinBox_umbral")

        self.verticalLayout_4.addWidget(self.doubleSpinBox_umbral)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")

        self.verticalLayout_6.addWidget(self.start)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lcd_voltaje = QLCDNumber(self.centralwidget)
        self.lcd_voltaje.setObjectName(u"lcd_voltaje")

        self.verticalLayout_2.addWidget(self.lcd_voltaje)

        self.lcd_current = QLCDNumber(self.centralwidget)
        self.lcd_current.setObjectName(u"lcd_current")

        self.verticalLayout_2.addWidget(self.lcd_current)

        self.lcd_power = QLCDNumber(self.centralwidget)
        self.lcd_power.setObjectName(u"lcd_power")

        self.verticalLayout_2.addWidget(self.lcd_power)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_10.addLayout(self.verticalLayout_6)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:rgb(240, 240, 240);\n"
"border-radius:10px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, -1, -1)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.grafica_voltaje = QVBoxLayout()
        self.grafica_voltaje.setObjectName(u"grafica_voltaje")

        self.verticalLayout.addLayout(self.grafica_voltaje)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:rgb(240, 240, 240);\n"
"border-radius:10px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_12)

        self.grafica_corriente = QVBoxLayout()
        self.grafica_corriente.setObjectName(u"grafica_corriente")

        self.verticalLayout_7.addLayout(self.grafica_corriente)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 5)

        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color:rgb(240, 240, 240);\n"
"border-radius:10px;\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_9)

        self.graphicsView_voltage_3 = QVBoxLayout()
        self.graphicsView_voltage_3.setObjectName(u"graphicsView_voltage_3")

        self.verticalLayout_8.addLayout(self.graphicsView_voltage_3)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 5)

        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color:rgb(240, 240, 240);\n"
"border-radius:10px;\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_10)

        self.graphicsView_voltage_4 = QVBoxLayout()
        self.graphicsView_voltage_4.setObjectName(u"graphicsView_voltage_4")

        self.verticalLayout_9.addLayout(self.graphicsView_voltage_4)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 5)

        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(accessibility)
        self.label.setAccessibleName(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(accessibility)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Instrumentaci\u00f3n Virtual Aplicada", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Umbral de energ\u00eda [W/h]", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Voltaje", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Corriente", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Potencia", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Luis Esc\u00e1rcega Corona", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Voltaje", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Corriente", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Potencia", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Energ\u00eda", None))
    # retranslateUi

