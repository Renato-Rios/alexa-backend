def learn_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    "type": "Container",
                    "width": "100%",
                    "height": "100%",
                    "items": [
                        {
                            # FONDO
                            "type": "Frame",
                            "width": "100%",
                            "height": "100%",
                            "backgroundColor": "#9DB4CF",
                            "items": [
                                {
                                    "type": "Container",
                                    "width": "100%",
                                    "height": "100%",
                                    "items": [

                                        # 🔷 TITULO (centrado y más abajo)
                                        {
                                            "type": "Frame",
                                            "width": "60%",
                                            "height": "70dp",
                                            "backgroundColor": "#0E5678",
                                            "borderRadius": "40dp",
                                            "justifyContent": "center",
                                            "alignItems": "center",
                                            "position": "absolute",
                                            "top": "60dp",
                                            "alignSelf": "center",
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

                                        # 🔷 FASE 1 (ARRIBA IZQUIERDA)
                                        {
                                            "type": "TouchWrapper",
                                            "onPress": {"type": "SendEvent", "arguments": ["fase1"]},
                                            "item": {
                                                "type": "Frame",
                                                "width": "200dp",
                                                "height": "90dp",
                                                "backgroundColor": "#0E6F7C",
                                                "borderRadius": "30dp",
                                                "position": "absolute",
                                                "top": "180dp",
                                                "left": "120dp",
                                                "items": [{
                                                    "type": "Container",
                                                    "width": "100%",
                                                    "height": "100%",
                                                    "justifyContent": "center",
                                                    "alignItems": "center",
                                                    "items": [{
                                                        "type": "Text",
                                                        "text": "FASE 1",
                                                        "fontSize": "22dp",
                                                        "color": "#FFFFFF",
                                                        "width": "100%",
                                                        "textAlign": "center"
                                                    }]
                                                }]
                                            }
                                        },

                                        # 🔷 FASE 2 (ARRIBA DERECHA)
                                        {
                                            "type": "TouchWrapper",
                                            "onPress": {"type": "SendEvent", "arguments": ["fase2"]},
                                            "item": {
                                                "type": "Frame",
                                                "width": "200dp",
                                                "height": "90dp",
                                                "backgroundColor": "#C2D63E",
                                                "borderRadius": "30dp",
                                                "position": "absolute",
                                                "top": "180dp",
                                                "right": "120dp",
                                                "items": [{
                                                    "type": "Container",
                                                    "width": "100%",
                                                    "height": "100%",
                                                    "justifyContent": "center",
                                                    "alignItems": "center",
                                                    "items": [{
                                                        "type": "Text",
                                                        "text": "FASE 2",
                                                        "fontSize": "22dp",
                                                        "color": "#FFFFFF",
                                                        "width": "100%",
                                                        "textAlign": "center"
                                                    }]
                                                }]
                                            }
                                        },

                                        # 🔷 FASE 3 (ABAJO DERECHA)
                                        {
                                            "type": "TouchWrapper",
                                            "onPress": {"type": "SendEvent", "arguments": ["fase3"]},
                                            "item": {
                                                "type": "Frame",
                                                "width": "200dp",
                                                "height": "90dp",
                                                "backgroundColor": "#E58AC0",
                                                "borderRadius": "30dp",
                                                "position": "absolute",
                                                "bottom": "120dp",
                                                "right": "120dp",
                                                "items": [{
                                                    "type": "Container",
                                                    "width": "100%",
                                                    "height": "100%",
                                                    "justifyContent": "center",
                                                    "alignItems": "center",
                                                    "items": [{
                                                        "type": "Text",
                                                        "text": "FASE 3",
                                                        "fontSize": "22dp",
                                                        "color": "#FFFFFF",
                                                        "width": "100%",
                                                        "textAlign": "center"
                                                    }]
                                                }]
                                            }
                                        },

                                        # 🔷 FASE 4 (ABAJO IZQUIERDA)
                                        {
                                            "type": "TouchWrapper",
                                            "onPress": {"type": "SendEvent", "arguments": ["fase4"]},
                                            "item": {
                                                "type": "Frame",
                                                "width": "200dp",
                                                "height": "90dp",
                                                "backgroundColor": "#F4B04E",
                                                "borderRadius": "30dp",
                                                "position": "absolute",
                                                "bottom": "120dp",
                                                "left": "120dp",
                                                "items": [{
                                                    "type": "Container",
                                                    "width": "100%",
                                                    "height": "100%",
                                                    "justifyContent": "center",
                                                    "alignItems": "center",
                                                    "items": [{
                                                        "type": "Text",
                                                        "text": "FASE 4",
                                                        "fontSize": "22dp",
                                                        "color": "#FFFFFF",
                                                        "width": "100%",
                                                        "textAlign": "center"
                                                    }]
                                                }]
                                            }
                                        },

                                        # 🔷 LINEA SUPERIOR
                                        {
                                            "type": "Frame",
                                            "width": "520dp",
                                            "height": "3dp",
                                            "backgroundColor": "#000000",
                                            "position": "absolute",
                                            "top": "225dp",
                                            "left": "320dp"
                                        },

                                        # 🔷 LINEA DERECHA
                                        {
                                            "type": "Frame",
                                            "width": "3dp",
                                            "height": "220dp",
                                            "backgroundColor": "#000000",
                                            "position": "absolute",
                                            "top": "260dp",
                                            "right": "220dp"
                                        },

                                        # 🔷 LINEA INFERIOR
                                        {
                                            "type": "Frame",
                                            "width": "520dp",
                                            "height": "3dp",
                                            "backgroundColor": "#000000",
                                            "position": "absolute",
                                            "bottom": "160dp",
                                            "left": "320dp"
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