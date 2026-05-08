def fase_1_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": [
                "payload"
            ],
            "items": [
                {
                    "type": "Container",
                    "width": "100%",
                    "height": "100%",
                    "direction": "column",
                    "items": [
                        {
                            "type": "Frame",
                            "width": "100%",
                            "height": "100%",
                            "backgroundColor": "#003049",
                            "item": {
                                "type": "Container",
                                "width": "100%",
                                "height": "100%",
                                "justifyContent": "center",
                                "alignItems": "center",
                                "items": [
                                    {
                                        "type": "Image",
                                        "source": "${payload.datosFase.image}",
                                        "width": "600dp",
                                        "height": "400dp",
                                        "scale": "best-fit",
                                        "align": "center"
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${payload.datosFase.word}",
                                        "fontSize": "60dp",
                                        "fontWeight": "700",
                                        "color": "#FFFFFF",
                                        "textAlign": "center",
                                        "marginTop": "20dp"
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${payload.datosFase.phonetic}",
                                        "fontSize": "35dp",
                                        "color": "#CCCCCC",
                                        "fontStyle": "italic",
                                        "textAlign": "center",
                                        "marginTop": "10dp"
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }
    }