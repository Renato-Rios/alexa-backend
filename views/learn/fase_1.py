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
                    # 1. Gradiente de fondo moderno para un look premium
                    "background": {
                        "type": "Gradient",
                        "colorRange": ["#1e3c72", "#2a5298"],
                        "angle": 135
                    },
                    "item": {
                        "type": "Container",
                        "width": "100%",
                        "height": "100%",
                        "items": [
                            # CONTENIDO CENTRAL (Contenedor Estilizado, Imagen y Textos)
                            {
                                "type": "Container",
                                "grow": 1,
                                "justifyContent": "center",
                                "alignItems": "center",
                                "paddingTop": "20dp",
                                "items": [
                                    # 2. Tarjeta con bordes redondeados para envolver la imagen
                                    {
                                        "type": "Frame",
                                        "width": "420dp",
                                        "height": "280dp",
                                        "borderRadius": "24dp",
                                        "backgroundColor": "#FFFFFF",
                                        "shadowColor": "#000000",
                                        "shadowOffset": {"width": 0, "height": 8},
                                        "shadowRadius": "12dp",
                                        "shadowOpacity": 0.3,
                                        "item": {
                                            "type": "Image",
                                            "source": "${payload.datosFase.image}",
                                            "width": "100%",
                                            "height": "100%",
                                            "scale": "best-fill",
                                            "borderRadius": "24dp"
                                        }
                                    },
                                    # 3. Palabra Principal estilizada
                                    {
                                        "type": "Text",
                                        "text": "${payload.datosFase.word}",
                                        "fontSize": "54dp",
                                        "fontWeight": "800",
                                        "color": "#FFFFFF",
                                        "marginTop": "24dp",
                                        "shadowColor": "#000000",
                                        "shadowOffset": {"width": 0, "height": 2},
                                        "shadowRadius": "4dp"
                                    },
                                    # 4. Texto fonético más legible y estilizado
                                    {
                                        "type": "Text",
                                        "text": "${payload.datosFase.phonetic}",
                                        "fontSize": "26dp",
                                        "color": "#E0E0E0",
                                        "fontStyle": "italic",
                                        "marginTop": "4dp",
                                        "fontWeight": "300"
                                    }
                                ]
                            },
                            # BARRA DE BOTONES INFERIOR ESTILIZADA
                            {
                                "type": "Container",
                                "direction": "row",
                                "width": "100%",
                                "paddingLeft": "40dp",
                                "paddingRight": "40dp",
                                "paddingBottom": "30dp",
                                "justifyContent": "spaceBetween",
                                "items": [
                                    # BOTÓN ATRÁS (Modernizado)
                                    {
                                        "type": "TouchWrapper",
                                        "onPress": {
                                            "type": "SendEvent",
                                            "arguments": ["aprender"]
                                        },
                                        "item": {
                                            "type": "Frame",
                                            "backgroundColor": "#e63946", # Un rojo/coral sutil en vez de verde chillón
                                            "borderRadius": "25dp",
                                            "paddingLeft": "30dp",
                                            "paddingRight": "30dp",
                                            "paddingTop": "12dp",
                                            "paddingBottom": "12dp",
                                            "shadowColor": "#000000",
                                            "shadowRadius": "4dp",
                                            "item": {
                                                "type": "Text",
                                                "text": "🔀 MENÚ",
                                                "color": "white",
                                                "fontWeight": "700",
                                                "fontSize": "18dp"
                                            }
                                        }
                                    },
                                    # BOTÓN CAMBIAR / SIGUIENTE (Modernizado)
                                    {
                                        "type": "TouchWrapper",
                                        "onPress": {
                                            "type": "SendEvent",
                                            "arguments": ["fase1"]
                                        },
                                        "item": {
                                            "type": "Frame",
                                            "backgroundColor": "#4cc9f0", # Un celeste eléctrico moderno e intuitivo
                                            "borderRadius": "25dp",
                                            "paddingLeft": "30dp",
                                            "paddingRight": "30dp",
                                            "paddingTop": "12dp",
                                            "paddingBottom": "12dp",
                                            "shadowColor": "#000000",
                                            "shadowRadius": "4dp",
                                            "item": {
                                                "type": "Text",
                                                "text": "SIGUIENTE ➡️",
                                                "color": "#001e3d", # Texto oscuro para contrastar con el celeste claro
                                                "fontWeight": "700",
                                                "fontSize": "18dp"
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