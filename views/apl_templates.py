def pantalla_principal():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    # 👇 ESTE SÍ ES EL CONTENEDOR PRINCIPAL
                    "type": "Container",
                    "direction": "column",
                    "width": "100%",
                    "height": "100%",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "backgroundColor": "#FDF0D5",

                    "items": [

                        # 🔤 TÍTULO
                        {
                            "type": "Text",
                            "text": "Asistente C",
                            "fontSize": "60dp",
                            "color": "#003049",
                            "textAlign": "center",
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
                                "width": "60%",   # 🔥 RESPONSIVE
                                "height": "120dp",
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
                                "width": "60%",
                                "height": "120dp",
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
    }