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
                        "items": [
                            # MARCO BLANCO (Absoluto para que sea solo decorativo)
                            {
                                "type": "Frame",
                                "width": "94%",
                                "height": "88%",
                                "position": "absolute",
                                "alignSelf": "center",
                                "top": "6%",
                                "borderWidth": "2dp",
                                "borderColor": "#FFFFFF",
                                "backgroundColor": "transparent"
                            },
                            # CONTENEDOR DE CONTENIDO (Título + Discos)
                            {
                                "type": "Container",
                                "width": "100%",
                                "height": "100%",
                                "direction": "column",
                                "alignItems": "center",
                                "items": [
                                    # Espacio desde el borde superior de la pantalla
                                    {"type": "Container", "height": "60dp"},
                                    
                                    # TÍTULO
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
                                    
                                    # 🔷 ESTA ES LA CLAVE: Espacio entre título y discos
                                    # Cámbialo de 40dp a 20dp si quieres que estén aún más pegados
                                    {"type": "Container", "height": "80dp"}, 

                                    # FILA DE DISCOS
                                    {
                                        "type": "Container",
                                        "direction": "row",
                                        "width": "100%",
                                        "justifyContent": "center",
                                        "items": [
                                            disco("playlist_mama", "PLAYLIST MAMÁ"),
                                            {"type": "Container", "width": "30dp"},
                                            disco("playlist_renato", "PLAYLIST RENATO"),
                                            {"type": "Container", "width": "30dp"},
                                            disco("playlist_oliver", "PLAYLIST OLIVER")
                                        ]
                                    }
                                ]
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
        "items": [
            {
                "type": "Container",
                "width": "190dp",
                "height": "190dp",
                "items": [
                    # VINILO
                    {
                        "type": "Frame",
                        "width": "180dp",
                        "height": "180dp",
                        "backgroundColor": "#F5F5F0",
                        "borderRadius": "90dp",
                        "borderWidth": "2dp",
                        "borderColor": "#000000",
                        "position": "absolute",
                        "left": "5dp"
                    },
                    # CÍRCULO NEGRO
                    {
                        "type": "Frame",
                        "width": "80dp",
                        "height": "80dp",
                        "backgroundColor": "#1A1A1A",
                        "borderRadius": "40dp",
                        "position": "absolute",
                        "left": "55dp", 
                        "top": "50dp"
                    },
                    # PUNTO BLANCO
                    {
                        "type": "Frame",
                        "width": "22dp",
                        "height": "22dp",
                        "backgroundColor": "#F5F5F0",
                        "borderRadius": "11dp",
                        "position": "absolute",
                        "left": "84dp",
                        "top": "79dp"
                    },
                    # NOTA
                    {
                        "type": "Text",
                        "text": "♫",
                        "fontSize": "45dp",
                        "color": "#000000",
                        "position": "absolute",
                        "right": "0dp",
                        "top": "-10dp"
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
                    "height": "50dp",
                    "backgroundColor": "#D6EAF8",
                    "borderRadius": "25dp",
                    "marginTop": "10dp",
                    "item": {
                        "type": "Text",
                        "text": texto,
                        "fontSize": "15dp",
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