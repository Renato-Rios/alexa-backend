def music_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "import": [
            {
                "name": "alexa-layouts",
                "version": "1.5.0"
            }
        ],
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    "type": "Frame",
                    "width": "100%",
                    "height": "100%",
                    "backgroundColor": "#710014", # Rojo oscuro de fondo
                    "item": {
                        "type": "Frame",
                        "width": "95%",
                        "height": "90%",
                        "alignSelf": "center",
                        "borderWidth": "2dp",
                        "borderColor": "#FFFFFF",
                        "item": {
                            "type": "Container",
                            "direction": "column",
                            "width": "100%",
                            "height": "100%",
                            "alignItems": "center",
                            "items": [
                                {"type": "Container", "height": "40dp"},
                                # TÍTULO SUPERIOR
                                {
                                    "type": "Frame",
                                    "width": "60%",
                                    "height": "60dp",
                                    "backgroundColor": "#F0F0F0",
                                    "borderRadius": "30dp",
                                    "item": {
                                        "type": "Text",
                                        "text": "CALMA TU ALMA CON UN POCO DE MÚSICA",
                                        "fontSize": "22dp",
                                        "color": "#000000",
                                        "textAlign": "center",
                                        "textAlignVertical": "center",
                                        "fontWeight": "bold",
                                        "width": "100%",
                                        "height": "100%"
                                    }
                                },
                                # CONTENEDOR DE DISCOS (CENTRADOS)
                                {
                                    "type": "Container",
                                    "direction": "row",
                                    "grow": 1,
                                    "width": "100%",
                                    "justifyContent": "space-evenly",
                                    "alignItems": "center",
                                    "items": [
                                        disco("playlist_mama", "PLAYLIST MAMÁ"),
                                        disco("playlist_renato", "PLAYLIST RENATO"),
                                        disco("playlist_oliver", "PLAYLIST OLIVER")
                                    ]
                                }
                            ]
                        }
                    }
                }
            ]
        }
    }
def disco(evento, texto):
    return {
        "type": "Container",
        "direction": "column",
        "alignItems": "center",
        "width": "220dp", # Fijamos el ancho de toda la columna del disco
        "items": [
            # CONTENEDOR DEL DISCO + NOTA
            {
                "type": "Container",
                "width": "200dp", # Mismo ancho que el disco
                "height": "200dp",
                "items": [
                    # EL VINILO
                    {
                        "type": "Frame",
                        "width": "200dp",
                        "height": "200dp",
                        "backgroundColor": "#F5F5F0",
                        "borderRadius": "100dp",
                        "borderWidth": "3dp",
                        "borderColor": "#000000",
                        "item": {
                            "type": "Frame",
                            "width": "80dp",
                            "height": "80dp",
                            "backgroundColor": "#1A1A1A",
                            "borderRadius": "40dp",
                            "alignSelf": "center", # Asegura centrado dentro del disco
                            "top": "60dp",        # Posicionamiento manual del centro
                            "item": {
                                "type": "Frame",
                                "width": "25dp",
                                "height": "25dp",
                                "backgroundColor": "#F5F5F0",
                                "borderRadius": "12dp",
                                "alignSelf": "center",
                                "top": "27dp"
                            }
                        }
                    },
                    # LA NOTA MUSICAL (Ajustada para no descuadrar)
                    {
                        "type": "Text",
                        "text": "♫",
                        "fontSize": "50dp",
                        "color": "#000000",
                        "position": "absolute",
                        "right": "10dp", # Un poco hacia adentro para evitar recortes
                        "top": "-10dp"
                    }
                ]
            },
            # BOTÓN (Ahora se alineará perfectamente abajo del disco)
            {
                "type": "TouchWrapper",
                "onPress": {
                    "type": "SendEvent",
                    "arguments": [evento]
                },
                "item": {
                    "type": "Frame",
                    "width": "180dp",
                    "height": "50dp",
                    "backgroundColor": "#D6EAF8",
                    "borderRadius": "25dp",
                    "marginTop": "30dp",
                    "item": {
                        "type": "Text",
                        "text": texto,
                        "fontSize": "16dp",
                        "color": "#005073",
                        "fontWeight": "bold",
                        "textAlign": "center",
                        "textAlignVertical": "center",
                        "width": "100%",
                        "height": "100%"
                    }
                }
            }
        ]
    }