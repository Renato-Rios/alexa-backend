from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import requests

class VentanaInicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de Inicio")
        self.showFullScreen()
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout vertical
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        tabla = QWidget()
        tabla.setObjectName("tabla")
        
        grid = QGridLayout()
        tabla.setLayout(grid)
        
        # 🔹 Botones
        boton_musica = QPushButton("Música")
        boton_aprender = QPushButton("Aprender")
        boton_salir = QPushButton("Salir")
        
        boton_musica.setObjectName("boton_musica")
        boton_aprender.setObjectName("boton_aprender")
        boton_salir.setObjectName("boton_salir")
        
        # 🔥 CONEXIONES
        boton_musica.clicked.connect(self.mandar_musica)
        boton_aprender.clicked.connect(self.mandar_aprender)
        boton_salir.clicked.connect(self.close)
        
        boton_musica.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        boton_aprender.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        boton_salir.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        # 🔹 Grid
        grid.addWidget(boton_musica, 0, 0)
        grid.addWidget(boton_aprender, 0, 1)
        grid.addWidget(boton_salir, 1, 0, 1, 2)

        grid.setContentsMargins(50, 50, 50, 50)
        grid.setSpacing(20)
        tabla.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout.addWidget(tabla)    
        
        # 🎨 Estilos
        self.setStyleSheet("""
            QMainWindow {
                background-color: #FDF0D5;
            }

            QPushButton {
                background-color: black;
                color: white;
                font-size: 60px;
                border-radius: 12px;
            }

            QPushButton:hover {
                background-color: #333333;
            }
            
            QPushButton#boton_musica {
                background-color: #780000;
            }
            QPushButton#boton_musica:hover {
                background-color: #B00000;
            }

            QPushButton#boton_aprender {
                background-color: #003049;
            }

            QPushButton#boton_aprender:hover {
                background-color: #457B9D;
            }

            QPushButton#boton_salir {
                background-color: #000000;
            }

            QPushButton#boton_salir:hover {
                background-color: #333333;
            }
        """)

    # 🔥 FUNCIONES
    def mandar_musica(self):
        self.enviar_a_alexa("Reproduciendo música")

    def mandar_aprender(self):
        self.enviar_a_alexa("Entrando a modo aprendizaje")

    def enviar_a_alexa(self, mensaje):
        try:
            url = "https://alexa-backend-5vyw.onrender.com/hablar"
            response = requests.post(url, json={"mensaje": mensaje})
            
            print("Respuesta del servidor:", response.json())

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.show()
    app.exec()