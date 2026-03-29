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
                    "items": [
                        {
                            "type": "Text",
                            "text": "Asistente C",
                            "fontSize": "60dp",
                            "horizontalAlignment": "center"
                        },
                        {
                            "type": "TouchWrapper",
                            "onPress": {
                                "type": "SendEvent",
                                "arguments": ["musica"]
                            },
                            "item": {
                                "type": "Text",
                                "text": "🎵 Música",
                                "fontSize": "40dp"
                            }
                        },
                        {
                            "type": "TouchWrapper",
                            "onPress": {
                                "type": "SendEvent",
                                "arguments": ["aprender"]
                            },
                            "item": {
                                "type": "Text",
                                "text": "📘 Aprender",
                                "fontSize": "40dp"
                            }
                        }
                    ]
                }
            ]
        }
    }