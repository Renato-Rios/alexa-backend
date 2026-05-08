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
        "items": [
            # GRUPO DISCO + NOTA MUSICAL
            {
                "type": "Container",
                "items": [
                    # DISCO (VINILO)
                    {
                        "type": "Frame",
                        "width": "200dp",
                        "height": "200dp",
                        "backgroundColor": "#F5F5F0", # Color crema de la imagen
                        "borderRadius": "100dp",
                        "borderWidth": "3dp",
                        "borderColor": "#000000",
                        "justifyContent": "center",
                        "alignItems": "center",
                        "item": {
                            "type": "Frame",
                            "width": "80dp",
                            "height": "80dp",
                            "backgroundColor": "#1A1A1A",
                            "borderRadius": "40dp",
                            "justifyContent": "center",
                            "alignItems": "center",
                            "item": {
                                "type": "Frame",
                                "width": "25dp",
                                "height": "25dp",
                                "backgroundColor": "#F5F5F0",
                                "borderRadius": "12dp"
                            }
                        }
                    },
                    # NOTA MUSICAL (Posicionada arriba a la derecha)
                    {
                        "type": "Text",
                        "text": "♫", # Carácter unicode o podrías usar un VectorGraphic
                        "fontSize": "60dp",
                        "color": "#000000",
                        "position": "absolute",
                        "right": "0dp",
                        "top": "-20dp"
                    }
                ]
            },
            # BOTÓN DE PLAYLIST
            {
                "type": "TouchWrapper",
                "onPress": {
                    "type": "SendEvent",
                    "arguments": [evento]
                },
                "item": {
                    "type": "Frame",
                    "width": "180dp",
                    "height": "55dp",
                    "backgroundColor": "#D6EAF8", # Azul claro
                    "borderRadius": "28dp",
                    "marginTop": "30dp",
                    "item": {
                        "type": "Text",
                        "text": texto,
                        "fontSize": "16dp",
                        "color": "#005073",
                        "textAlign": "center",
                        "textAlignVertical": "center",
                        "fontWeight": "bold",
                        "width": "100%",
                        "height": "100%"
                    }
                }
            }
        ]
    }