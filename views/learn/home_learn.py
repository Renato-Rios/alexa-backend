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
                            # FONDO
                            "type": "Frame",
                            "width": "100%",
                            "height": "100%",
                            "backgroundColor": "#003049",
                            "items": [
                                {
                                    # CONTENEDOR GENERAL
                                    "type": "Container",
                                    "direction": "column",
                                    "width": "100%",
                                    "height": "100%",
                                    "alignItems": "center",

                                    "items": [

                                        # 🔷 TITULO SUPERIOR
                                        {
                                            "type": "Frame",
                                            "width": "60%",
                                            "height": "70dp",
                                            "backgroundColor": "#005B8D",
                                            "borderRadius": "40dp",
                                            "justifyContent": "center",
                                            "alignItems": "center",
                                            "marginTop": "30dp",
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

                                        # 🔷 CONTENEDOR CENTRAL (IZQ - DER)
                                        {
                                            "type": "Container",
                                            "direction": "row",
                                            "width": "100%",
                                            "height": "100%",
                                            "justifyContent": "space-between",
                                            "alignItems": "center",
                                            "paddingLeft": "80dp",
                                            "paddingRight": "80dp",

                                            "items": [

                                                # 🔷 LADO IZQUIERDO
                                                {
                                                    "type": "Container",
                                                    "direction": "column",
                                                    "alignItems": "center",
                                                    "justifyContent": "center",
                                                    "items": [

                                                        # BOTON FASE 1
                                                        {
                                                            "type": "TouchWrapper",
                                                            "onPress": {
                                                                "type": "SendEvent",
                                                                "arguments": ["fase1"]
                                                            },
                                                            "item": {
                                                                "type": "Frame",
                                                                "width": "220dp",
                                                                "height": "90dp",
                                                                "backgroundColor": "#0E6F7C",
                                                                "borderRadius": "30dp",
                                                                "marginBottom": "20dp",
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
                                                                                "fontSize": "24dp",
                                                                                "color": "#FFFFFF",
                                                                                "textAlign": "center",
                                                                                "width": "100%"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        },

                                                        # LINEA (SIMULADA)
                                                        {
                                                            "type": "Frame",
                                                            "width": "2dp",
                                                            "height": "40dp",
                                                            "backgroundColor": "#FFFFFF"
                                                        },

                                                        # BOTON FASE 2
                                                        {
                                                            "type": "TouchWrapper",
                                                            "onPress": {
                                                                "type": "SendEvent",
                                                                "arguments": ["fase2"]
                                                            },
                                                            "item": {
                                                                "type": "Frame",
                                                                "width": "220dp",
                                                                "height": "90dp",
                                                                "backgroundColor": "#C2D63E",
                                                                "borderRadius": "30dp",
                                                                "marginTop": "20dp",
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
                                                                                "fontSize": "24dp",
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
                                                },

                                                # 🔷 LADO DERECHO
                                                {
                                                    "type": "Container",
                                                    "direction": "column",
                                                    "alignItems": "center",
                                                    "justifyContent": "center",
                                                    "items": [

                                                        # BOTON FASE 3
                                                        {
                                                            "type": "TouchWrapper",
                                                            "onPress": {
                                                                "type": "SendEvent",
                                                                "arguments": ["fase3"]
                                                            },
                                                            "item": {
                                                                "type": "Frame",
                                                                "width": "220dp",
                                                                "height": "90dp",
                                                                "backgroundColor": "#E58AC0",
                                                                "borderRadius": "30dp",
                                                                "marginBottom": "20dp",
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
                                                                                "fontSize": "24dp",
                                                                                "color": "#FFFFFF",
                                                                                "textAlign": "center",
                                                                                "width": "100%"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        },

                                                        # LINEA
                                                        {
                                                            "type": "Frame",
                                                            "width": "2dp",
                                                            "height": "40dp",
                                                            "backgroundColor": "#FFFFFF"
                                                        },

                                                        # BOTON FASE 4
                                                        {
                                                            "type": "TouchWrapper",
                                                            "onPress": {
                                                                "type": "SendEvent",
                                                                "arguments": ["fase4"]
                                                            },
                                                            "item": {
                                                                "type": "Frame",
                                                                "width": "220dp",
                                                                "height": "90dp",
                                                                "backgroundColor": "#F4B04E",
                                                                "borderRadius": "30dp",
                                                                "marginTop": "20dp",
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
                                                                                "fontSize": "24dp",
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
            ]
        }
    }