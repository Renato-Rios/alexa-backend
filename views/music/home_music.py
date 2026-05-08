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
                            "justifyContent": "center",  # Centra verticalmente el borde blanco
                            "alignItems": "center",      # Centra horizontalmente el borde blanco

                            "items": [
                                {
                                    # BORDE
                                    "type": "Frame",
                                    "width": "90%",
                                    "height": "85%",
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
                                            "justifyContent": "center", # Centra todo el contenido verticalmente dentro del borde

                                            "items": [
                                                # TITULO
                                                {
                                                    "type": "Frame",
                                                    "width": "70%",
                                                    "height": "70dp",
                                                    "backgroundColor": "#E6E6E6",
                                                    "borderRadius": "35dp",
                                                    "justifyContent": "center",
                                                    "alignItems": "center",
                                                    "items": [
                                                        {
                                                            "type": "Text",
                                                            "text": "CALMA TU ALMA CON UN POCO DE MÚSICA",
                                                            "fontSize": "22dp",
                                                            "color": "#000000",
                                                            "textAlign": "center",
                                                            "fontWeight": "bold",
                                                            "width": "100%"
                                                        }
                                                    ]
                                                },

                                                # Espacio controlado entre el título y los discos
                                                {"type": "Container", "height": "40dp"},

                                                # FILA DE DISCOS (Centrada horizontalmente)
                                                {
                                                    "type": "Container",
                                                    "direction": "row",
                                                    "width": "100%",
                                                    "justifyContent": "center", # Los junta y los centra en grupo
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
        "paddingLeft": "15dp",   # Margen interno para que no se peguen entre sí
        "paddingRight": "15dp",  # Margen interno para que no se peguen entre sí

        "items": [
            # CÍRCULO GRANDE (Representación del disco de vinilo concéntrico)
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

            # BOTÓN / TEXTO (Alineado justo debajo del círculo)
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
                    "marginTop": "15dp", # Espacio ideal entre el disco y su botón
                    "justifyContent": "center",
                    "alignItems": "center",

                    "items": [
                        {
                            "type": "Text",
                            "text": texto,
                            "fontSize": "14dp", # Ajustado ligeramente para asegurar que quepa bien en pantallas pequeñas
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