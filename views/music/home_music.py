def music_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    "type": "Frame",
                    "width": "100%",
                    "height": "100%",
                    "backgroundColor": "#710014",
                    "item": {
                        "type": "Container",
                        "width": "100%",
                        "height": "100%",
                        "alignItems": "center",
                        "items": [
                            # Recuadro blanco de borde
                            {
                                "type": "Frame",
                                "width": "95%",
                                "height": "90%",
                                "alignSelf": "center",
                                "borderWidth": "2dp",
                                "borderColor": "#FFFFFF",
                                "backgroundColor": "transparent",
                                "marginTop": "2%", # Centrado manual vertical
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
                                        # 🔷 CONTENEDOR DE DISCOS (Aquí está el arreglo del centrado)
                                        {
                                            "type": "Container",
                                            "direction": "row",
                                            "width": "100%", # Forzamos el ancho completo
                                            "grow": 1,       # Ocupa el espacio vertical restante
                                            "justifyContent": "space-evenly", # Distribuye igual a los lados y centro
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
        # Quitamos anchos fijos de este contenedor para que el 'space-evenly' del padre mande
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
                    # CÍRCULO NEGRO
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
                    # PUNTO BLANCO
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