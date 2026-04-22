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
                                            "fontSize": "55dp",
                                            "color": "#303030",
                                            "fontFamily": "Amazon Ember Display",
                                            "marginBottom": "50dp"
                                        },

                                        {
                                            "type": "Container",
                                            "direction": "row",
                                            "justifyContent": "center",
                                            "alignItems": "center",
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
                                                        "width": "240dp",
                                                        "height": "140dp",
                                                        "backgroundColor": "#003049",
                                                        "borderRadius": "25dp",
                                                        "justifyContent": "center",
                                                        "alignItems": "center",
                                                        "marginRight": "30dp",
                                                        "items": [
                                                            {
                                                                "type": "Text",
                                                                "text": "Aprender",
                                                                "fontSize": "24dp",
                                                                "color": "#FFFFFF",
                                                                "fontFamily": "Amazon Ember",
                                                                "textAlign": "center"
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
                                                        "width": "240dp",
                                                        "height": "140dp",
                                                        "backgroundColor": "#780000",
                                                        "borderRadius": "25dp",
                                                        "justifyContent": "center",
                                                        "alignItems": "center",
                                                        "items": [
                                                            {
                                                                "type": "Text",
                                                                "text": "Música",
                                                                "fontSize": "24dp",
                                                                "color": "#FFFFFF",
                                                                "fontFamily": "Amazon Ember",
                                                                "textAlign": "center"
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