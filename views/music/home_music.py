def music_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    # ESTE FRAME DA EL COLOR ROJO
                    "type": "Frame",
                    "width": "100%",
                    "height": "100%",
                    "backgroundColor": "#710014", 
                    "item": {
                        # ESTE CONTAINER CENTRA EL RECUADRO BLANCO
                        "type": "Container",
                        "width": "100%",
                        "height": "100%",
                        "justifyContent": "center",
                        "alignItems": "center",
                        "items": [
                            {
                                "type": "Frame",
                                "width": "95%",
                                "height": "90%",
                                "borderWidth": "2dp",
                                "borderColor": "#FFFFFF",
                                "backgroundColor": "transparent",
                                "item": {
                                    "type": "Container",
                                    "direction": "column",
                                    "width": "100%",
                                    "height": "100%",
                                    "items": [
                                        {"type": "Container", "height": "40dp"},
                                        # TÍTULO
                                        {
                                            "type": "Frame",
                                            "width": "60%",
                                            "height": "60dp",
                                            "backgroundColor": "#F0F0F0",
                                            "borderRadius": "30dp",
                                            "alignSelf": "center",
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
                                        # DISCOS
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
                        ]
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
                    # DISCO BASE
                    {
                        "type": "Frame",
                        "width": "180dp",
                        "height": "180dp",
                        "backgroundColor": "#F5F5F0",
                        "borderRadius": "90dp",
                        "borderWidth": "2dp",
                        "borderColor": "#000000",
                        "position": "absolute",
                        "left": "10dp",
                        "top": "10dp"
                    },
                    # CÍRCULO NEGRO (Calculado al centro de 200dp)
                    {
                        "type": "Frame",
                        "width": "80dp",
                        "height": "80dp",
                        "backgroundColor": "#1A1A1A",
                        "borderRadius": "40dp",
                        "position": "absolute",
                        "left": "60dp", 
                        "top": "60dp"
                    },
                    # PUNTO BLANCO (Calculado al centro de 200dp)
                    {
                        "type": "Frame",
                        "width": "24dp",
                        "height": "24dp",
                        "backgroundColor": "#F5F5F0",
                        "borderRadius": "12dp",
                        "position": "absolute",
                        "left": "88dp",
                        "top": "88dp"
                    },
                    # NOTA
                    {
                        "type": "Text",
                        "text": "♫",
                        "fontSize": "45dp",
                        "color": "#000000",
                        "position": "absolute",
                        "right": "10dp",
                        "top": "0dp"
                    }
                ]
            },
            # BOTÓN
            {
                "type": "TouchWrapper",
                "onPress": {"type": "SendEvent", "arguments": [evento]},
                "item": {
                    "type": "Frame",
                    "width": "190dp",
                    "height": "55dp",
                    "backgroundColor": "#D6EAF8",
                    "borderRadius": "28dp",
                    "marginTop": "15dp",
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