def music_gui():
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
                            "backgroundColor": "#780000",
                            "items": [
                                {
                                    # BORDE
                                    "type": "Frame",
                                    "width": "90%",
                                    "height": "85%",
                                    "borderWidth": "3dp",
                                    "borderColor": "#FFFFFF",
                                    "alignSelf": "center",
                                    "alignItems": "center",

                                    "items": [

                                        {
                                            "type": "Container",
                                            "height": "40dp"
                                        },

                                        # TITULO
                                        {
                                            "type": "Frame",
                                            "width": "70%",
                                            "height": "70dp",
                                            "backgroundColor": "#E6E6E6",
                                            "borderRadius": "40dp",
                                            "justifyContent": "center",
                                            "alignItems": "center",
                                            "items": [
                                                {
                                                    "type": "Text",
                                                    "text": "CALMA TU ALMA CON UN POCO DE MÚSICA",
                                                    "fontSize": "26dp",
                                                    "color": "#000000",
                                                    "textAlign": "center",
                                                    "width": "90%"
                                                }
                                            ]
                                        },

                                        {
                                            "type": "Container",
                                            "height": "50dp"
                                        },

                                        # CONTENEDOR PRINCIPAL
                                        {
                                            "type": "Container",
                                            "direction": "row",
                                            "justifyContent": "space-around",
                                            "width": "100%",
                                            "items": [

                                                # 🔴 DISCO 1
                                                {
                                                    "type": "Container",
                                                    "direction": "column",
                                                    "alignItems": "center",
                                                    "items": [

                                                        # CIRCULO GRANDE
                                                        {
                                                            "type": "Frame",
                                                            "width": "180dp",
                                                            "height": "180dp",
                                                            "backgroundColor": "#E6E6E6",
                                                            "borderRadius": "90dp",
                                                            "justifyContent": "center",
                                                            "alignItems": "center",
                                                            "items": [

                                                                # CENTRO NEGRO
                                                                {
                                                                    "type": "Frame",
                                                                    "width": "60dp",
                                                                    "height": "60dp",
                                                                    "backgroundColor": "#000000",
                                                                    "borderRadius": "30dp"
                                                                }

                                                            ]
                                                        },

                                                        # BOTON
                                                        {
                                                            "type": "TouchWrapper",
                                                            "onPress": {"type": "SendEvent","arguments": ["playlist_mama"]},
                                                            "item": {
                                                                "type": "Frame",
                                                                "width": "180dp",
                                                                "height": "50dp",
                                                                "backgroundColor": "#CFE3E8",
                                                                "borderRadius": "25dp",
                                                                "marginTop": "20dp",
                                                                "items": [{
                                                                    "type": "Container",
                                                                    "width": "100%",
                                                                    "height": "100%",
                                                                    "justifyContent": "center",
                                                                    "alignItems": "center",
                                                                    "items": [{
                                                                        "type": "Text",
                                                                        "text": "PLAYLIST MAMÁ",
                                                                        "fontSize": "18dp",
                                                                        "color": "#0E5678",
                                                                        "width": "100%",
                                                                        "textAlign": "center"
                                                                    }]
                                                                }]
                                                            }
                                                        }
                                                    ]
                                                },

                                                # 🔴 DISCO 2
                                                {
                                                    "type": "Container",
                                                    "direction": "column",
                                                    "alignItems": "center",
                                                    "items": [

                                                        {
                                                            "type": "Frame",
                                                            "width": "180dp",
                                                            "height": "180dp",
                                                            "backgroundColor": "#E6E6E6",
                                                            "borderRadius": "90dp",
                                                            "justifyContent": "center",
                                                            "alignItems": "center",
                                                            "items": [
                                                                {
                                                                    "type": "Frame",
                                                                    "width": "60dp",
                                                                    "height": "60dp",
                                                                    "backgroundColor": "#000000",
                                                                    "borderRadius": "30dp"
                                                                }
                                                            ]
                                                        },

                                                        {
                                                            "type": "TouchWrapper",
                                                            "onPress": {"type": "SendEvent","arguments": ["playlist_renato"]},
                                                            "item": {
                                                                "type": "Frame",
                                                                "width": "180dp",
                                                                "height": "50dp",
                                                                "backgroundColor": "#CFE3E8",
                                                                "borderRadius": "25dp",
                                                                "marginTop": "20dp",
                                                                "items": [{
                                                                    "type": "Container",
                                                                    "width": "100%",
                                                                    "height": "100%",
                                                                    "justifyContent": "center",
                                                                    "alignItems": "center",
                                                                    "items": [{
                                                                        "type": "Text",
                                                                        "text": "PLAYLIST RENATO",
                                                                        "fontSize": "18dp",
                                                                        "color": "#0E5678",
                                                                        "width": "100%",
                                                                        "textAlign": "center"
                                                                    }]
                                                                }]
                                                            }
                                                        }
                                                    ]
                                                },

                                                # 🔴 DISCO 3
                                                {
                                                    "type": "Container",
                                                    "direction": "column",
                                                    "alignItems": "center",
                                                    "items": [

                                                        {
                                                            "type": "Frame",
                                                            "width": "180dp",
                                                            "height": "180dp",
                                                            "backgroundColor": "#E6E6E6",
                                                            "borderRadius": "90dp",
                                                            "justifyContent": "center",
                                                            "alignItems": "center",
                                                            "items": [
                                                                {
                                                                    "type": "Frame",
                                                                    "width": "60dp",
                                                                    "height": "60dp",
                                                                    "backgroundColor": "#000000",
                                                                    "borderRadius": "30dp"
                                                                }
                                                            ]
                                                        },

                                                        {
                                                            "type": "TouchWrapper",
                                                            "onPress": {"type": "SendEvent","arguments": ["playlist_oliver"]},
                                                            "item": {
                                                                "type": "Frame",
                                                                "width": "180dp",
                                                                "height": "50dp",
                                                                "backgroundColor": "#CFE3E8",
                                                                "borderRadius": "25dp",
                                                                "marginTop": "20dp",
                                                                "items": [{
                                                                    "type": "Container",
                                                                    "width": "100%",
                                                                    "height": "100%",
                                                                    "justifyContent": "center",
                                                                    "alignItems": "center",
                                                                    "items": [{
                                                                        "type": "Text",
                                                                        "text": "PLAYLIST OLIVER",
                                                                        "fontSize": "18dp",
                                                                        "color": "#0E5678",
                                                                        "width": "100%",
                                                                        "textAlign": "center"
                                                                    }]
                                                                }]
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
            ]
        }
    }