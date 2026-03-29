def pantalla_principal():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    "type": "Container",
                    "direction": "column",
                    "width": "100%",
                    "height": "100%",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "backgroundColor": "#FDF0D5",

                    "items": [

                        # 🎓 TÍTULO
                        {
                            "type": "Text",
                            "text": "Asistente C",
                            "fontSize": "50dp",
                            "color": "white",
                            "textAlign": "center",
                            "marginBottom": "40dp"
                        },

                        #BOTÓN APRENDER (GRANDE)
                        {
                            "type": "TouchWrapper",
                            "onPress": {
                                "type": "SendEvent",
                                "arguments": ["aprender"]
                            },
                            "item": {
                                "type": "Container",
                                "width": "70%",
                                "height": "180dp",
                                "backgroundColor": "#003049",
                                "borderRadius": "25dp",
                                "justifyContent": "center",
                                "alignItems": "center",
                                "shadow": True,

                                "items": [
                                    {
                                        "type": "Text",
                                        "text": "Aprender",
                                        "fontSize": "40dp",
                                        "color": "white",
                                        "textAlign": "center"
                                    }
                                ]
                            }
                        },

                        # BOTÓN MÚSICA (PEQUEÑO)
                        {
                            "type": "TouchWrapper",
                            "onPress": {
                                "type": "SendEvent",
                                "arguments": ["musica"]
                            },
                            "item": {
                                "type": "Container",
                                "width": "50%",
                                "height": "100dp",
                                "marginTop": "30dp",
                                "backgroundColor": "#780000",
                                "borderRadius": "20dp",
                                "justifyContent": "center",
                                "alignItems": "center",

                                "items": [
                                    {
                                        "type": "Text",
                                        "text": "Música",
                                        "fontSize": "28dp",
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