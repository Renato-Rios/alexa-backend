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
                            # EL MARCO BLANCO (Ahora es solo decorativo, no empuja)
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
                            # EL TÍTULO (Flotando arriba)
                            {
                                "type": "Frame",
                                "width": "60%",
                                "height": "60dp",
                                "backgroundColor": "#F0F0F0",
                                "borderRadius": "30dp",
                                "alignSelf": "center",
                                "marginTop": "60dp",
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
                            # 🔷 BLOQUE DE DISCOS (CENTRADO ABSOLUTO EN PANTALLA)
                            {
                                "type": "Container",
                                "direction": "row",
                                "width": "100%",
                                "height": "300dp", # Altura fija para el bloque
                                "position": "absolute",
                                "top": "50%",        # Lo mandamos al centro vertical
                                "marginTop": "-100dp", # Ajuste fino para compensar su propia altura
                                "justifyContent": "center", # Centro horizontal
                                "alignItems": "center",
                                "items": [
                                    disco("playlist_mama", "PLAYLIST MAMÁ"),
                                    {"type": "Container", "width": "40dp"}, # Separación
                                    disco("playlist_renato", "PLAYLIST RENATO"),
                                    {"type": "Container", "width": "40dp"}, # Separación
                                    disco("playlist_oliver", "PLAYLIST OLIVER")
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