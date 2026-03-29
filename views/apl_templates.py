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
                    "backgroundColor": "#0f0f0f",
                    "paddingLeft": "30dp",
                    "paddingRight": "30dp",
                    "paddingTop": "20dp",
                    "items": [

                        # 🎓 TÍTULO
                        {
                            "type": "Text",
                            "text": "Asistente C",
                            "fontSize": "50dp",
                            "color": "white"
                        },

                        # 📚 SUBTÍTULO
                        {
                            "type": "Text",
                            "text": "Desliza →",
                            "fontSize": "25dp",
                            "color": "#888888",
                            "marginTop": "10dp"
                        },

                        # 🎬 CARRUSEL MEJORADO
                        {
                            "type": "Sequence",
                            "scrollDirection": "horizontal",
                            "height": "200dp",
                            "marginTop": "20dp",
                            "data": [
                                {"titulo": "Matemáticas", "accion": "mate"},
                                {"titulo": "Lenguaje", "accion": "lenguaje"},
                                {"titulo": "Memoria", "accion": "memoria"},
                                {"titulo": "Música", "accion": "musica"}
                            ],
                            "items": {
                                "type": "TouchWrapper",
                                "onPress": {
                                    "type": "SendEvent",
                                    "arguments": ["${data.accion}"]
                                },
                                "item": {
                                    "type": "Container",
                                    "width": "300dp",
                                    "height": "180dp",
                                    "marginRight": "20dp",
                                    "backgroundColor": "#1f1f1f",
                                    "borderRadius": "20dp",
                                    "items": [
                                        {
                                            "type": "Text",
                                            "text": "${data.titulo}",
                                            "color": "white",
                                            "fontSize": "30dp",
                                            "horizontalAlignment": "center",
                                            "verticalAlignment": "center",
                                            "height": "100%"
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            ]
        }
    }