import sys
import numpy as np
from Backend import*
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
# Conexión con Arduino

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print("Fin de MiApp")
        self.ui.start.clicked.connect(self.inicio)

    def inicio(self):
        print("Inicio")
        umbral = self.ui.doubleSpinBox_umbral.value()
        np.t = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        # 1 Obtener Voltaje
        self.yv = [2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75]
        self.yvpromedio = sum(self.yv)/len(self.yv)
        print("Voltaje obtenido")
        # 2 Obtener Corriente
        self.yc = [0.046,0.045,0.049,0.043,0.043,0.048,0.044,0.045,0.049,0.042,0.043,0.044,0.047,0.041,0.046,0.042]
        self.ycpromedio = sum(self.yc)/len(self.yc)
        print("Corriente obtenido")
        # 3 Obtener Potencia
        self.potencia = np.multiply(self.yc,self.yv)
        self.potenciapromedio = sum(self.potencia)/len(self.potencia)
        print("Potencia obtenida")
        # 4 Desplegar en LCD
        self.ui.lcd_voltaje.display(self.yvpromedio)
        self.ui.lcd_current.display(self.ycpromedio)
        self.ui.lcd_power.display(self.potenciapromedio)
        print("Valores en LCD")
        # 5 Obtener Energía
        self.ye = sum(self.potencia)/sum(np.t)
        print("Energía obtenida")
        # 6 Graficar
        self.grafica1 = Canvas_voltage()
        self.grafica2 = Canvas_corriente()
        self.grafica3 = Canvas_potencia()
        self.grafica4 = Canvas_energia()
        self.ui.grafica_voltaje.addWidget(self.grafica1)
        self.ui.grafica_corriente.addWidget(self.grafica2)
        self.ui.grafica_potencia.addWidget(self.grafica3)
        self.ui.grafica_energia.addWidget(self.grafica4)

        print("Gráficas obtenidas")


class Canvas_voltage(FigureCanvas):  # Clase para graficar voltaje
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(
            1, dpi=80, figsize=(5, 5), sharey=True, facecolor='white')
        super().__init__(self.fig)

        np.t = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        yv = [2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75]

        self.ax = plt.axes()
        plt.plot(yv, color='orange')


class Canvas_corriente(FigureCanvas):  # Clase para graficar corriente
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(
            1, dpi=80, figsize=(5, 5), sharey=True, facecolor='white')
        super().__init__(self.fig)

        np.t = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        yc = [0.046,0.045,0.049,0.043,0.043,0.048,0.044,0.045,0.049,0.042,0.043,0.044,0.047,0.041,0.046,0.042]

        self.ax = plt.axes()
        plt.plot(yc, color='blue')


class Canvas_potencia(FigureCanvas):  # Clase para graficar potencia
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(
            1, dpi=80, figsize=(5, 5), sharey=True, facecolor='white')
        super().__init__(self.fig)

        yv = [2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75]
        yc = [0.046,0.045,0.049,0.043,0.043,0.048,0.044,0.045,0.049,0.042,0.043,0.044,0.047,0.041,0.046,0.042]
        np.t = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        yp = np.multiply(yv,yc)
        

        self.ax = plt.axes()
        plt.plot(yp, color='green')


class Canvas_energia(FigureCanvas):  # Clase para graficar energia
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(
            1, dpi=80, figsize=(5, 5), sharey=True, facecolor='white')
        super().__init__(self.fig)

        yv = [2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75,2.75]
        yc = [0.046,0.045,0.049,0.043,0.043,0.048,0.044,0.045,0.049,0.042,0.043,0.044,0.047,0.041,0.046,0.042]
        np.t = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        yp = np.multiply(yv,yc)

        ye = yp*np.t

        self.ax = plt.axes()
        plt.plot(ye, color='magenta')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())
