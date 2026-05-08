def learn_gui():
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
                    "backgroundColor": "#9DB4CF",
                    "item": {
                        "type": "Container",
                        "direction": "column",
                        "width": "100%",
                        "height": "100%",
                        "alignItems": "center",
                        "paddingTop": "40dp", # Reemplaza el contenedor de espacio superior
                        "items": [
                            # 🔷 TITULO
                            {
                                "type": "Frame",
                                "width": "70%",
                                "height": "80dp",
                                "backgroundColor": "#0E5678",
                                "borderRadius": "40dp",
                                "item": {
                                    "type": "Text",
                                    "text": "¡APRENDE CON ASISTENTE C!",
                                    "fontSize": "28dp",
                                    "color": "#FFFFFF",
                                    "textAlign": "center",
                                    "textAlignVertical": "center",
                                    "width": "100%",
                                    "height": "100%"
                                }
                            },

                            # 🔷 CONTENIDO PRINCIPAL (BOTONES)
                            {
                                "type": "Container",
                                "direction": "row",
                                "width": "100%",
                                "grow": 1, # <--- ESTO hace que ocupe el resto del espacio disponible de forma equilibrada
                                "justifyContent": "space-around", # Distribuye mejor que space-between
                                "alignItems": "center",
                                "paddingLeft": "40dp",
                                "paddingRight": "40dp",
                                "items": [
                                    # LADO IZQUIERDO (FASE 1 Y 2)
                                    {
                                        "type": "Container",
                                        "direction": "column",
                                        "items": [
                                            # FASE 1
                                            {
                                                "type": "TouchWrapper",
                                                "onPress": {"type": "SendEvent", "arguments": ["fase1"]},
                                                "item": {
                                                    "type": "Frame",
                                                    "width": "220dp",
                                                    "height": "90dp",
                                                    "backgroundColor": "#0E6F7C",
                                                    "borderRadius": "30dp",
                                                    "marginBottom": "20dp",
                                                    "item": {"type": "Text", "text": "FASE 1", "color": "#FFFFFF", "fontSize": "24dp", "textAlign": "center", "textAlignVertical": "center", "height": "100%"}
                                                }
                                            },
                                            # FASE 2
                                            {
                                                "type": "TouchWrapper",
                                                "onPress": {"type": "SendEvent", "arguments": ["fase2"]},
                                                "item": {
                                                    "type": "Frame",
                                                    "width": "220dp",
                                                    "height": "90dp",
                                                    "backgroundColor": "#C2D63E",
                                                    "borderRadius": "30dp",
                                                    "item": {"type": "Text", "text": "FASE 2", "color": "#FFFFFF", "fontSize": "24dp", "textAlign": "center", "textAlignVertical": "center", "height": "100%"}
                                                }
                                            }
                                        ]
                                    },

                                    # LADO DERECHO (FASE 3 Y 4)
                                    {
                                        "type": "Container",
                                        "direction": "column",
                                        "items": [
                                            # FASE 3
                                            {
                                                "type": "TouchWrapper",
                                                "onPress": {"type": "SendEvent", "arguments": ["fase3"]},
                                                "item": {
                                                    "type": "Frame",
                                                    "width": "220dp",
                                                    "height": "90dp",
                                                    "backgroundColor": "#E58AC0",
                                                    "borderRadius": "30dp",
                                                    "marginBottom": "20dp",
                                                    "item": {"type": "Text", "text": "FASE 3", "color": "#FFFFFF", "fontSize": "24dp", "textAlign": "center", "textAlignVertical": "center", "height": "100%"}
                                                }
                                            },
                                            # FASE 4
                                            {
                                                "type": "TouchWrapper",
                                                "onPress": {"type": "SendEvent", "arguments": ["fase4"]},
                                                "item": {
                                                    "type": "Frame",
                                                    "width": "220dp",
                                                    "height": "90dp",
                                                    "backgroundColor": "#F4B04E",
                                                    "borderRadius": "30dp",
                                                    "item": {"type": "Text", "text": "FASE 4", "color": "#FFFFFF", "fontSize": "24dp", "textAlign": "center", "textAlignVertical": "center", "height": "100%"}
                                                }
                                            }
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