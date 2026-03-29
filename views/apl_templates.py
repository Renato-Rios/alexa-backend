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
                    "backgroundColor": "#0f0f0f",

                    "items": [

                        # 🎓 TÍTULO
                        {
                            "type": "Text",
                            "text": "Asistente C",
                            "fontSize": "50dp",
                            "color": "white",
                            "textAlign": "center"
                        },

                        # 📚 SUBTÍTULO
                        {
                            "type": "Text",
                            "text": "Desliza →",
                            "fontSize": "25dp",
                            "color": "#888",
                            "marginTop": "10dp"
                        },

                        # 🎬 CARRUSEL
                        {
                            "type": "Sequence",
                            "scrollDirection": "horizontal",
                            "height": "200dp",
                            "width": "80%",  # 🔥 controla el ancho del carrusel
                            "marginTop": "30dp",

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
                                    "width": "280dp",
                                    "height": "180dp",
                                    "marginRight": "20dp",
                                    "backgroundColor": "#1f1f1f",
                                    "borderRadius": "20dp",

                                    "items": [
                                        {
                                            "type": "Text",
                                            "text": "${data.titulo}",
                                            "color": "white",
                                            "fontSize": "28dp",
                                            "textAlign": "center",
                                            "height": "100%",
                                            "verticalAlignment": "center"
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