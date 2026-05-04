def learn_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    # CONTENEDOR PRINCIPAL
                    "type": "Container",
                    "width": "100%",
                    "height": "100%",
                    "items": [
                        {
                            # FONDO AZUL CLARO
                            "type": "Frame",
                            "width": "100%",
                            "height": "100%",
                            "backgroundColor": "#9DB4CF",
                            "items": [
                                {
                                    # CONTENEDOR GENERAL
                                    "type": "Container",
                                    "direction": "column",
                                    "width": "100%",
                                    "height": "100%",
                                    "alignItems": "center",

                                    "items": [

                                        # 🔷 ESPACIO ARRIBA (BAJA EL TITULO)
                                        {
                                            "type": "Container",
                                            "height": "60dp"
                                        },

                                        # 🔷 TITULO
                                        {
                                            "type": "Frame",
                                            "width": "60%",
                                            "height": "70dp",
                                            "backgroundColor": "#0E5678",
                                            "borderRadius": "40dp",
                                            "justifyContent": "center",
                                            "alignItems": "center",
                                            "items": [
                                                {
                                                    "type": "Text",
                                                    "text": "¡APRENDE CON ASISTENTE C!",
                                                    "fontSize": "28dp",
                                                    "color": "#FFFFFF",
                                                    "textAlign": "center",
                                                    "width": "100%"
                                                }
                                            ]
                                        },

                                        # 🔷 ESPACIO ENTRE TITULO Y CONTENIDO
                                        {
                                            "type": "Container",
                                            "height": "40dp"
                                        },

                                        # 🔷 ZONA CENTRAL (RECORRIDO)
                                        {
                                            "type": "Container",
                                            "width": "100%",
                                            "height": "100%",
                                            "items": [

                                                # FASE 1 (ARRIBA IZQUIERDA)
                                                {
                                                    "type": "TouchWrapper",
                                                    "onPress": {
                                                        "type": "SendEvent",
                                                        "arguments": ["fase1"]
                                                    },
                                                    "item": {
                                                        "type": "Frame",
                                                        "width": "200dp",
                                                        "height": "90dp",
                                                        "backgroundColor": "#0E6F7C",
                                                        "borderRadius": "30dp",
                                                        "position": "absolute",
                                                        "top": "40dp",
                                                        "left": "120dp",
                                                        "items": [
                                                            {
                                                                "type": "Container",
                                                                "width": "100%",
                                                                "height": "100%",
                                                                "justifyContent": "center",
                                                                "alignItems": "center",
                                                                "items": [
                                                                    {
                                                                        "type": "Text",
                                                                        "text": "FASE 1",
                                                                        "fontSize": "22dp",
                                                                        "color": "#FFFFFF",
                                                                        "textAlign": "center",
                                                                        "width": "100%"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                },

                                                # LINEA SUPERIOR
                                                {
                                                    "type": "Frame",
                                                    "width": "500dp",
                                                    "height": "3dp",
                                                    "backgroundColor": "#000000",
                                                    "position": "absolute",
                                                    "top": "85dp",
                                                    "left": "320dp"
                                                },

                                                # FASE 2 (ARRIBA DERECHA)
                                                {
                                                    "type": "TouchWrapper",
                                                    "onPress": {
                                                        "type": "SendEvent",
                                                        "arguments": ["fase2"]
                                                    },
                                                    "item": {
                                                        "type": "Frame",
                                                        "width": "200dp",
                                                        "height": "90dp",
                                                        "backgroundColor": "#C2D63E",
                                                        "borderRadius": "30dp",
                                                        "position": "absolute",
                                                        "top": "40dp",
                                                        "right": "120dp",
                                                        "items": [
                                                            {
                                                                "type": "Container",
                                                                "width": "100%",
                                                                "height": "100%",
                                                                "justifyContent": "center",
                                                                "alignItems": "center",
                                                                "items": [
                                                                    {
                                                                        "type": "Text",
                                                                        "text": "FASE 2",
                                                                        "fontSize": "22dp",
                                                                        "color": "#FFFFFF",
                                                                        "textAlign": "center",
                                                                        "width": "100%"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                },

                                                # LINEA DERECHA
                                                {
                                                    "type": "Frame",
                                                    "width": "3dp",
                                                    "height": "200dp",
                                                    "backgroundColor": "#000000",
                                                    "position": "absolute",
                                                    "top": "130dp",
                                                    "right": "210dp"
                                                },

                                                # FASE 3 (ABAJO DERECHA)
                                                {
                                                    "type": "TouchWrapper",
                                                    "onPress": {
                                                        "type": "SendEvent",
                                                        "arguments": ["fase3"]
                                                    },
                                                    "item": {
                                                        "type": "Frame",
                                                        "width": "200dp",
                                                        "height": "90dp",
                                                        "backgroundColor": "#E58AC0",
                                                        "borderRadius": "30dp",
                                                        "position": "absolute",
                                                        "bottom": "80dp",
                                                        "right": "120dp",
                                                        "items": [
                                                            {
                                                                "type": "Container",
                                                                "width": "100%",
                                                                "height": "100%",
                                                                "justifyContent": "center",
                                                                "alignItems": "center",
                                                                "items": [
                                                                    {
                                                                        "type": "Text",
                                                                        "text": "FASE 3",
                                                                        "fontSize": "22dp",
                                                                        "color": "#FFFFFF",
                                                                        "textAlign": "center",
                                                                        "width": "100%"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                },

                                                # LINEA INFERIOR
                                                {
                                                    "type": "Frame",
                                                    "width": "500dp",
                                                    "height": "3dp",
                                                    "backgroundColor": "#000000",
                                                    "position": "absolute",
                                                    "bottom": "120dp",
                                                    "left": "320dp"
                                                },

                                                # FASE 4 (ABAJO IZQUIERDA)
                                                {
                                                    "type": "TouchWrapper",
                                                    "onPress": {
                                                        "type": "SendEvent",
                                                        "arguments": ["fase4"]
                                                    },
                                                    "item": {
                                                        "type": "Frame",
                                                        "width": "200dp",
                                                        "height": "90dp",
                                                        "backgroundColor": "#F4B04E",
                                                        "borderRadius": "30dp",
                                                        "position": "absolute",
                                                        "bottom": "80dp",
                                                        "left": "120dp",
                                                        "items": [
                                                            {
                                                                "type": "Container",
                                                                "width": "100%",
                                                                "height": "100%",
                                                                "justifyContent": "center",
                                                                "alignItems": "center",
                                                                "items": [
                                                                    {
                                                                        "type": "Text",
                                                                        "text": "FASE 4",
                                                                        "fontSize": "22dp",
                                                                        "color": "#FFFFFF",
                                                                        "textAlign": "center",
                                                                        "width": "100%"
                                                                    }
                                                                ]
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
            ]
        }
    }