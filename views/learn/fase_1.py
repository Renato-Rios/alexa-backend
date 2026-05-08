def fase_1_gui():
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
                    "backgroundColor": "#147AB0",
                    "item": {
                        "type": "Container",
                        "width": "100%",
                        "height": "100%",
                        "items": [
                            # CONTENIDO CENTRAL (Imagen y Texto)
                            {
                                "type": "Container",
                                "grow": 1, # Esto empuja los botones hacia abajo
                                "justifyContent": "center",
                                "alignItems": "center",
                                "items": [
                                    {
                                        "type": "Image",
                                        "source": "${payload.datosFase.image}",
                                        "width": "500dp",
                                        "height": "350dp",
                                        "scale": "best-fit"
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${payload.datosFase.word}",
                                        "fontSize": "60dp",
                                        "fontWeight": "700",
                                        "color": "#FFFFFF",
                                        "marginTop": "10dp"
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${payload.datosFase.phonetic}",
                                        "fontSize": "30dp",
                                        "color": "#CCCCCC",
                                        "fontStyle": "italic"
                                    }
                                ]
                            },
                            # BARRA DE BOTONES INFERIOR
                            {
                                "type": "Container",
                                "direction": "row",
                                "width": "100%",
                                "paddingLeft": "40dp",
                                "paddingRight": "40dp",
                                "paddingBottom": "20dp",
                                "justifyContent": "spaceBetween",
                                "items": [
                                    # BOTÓN ATRÁS
                                    {
                                        "type": "TouchWrapper",
                                        "onPress": {
                                            "type": "SendEvent",
                                            "arguments": ["aprender"] # Regresa al home de aprender
                                        },
                                        "item": {
                                            "type": "Frame",
                                            "backgroundColor": "#16BA00",
                                            "borderRadius": "10dp",
                                            "padding": "15dp",
                                            "item": {
                                                "type": "Text",
                                                "text": "ATRÁS",
                                                "color": "white",
                                                "fontWeight": "bold"
                                            }
                                        }
                                    },
                                    # BOTÓN CAMBIAR (SIGUIENTE)
                                    {
                                        "type": "TouchWrapper",
                                        "onPress": {
                                            "type": "SendEvent",
                                            "arguments": ["fase1"] # Recarga la misma fase (traerá otra random)
                                        },
                                        "item": {
                                            "type": "Frame",
                                            "backgroundColor": "#3400B8",
                                            "borderRadius": "10dp",
                                            "padding": "15dp",
                                            "item": {
                                                "type": "Text",
                                                "text": "CAMBIAR",
                                                "color": "white",
                                                "fontWeight": "bold"
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    }