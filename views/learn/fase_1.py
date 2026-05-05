def fase_1_gui():
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
                            "backgroundColor": "#003049",
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
                                            "type": "Image",
                                            "source": "${payload.datosFase.image}",
                                            "width": "350dp",
                                            "height": "350dp",
                                            "scale": "best-fit",
                                            "align": "center",
                                            "marginBottom": "20dp"
                                        },
                                        {
                                            "type": "Text",
                                            "text": "${payload.datosFase.word}",
                                            "fontSize": "60dp",
                                            "fontWeight": "700",
                                            "color": "#FFFFFF",
                                            "textAlign": "center"
                                        },
                                        {
                                            "type": "Text",
                                            "text": "${payload.datosFase.phonetic}",
                                            "fontSize": "35dp",
                                            "color": "#CCCCCC",
                                            "marginTop": "10dp",
                                            "textAlign": "center",
                                            "fontStyle": "italic"
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