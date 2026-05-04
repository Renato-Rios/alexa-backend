def learn_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    # CONTENEDOR PRINCIPAL (layout)
                    "type": "Container",
                    "width": "100%",
                    "height": "100%",
                    "justifyContent": "center",
                    "alignItems": "center",
                    
                    "items": [
                        {
                            # FRAME = FONDO REAL
                            "type": "Frame",
                            "width": "100%",
                            "height": "100%",
                            "backgroundColor": "#003049",

                            "items": [
                                {
                                    # CONTENIDO CENTRADO
                                    "type": "Container",
                                    "direction": "column",
                                    "width": "100%",
                                    "height": "100%",
                                    "justifyContent": "center",
                                    "alignItems": "center",

                                    "items": [

                                        # TÍTULO
                                        {
                                            "type": "Text",
                                            "text": "Bienvenido a Aprender",
                                            "fontSize": "60dp",
                                            "color": "#1B1B1C",
                                            "marginBottom": "40dp"
                                        },

                                        # BOTÓN APRENDER
                                        {
                                            "type": "TouchWrapper",
                                            "onPress": {
                                                "type": "SendEvent",
                                                "arguments": ["fase1"]
                                            },
                                            "item": {
                                                "type": "Frame",
                                                "width": "70%",
                                                "height": "60dp",
                                                "backgroundColor": "#005B8D",
                                                "borderRadius": "25dp",
                                                "justifyContent": "center",
                                                "alignItems": "center",

                                                # TEXTO DEL BOTÓN
                                                "items": [
                                                    {
                                                        "type": "Text",
                                                        "text": "Fase 1",
                                                        "fontSize": "30dp",
                                                        "color": "#FFFFFF"
                                                    }
                                                ]
                                            }
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
