def fase_1_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    # CONTENEDOR PRINCIPAL (layout)
                    "type": "Container",
                    "width": "100%",
                    "height": "100%",
                    "justifyContent": "center",
                    "alignItems": "center",
                    
                    "items": [
                        {
                            # FRAME = FONDO REAL
                            "type": "Frame",
                            "width": "100%",
                            "height": "100%",
                            "backgroundColor": "#003049",

                            "items": [
                                {
                                    # CONTENIDO CENTRADO
                                    "type": "Container",
                                    "direction": "column",
                                    "width": "100%",
                                    "height": "100%",
                                    "justifyContent": "center",
                                    "alignItems": "center",

                                    "items": [

                                        # TÍTULO
                                        {
                                            "type": "Text",
                                            "text": "Fase 1",
                                            "fontSize": "60dp",
                                            "color": "#1B1B1C",
                                            "marginBottom": "40dp"
                                        },
                                        #imagen
                                        {
                                            "type": "Image",
                                            "source": "${payload.image}",
                                            "width": "300dp",
                                            "height": "300dp",
                                            "scale": "best-fill",
                                            "marginBottom": "30dp"
                                        },
                                        #palabra
                                        {
                                            "type": "Text",
                                            "text": "${payload.word}",
                                            "fontSize": "50dp",
                                            "color": "#FFFFFF",
                                            "textAlign": "center"
                                        },
                                        
                                        #fonetica
                                        {
                                            "type": "Text",
                                            "text": "${payload.phonetic}",
                                            "fontSize": "30dp",
                                            "color": "#CCCCCC",
                                            "marginTop": "20dp",
                                            "textAlign": "center"
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
