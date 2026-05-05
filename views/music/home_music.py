def music_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    # CONTENEDOR PRINCIPAL
                    "type": "Container",
                    "width": "100%",
                    "height": "100%",
                    "items": [
                        {
                            # FONDO CORRECTO
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
                                            # CONTENEDOR GENERAL (AQUÍ ESTABA EL ERROR)
                                            "type": "Container",
                                            "direction": "column",
                                            "width": "100%",
                                            "height": "100%",
                                            "alignItems": "center",
                                            "justifyContent": "flex-start",

                                            "items": [

                                                # ESPACIO ARRIBA
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
                                                    "items": [
                                                        {
                                                            "type": "Text",
                                                            "text": "CALMA TU ALMA CON UN POCO DE MÚSICA",
                                                            "fontSize": "24dp",
                                                            "color": "#000000",
                                                            "textAlign": "center",
                                                            "width": "90%"
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

                                                        # 🔴 DISCO 1
                                                        disco("playlist_mama", "PLAYLIST MAMÁ"),

                                                        # 🔴 DISCO 2
                                                        disco("playlist_renato", "PLAYLIST RENATO"),

                                                        # 🔴 DISCO 3
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


# 🔧 FUNCIÓN PARA EVITAR REPETIR CÓDIGO
def disco(evento, texto):
    return {
        "type": "Container",
        "direction": "column",
        "alignItems": "center",

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
                    # ARO INTERNO
                    {
                        "type": "Frame",
                        "width": "80dp",
                        "height": "80dp",
                        "backgroundColor": "#000000",
                        "borderRadius": "40dp",
                        "justifyContent": "center",
                        "alignItems": "center",

                        "items": [
                            # CENTRO
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
                            "width": "100%"
                        }
                    ]
                }
            }
        ]
    }