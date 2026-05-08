def music_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    # 1. CONTENEDOR RAIZ: Ocupa toda la pantalla y centra el marco
                    "type": "Container",
                    "width": "100vw",
                    "height": "100vh",
                    "backgroundColor": "#710014",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "items": [
                        {
                            # 2. EL MARCO BLANCO: Centra todo su contenido internamente
                            "type": "Frame",
                            "width": "90%",
                            "height": "85%",
                            "borderWidth": "3dp",
                            "borderColor": "#FFFFFF",
                            "item": {
                                "type": "Container",
                                "width": "100%",
                                "height": "100%",
                                "direction": "column",
                                "alignItems": "center",
                                "justifyContent": "center", # Centrado vertical absoluto
                                "items": [
                                    # 3. TITULO: Centrado arriba con margen fijo
                                    {
                                        "type": "Frame",
                                        "width": "75%",
                                        "height": "75dp",
                                        "backgroundColor": "#E6E6E6",
                                        "borderRadius": "37.5dp",
                                        "justifyContent": "center",
                                        "alignItems": "center",
                                        "marginTop": "20dp",   # Margen superior para equilibrio
                                        "marginBottom": "auto", # Empuja los discos hacia el centro
                                        "item": {
                                            "type": "Text",
                                            "text": "CALMA TU ALMA con un poco de música".upper(),
                                            "fontSize": "24dp",
                                            "color": "#000000",
                                            "textAlign": "center",
                                            "fontWeight": "bold"
                                        }
                                    },
                                    # 4. FILA DE DISCOS: Distribución simétrica
                                    {
                                        "type": "Container",
                                        "direction": "row",
                                        "width": "100%",
                                        "grow": 1,              # Toma el espacio central
                                        "justifyContent": "space-around", # Centrado horizontal absoluto de los 3
                                        "alignItems": "center",
                                        "items": [
                                            disco("playlist_mama", "PLAYLIST MAMÁ"),
                                            disco("playlist_renato", "PLAYLIST RENATO"),
                                            disco("playlist_oliver", "PLAYLIST OLIVER")
                                        ]
                                    },
                                    # Espaciador inferior invisible para forzar el centro real
                                    {"type": "Container", "height": "20dp"}
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
        "justifyContent": "center",
        "items": [
            # EL DISCO (Círculos concéntricos)
            {
                "type": "Frame",
                "width": "160dp",
                "height": "160dp",
                "backgroundColor": "#E6E6E6",
                "borderRadius": "80dp",
                "justifyContent": "center",
                "alignItems": "center",
                "items": [
                    {
                        "type": "Frame",
                        "width": "80dp",
                        "height": "80dp",
                        "backgroundColor": "#000000",
                        "borderRadius": "40dp",
                        "justifyContent": "center",
                        "alignItems": "center",
                        "items": [
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
            # EL BOTÓN
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
                        "fontSize": "15dp",
                        "color": "#0E5678",
                        "textAlign": "center",
                        "fontWeight": "bold",
                        "width": "100%"
                    }
                }
            }
        ]
    }