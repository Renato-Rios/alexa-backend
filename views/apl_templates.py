def pantalla_principal():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    # 🔹 CONTENEDOR PRINCIPAL (layout)
                    "type": "Container",
                    "width": "100%",
                    "height": "100%",
                    "justifyContent": "center",
                    "alignItems": "center",

                    "items": [
                        {
                            # 🔥 FRAME = FONDO REAL
                            "type": "Frame",
                            "width": "100%",
                            "height": "100%",
                            "backgroundColor": "#FDF0D5",

                            "items": [
                                {
                                    # 🔹 CONTENIDO CENTRADO
                                    "type": "Container",
                                    "direction": "column",
                                    "width": "100%",
                                    "height": "100%",
                                    "justifyContent": "center",
                                    "alignItems": "center",

                                    "items": [

                                        # 🎓 TÍTULO
                                        {
                                            "type": "Text",
                                            "text": "Asistente C",
                                            "fontSize": "60dp",
                                            "color": "#303030",
                                            "marginBottom": "40dp"
                                        },

                                        # 📘 BOTÓN APRENDER
                                        {
                                            "type": "TouchWrapper",
                                            "onPress": {
                                                "type": "SendEvent",
                                                "arguments": ["aprender"]
                                            },
                                            "item": {
                                                "type": "Frame",
                                                "width": "70%",
                                                "height": "60dp",
                                                "backgroundColor": "#003049",
                                                "borderRadius": "25dp",
                                                "justifyContent": "center",
                                                "alignItems": "center",

                                                "items": [
                                                    {
                                                        "type": "Text",
                                                        "text": "Aprender",
                                                        "fontSize": "30dp",
                                                        "color": "white"
                                                    }
                                                ]
                                            }
                                        },

                                        # 🎵 BOTÓN MÚSICA
                                        {
                                            "type": "TouchWrapper",
                                            "onPress": {
                                                "type": "SendEvent",
                                                "arguments": ["musica"]
                                            },
                                            "item": {
                                                "type": "Frame",
                                                "width": "70%",
                                                "height": "60dp",
                                                "marginTop": "30dp",
                                                "backgroundColor": "#780000",
                                                "borderRadius": "25dp",
                                                "justifyContent": "center",
                                                "alignItems": "center",

                                                "items": [
                                                    {
                                                        "type": "Text",
                                                        "text": "Música",
                                                        "fontSize": "30dp",
                                                        "color": "white"
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