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
                    "paddingLeft": "20dp",
                    "paddingRight": "20dp",
                    "paddingTop": "20dp",
                    "items": [

                        # 🔥 TÍTULO
                        {
                            "type": "Text",
                            "text": "🎓 Asistente C",
                            "fontSize": "50dp",
                            "color": "white"
                        },

                        # 📚 SUBTÍTULO
                        {
                            "type": "Text",
                            "text": "Aprendizaje",
                            "fontSize": "30dp",
                            "marginTop": "20dp",
                            "color": "#AAAAAA"
                        },

                        # 🎬 CARRUSEL
                        {
                            "type": "Sequence",
                            "scrollDirection": "horizontal",
                            "data": [
                                {"titulo": "Matemáticas", "accion": "mate"},
                                {"titulo": "Lenguaje", "accion": "lenguaje"},
                                {"titulo": "Memoria", "accion": "memoria"},
                                {"titulo": "Juegos", "accion": "juegos"}
                            ],
                            "items": {
                                "type": "TouchWrapper",
                                "onPress": {
                                    "type": "SendEvent",
                                    "arguments": ["${data.accion}"]
                                },
                                "item": {
                                    "type": "Container",
                                    "width": "250dp",
                                    "height": "150dp",
                                    "marginRight": "15dp",
                                    "backgroundColor": "#1f1f1f",
                                    "borderRadius": "12dp",
                                    "padding": "10dp",
                                    "items": [
                                        {
                                            "type": "Text",
                                            "text": "${data.titulo}",
                                            "color": "white",
                                            "fontSize": "25dp"
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