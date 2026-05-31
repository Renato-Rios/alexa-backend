def fase_1_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    # 1. Estructura raíz sólida con Frame
                    "type": "Frame",
                    "width": "100%",
                    "height": "100%",
                    "backgroundColor": "#0052FF", 
                    "item": {
                        "type": "Container",
                        "width": "100%",
                        "height": "100%",
                        "items": [
                            # CONTENIDO CENTRAL (Imagen y Textos más grandes)
                            {
                                "type": "Container",
                                "grow": 1,
                                "justifyContent": "center",
                                "alignItems": "center",
                                "paddingTop": "20dp",
                                "paddingBottom": "15dp", # Espacio extra abajo para balancear el texto grande
                                "items": [
                                    # 2. Tarjeta blanca para resaltar la imagen
                                    {
                                        "type": "Frame",
                                        "width": "600dp",
                                        "height": "400dp",
                                        "borderRadius": "24dp",
                                        "backgroundColor": "#FFFFFF",
                                        "shadowColor": "#FFD037",
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
                                    # 3. Palabra Principal (¡Más grande y separada!)
                                    {
                                        "type": "Text",
                                        "text": "${payload.datosFase.word}",
                                        "fontSize": "64dp",         # Modificado: Antes 54dp
                                        "fontWeight": "900",         # Modificado: Más pesada y legible
                                        "color": "#FFFFFF",
                                        "marginTop": "30dp",        # Modificado: Más separación de la tarjeta
                                        # --- TRUCO PARA EL BORDE DE COLOR ---
                                        "shadowColor": "#FF0000",   # Color del borde (Negro en este caso)
                                        "shadowOffset": {
                                            "width": 0, 
                                            "height": 0             # Centrado para que abrace toda la letra
                                        },
                                        "shadowRadius": "8dp",      # Grosor del contorno (ajústalo a tu gusto, por ejemplo 2dp o 4dp)
                                        "shadowOpacity": 1.0        # Totalmente sólido para que parezca borde y no sombra difuminada
                                    },
                                    # 4. Texto fonético (¡Más grande!)
                                    {
                                        "type": "Text",
                                        "text": "${payload.datosFase.phonetic}",
                                        "fontSize": "32dp",         # Modificado: Antes 26dp
                                        "color": "#E0E0E0",
                                        "fontStyle": "italic",
                                        "marginTop": "8dp",         # Modificado: Más aire con la palabra principal
                                        # --- TRUCO PARA EL BORDE DE COLOR ---
                                        "shadowColor": "#FF8000",   # Color del borde (Negro en este caso)
                                        "shadowOffset": {
                                            "width": 0, 
                                            "height": 0             # Centrado para que abrace toda la letra
                                        },
                                        "shadowRadius": "8dp",      # Grosor del contorno (ajústalo a tu gusto, por ejemplo 2dp o 4dp)
                                        "shadowOpacity": 1.0 
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
                                "paddingBottom": "30dp",
                                "justifyContent": "spaceBetween",
                                "items": [
                                    # BOTÓN ATRÁS / MENÚ
                                    {
                                        "type": "TouchWrapper",
                                        "onPress": {
                                            "type": "SendEvent",
                                            "arguments": ["aprender"]
                                        },
                                        "item": {
                                            "type": "Frame",
                                            "backgroundColor": "#e63946",
                                            "borderRadius": "25dp",
                                            "paddingLeft": "30dp",
                                            "paddingRight": "30dp",
                                            "paddingTop": "12dp",
                                            "paddingBottom": "12dp",
                                            "item": {
                                                "type": "Text",
                                                "text": "MENÚ",
                                                "color": "white",
                                                "fontWeight": "700",
                                                "fontSize": "18dp"
                                            }
                                        }
                                    },
                                    # BOTÓN SIGUIENTE
                                    {
                                        "type": "TouchWrapper",
                                        "onPress": {
                                            "type": "SendEvent",
                                            "arguments": ["fase1"]
                                        },
                                        "item": {
                                            "type": "Frame",
                                            "backgroundColor": "#4cc9f0",
                                            "borderRadius": "25dp",
                                            "paddingLeft": "30dp",
                                            "paddingRight": "30dp",
                                            "paddingTop": "12dp",
                                            "paddingBottom": "12dp",
                                            "item": {
                                                "type": "Text",
                                                "text": "SIGUIENTE",
                                                "color": "#001e3d",
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