def pantalla_principal():
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
                    "justifyContent": "center",
                    "alignItems": "center",
                    "items": [
                        {
                            "type": "Frame",
                            "width": "100%",
                            "height": "100%",
                            "backgroundColor": "#FDF0D5",
                            "items": [
                                {
                                    "type": "Container",
                                    "direction": "column",
                                    "width": "100%",
                                    "height": "100%",
                                    "justifyContent": "center",
                                    "alignItems": "center",
                                    "items": [

                                        {
                                            "type": "Text",
                                            "text": "Asistente C",
                                            "fontSize": "60dp",
                                            "color": "#303030",
                                            "marginBottom": "40dp"
                                        },

                                        {
                                            "type": "Container",
                                            "direction": "row",
                                            "justifyContent": "spaceEvenly",
                                            "width": "100%",
                                            "items": [

                                                {
                                                    "type": "TouchWrapper",
                                                    "onPress": {
                                                        "type": "SendEvent",
                                                        "arguments": ["aprender"]
                                                    },
                                                    "item": {
                                                        "type": "Frame",
                                                        "width": "40%",
                                                        "height": "140dp",
                                                        "backgroundColor": "#003049",
                                                        "borderRadius": "25dp",
                                                        "justifyContent": "center",
                                                        "alignItems": "center",
                                                        "items": [
                                                            {
                                                                "type": "Text",
                                                                "text": "Aprender",
                                                                "fontSize": "26dp",
                                                                "color": "white"
                                                            }
                                                        ]
                                                    }
                                                },

                                                {
                                                    "type": "TouchWrapper",
                                                    "onPress": {
                                                        "type": "SendEvent",
                                                        "arguments": ["musica"]
                                                    },
                                                    "item": {
                                                        "type": "Frame",
                                                        "width": "40%",
                                                        "height": "140dp",
                                                        "backgroundColor": "#780000",
                                                        "borderRadius": "25dp",
                                                        "justifyContent": "center",
                                                        "alignItems": "center",
                                                        "items": [
                                                            {
                                                                "type": "Text",
                                                                "text": "Música",
                                                                "fontSize": "26dp",
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
            ]
        }
    }