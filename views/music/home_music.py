def music_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    "type": "Container",
                    "width": "100vw",
                    "height": "100vh",
                    "backgroundColor": "#710014",
                    "alignItems": "center",       # Centra horizontalmente todo el bloque
                    "justifyContent": "center",    # Centra verticalmente todo el bloque
                    "items": [
                        {
                            # MARCO / BORDE BLANCO
                            "type": "Frame",
                            "width": "90%",
                            "height": "85%",
                            "borderWidth": "3dp",
                            "borderColor": "#FFFFFF",
                            "item": {
                                # CONTENEDOR DE CONTENIDO (Dentro del borde)
                                "type": "Container",
                                "width": "100%",
                                "height": "100%",
                                "direction": "column",
                                "alignItems": "center",
                                "justifyContent": "center", # <--- Centrado absoluto vertical
                                "items": [
                                    # TITULO
                                    {
                                        "type": "Frame",
                                        "width": "75%",
                                        "height": "75dp",
                                        "backgroundColor": "#E6E6E6",
                                        "borderRadius": "37.5dp",
                                        "justifyContent": "center",
                                        "alignItems": "center",
                                        "marginBottom": "50dp", # Espacio debajo del título
                                        "item": {
                                            "type": "Text",
                                            "text": "CALMA TU ALMA CON UN POCO DE MÚSICA",
                                            "fontSize": "26dp", # Un poco más grande para mejor lectura
                                            "color": "#000000",
                                            "textAlign": "center",
                                            "fontWeight": "bold"
                                        }
                                    },
                                    # FILA DE DISCOS (Aquí es donde estaba el problema)
                                    {
                                        "type": "Container",
                                        "direction": "row",
                                        "width": "100%",
                                        "justifyContent": "space-evenly", # <--- CAMBIO CLAVE: Distribuye discos y espacio
                                        "alignItems": "center",
                                        "items": [
                                            # Llamadas a la función disco con argumentos corregidos
                                            disco("playlist_mama", "PLAYLIST MAMÁ"),
                                            disco("playlist_renato", "PLAYLIST RENATO"),
                                            disco("playlist_oliver", "PLAYLIST OLIVER")
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }
    }


def disco(evento, texto):
    return {
        "type": "Container",
        "direction": "column",
        "alignItems": "center",
        # Quitamos padding lateral aquí, space-evenly se encarga del espacio
        "items": [
            # CÍRCULO GRANDE (Efecto Disco)
            {
                "type": "Frame",
                "width": "160dp",
                "height": "160dp",
                "backgroundColor": "#E6E6E6",
                "borderRadius": "80dp",
                "justifyContent": "center",
                "alignItems": "center",
                "items": [
                    # CÍRCULO NEGRO
                    {
                        "type": "Frame",
                        "width": "80dp",
                        "height": "80dp",
                        "backgroundColor": "#000000",
                        "borderRadius": "40dp",
                        "justifyContent": "center",
                        "alignItems": "center",
                        "items": [
                            # CENTRO BLANCO
                            {
                                "type": "Frame",
                                "width": "20dp",
                                "height": "20dp",
                                "backgroundColor": "#E6E6E6",
                                "borderRadius": "10dp"
                            }
                        ]
                    }
                ]
            },
            # BOTÓN / ETIQUETA
            {
                "type": "TouchWrapper",
                "onPress": {
                    "type": "SendEvent",
                    "arguments": [evento]
                },
                "item": {
                    "type": "Frame",
                    "width": "160dp",
                    "height": "50dp",
                    "backgroundColor": "#CFE3E8",
                    "borderRadius": "25dp",
                    "marginTop": "20dp",
                    "justifyContent": "center",
                    "alignItems": "center",
                    "item": {
                        "type": "Text",
                        "text": texto,
                        "fontSize": "16dp",
                        "color": "#0E5678",
                        "textAlign": "center", # Asegura el centrado del texto interno
                        "fontWeight": "bold",
                        "width": "100%"
                    }
                }
            }
        ]
    }