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
        "width": "220dp",
        "items": [
            {
                "type": "Container",
                "width": "200dp",
                "height": "200dp",
                "items": [
                    # DISCO BLANCO (BASE)
                    {
                        "type": "Frame",
                        "width": "180dp", # Un poco más pequeño para dar aire
                        "height": "180dp",
                        "backgroundColor": "#F5F5F0",
                        "borderRadius": "90dp",
                        "borderWidth": "2dp",
                        "borderColor": "#000000",
                        "alignSelf": "center",
                        "justifyContent": "center", # CENTRA EL HIJO NEGRO
                        "alignItems": "center",     # CENTRA EL HIJO NEGRO
                        "item": {
                            # CÍRCULO NEGRO
                            "type": "Frame",
                            "width": "70dp",
                            "height": "70dp",
                            "backgroundColor": "#1A1A1A",
                            "borderRadius": "35dp",
                            "justifyContent": "center", # CENTRA EL HIJO BLANCO
                            "alignItems": "center",     # CENTRA EL HIJO BLANCO
                            "item": {
                                # PUNTO BLANCO CENTRAL
                                "type": "Frame",
                                "width": "20dp",
                                "height": "20dp",
                                "backgroundColor": "#F5F5F0",
                                "borderRadius": "10dp"
                            }
                        }
                    },
                    # NOTA MUSICAL
                    {
                        "type": "Text",
                        "text": "♫",
                        "fontSize": "40dp",
                        "color": "#000000",
                        "position": "absolute",
                        "right": "15dp",
                        "top": "0dp"
                    }
                ]
            },
            # BOTÓN
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
                    "marginTop": "20dp",
                    "item": {
                        "type": "Text",
                        "text": texto,
                        "fontSize": "14dp",
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