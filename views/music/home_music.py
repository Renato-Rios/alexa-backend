def music_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    "type": "Container",
                    "width": "100%",
                    "height": "100%",
                    "items": [
                        {
                            # FONDO
                            "type": "Frame",
                            "width": "100%",
                            "height": "100%",
                            "backgroundColor": "#710014",

                            "items": [
                                {
                                    # BORDE
                                    "type": "Frame",
                                    "width": "90%",
                                    "height": "85%",
                                    "alignSelf": "center",
                                    "borderWidth": "3dp",
                                    "borderColor": "#FFFFFF",

                                    "items": [
                                        {
                                            # CONTENEDOR GENERAL
                                            "type": "Container",
                                            "direction": "column",
                                            "width": "100%",
                                            "height": "100%",
                                            "alignItems": "center",
                                            "justifyContent": "flex-start",

                                            "items": [

                                                {"type": "Container", "height": "40dp"},

                                                # TITULO
                                                {
                                                    "type": "Frame",
                                                    "width": "70%",
                                                    "height": "70dp",
                                                    "backgroundColor": "#E6E6E6",
                                                    "borderRadius": "40dp",
                                                    "justifyContent": "center",
                                                    "alignItems": "center",
                                                    "alignSelf": "center",
                                                    "items": [
                                                        {
                                                            "type": "Text",
                                                            "text": "CALMA TU ALMA CON UN POCO DE MÚSICA",
                                                            "fontSize": "24dp",
                                                            "color": "#000000",
                                                            "textAlign": "center",
                                                            "fontWeight": "bold",
                                                            "width": "100%"
                                                        }
                                                    ]
                                                },

                                                {"type": "Container", "height": "60dp"},

                                                # FILA DE DISCOS
                                                {
                                                    "type": "Container",
                                                    "direction": "row",
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
                                    ]
                                }
                            ]
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

            # CÍRCULO GRANDE
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

            # BOTÓN
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

                    "items": [
                        {
                            "type": "Text",
                            "text": texto,
                            "fontSize": "18dp",
                            "color": "#0E5678",
                            "textAlign": "center",
                            "fontWeight": "bold",
                            "width": "100%"
                        }
                    ]
                }
            }
        ]
    }