def learn_gui():
    return {
        "type": "APL",
        "version": "1.7",
        "mainTemplate": {
            "parameters": ["payload"],
            "items": [
                {
                    # FONDO (AZUL CLARO)
                    "type": "Frame",
                    "width": "100%",
                    "height": "100%",
                    "backgroundColor": "#9DB4CF",
                    "item": {
                        # CONTENEDOR GENERAL (Columna)
                        "type": "Container",
                        "direction": "column",
                        "width": "100%",
                        "height": "100%",
                        "alignItems": "center",
                        "items": [

                            # 🔷 ESPACIO SUPERIOR (BAJA EL TITULO)
                            {
                                "type": "Container",
                                "height": "70dp" # Mantengo tu espacio estético
                            },

                            # 🔷 TITULO
                            {
                                "type": "Frame",
                                "width": "60%",
                                "height": "70dp",
                                "backgroundColor": "#0E5678",
                                "borderRadius": "40dp",
                                "items": [{
                                    "type": "Text",
                                    "text": "¡APRENDE CON ASISTENTE C!",
                                    "fontSize": "28dp",
                                    "color": "#FFFFFF",
                                    "textAlign": "center",
                                    "textAlignVertical": "center", # Centrado vertical
                                    "width": "100%",
                                    "height": "100%"
                                }]
                            },

                            # 🔷 CONTENEDOR INTERMEDIO (LA CLAVE DE LA SOLUCIÓN)
                            {
                                "type": "Container",
                                "grow": 1, # <--- Ocupa todo el espacio sobrante
                                "justifyContent": "center", # <--- Centra el diagrama verticalmente aquí
                                "width": "100%",
                                "items": [
                                    # Aquí dentro va tu diagrama original tal cual
                                    {
                                        # 🔷 CONTENIDO PRINCIPAL (EL DIAGRAMA)
                                        "type": "Container",
                                        "direction": "row",
                                        "width": "100%",
                                        # "height": "100%", # <--- ELIMINADO: Esto causaba el error
                                        "justifyContent": "space-between",
                                        "alignItems": "center",
                                        "paddingLeft": "80dp",
                                        "paddingRight": "80dp",
                                        "items": [

                                            # 🔷 LADO IZQUIERDO
                                            {
                                                "type": "Container",
                                                "direction": "column",
                                                "alignItems": "center",
                                                "items": [
                                                    # FASE 1
                                                    {"type": "TouchWrapper", "onPress": {"type": "SendEvent", "arguments": ["fase1"]}, "item": {"type": "Frame", "width": "220dp", "height": "90dp", "backgroundColor": "#0E6F7C", "borderRadius": "30dp", "marginBottom": "20dp", "items": [{"type": "Text", "text": "FASE 1", "fontSize": "24dp", "color": "#FFFFFF", "textAlign": "center", "textAlignVertical": "center", "width": "100%", "height": "100%"}]}},
                                                    
                                                    # 🔷 LINEA ESTÉTICA 1
                                                    {"type": "Frame", "width": "2dp", "height": "40dp", "backgroundColor": "#000000"},
                                                    
                                                    # FASE 2
                                                    {"type": "TouchWrapper", "onPress": {"type": "SendEvent", "arguments": ["fase2"]}, "item": {"type": "Frame", "width": "220dp", "height": "90dp", "backgroundColor": "#C2D63E", "borderRadius": "30dp", "marginTop": "20dp", "items": [{"type": "Text", "text": "FASE 2", "fontSize": "24dp", "color": "#FFFFFF", "textAlign": "center", "textAlignVertical": "center", "width": "100%", "height": "100%"}]}}
                                                ]
                                            },

                                            # 🔷 LINEA CENTRAL CONECTORA (Añadida para estética de flecha horizontal)
                                            {"type": "Frame", "width": "grow", "height": "2dp", "backgroundColor": "#000000", "marginLeft": "20dp", "marginRight": "20dp"},

                                            # 🔷 LADO DERECHO
                                            {
                                                "type": "Container",
                                                "direction": "column",
                                                "alignItems": "center",
                                                "items": [
                                                    # FASE 3
                                                    {"type": "TouchWrapper", "onPress": {"type": "SendEvent", "arguments": ["fase3"]}, "item": {"type": "Frame", "width": "220dp", "height": "90dp", "backgroundColor": "#E58AC0", "borderRadius": "30dp", "marginBottom": "20dp", "items": [{"type": "Text", "text": "FASE 3", "fontSize": "24dp", "color": "#FFFFFF", "textAlign": "center", "textAlignVertical": "center", "width": "100%", "height": "100%"}]}},
                                                    
                                                    # 🔷 LINEA ESTÉTICA 2
                                                    {"type": "Frame", "width": "2dp", "height": "40dp", "backgroundColor": "#000000"},
                                                    
                                                    # FASE 4
                                                    {"type": "TouchWrapper", "onPress": {"type": "SendEvent", "arguments": ["fase4"]}, "item": {"type": "Frame", "width": "220dp", "height": "90dp", "backgroundColor": "#F4B04E", "borderRadius": "30dp", "marginTop": "20dp", "items": [{"type": "Text", "text": "FASE 4", "fontSize": "24dp", "color": "#FFFFFF", "textAlign": "center", "textAlignVertical": "center", "width": "100%", "height": "100%"}]}}
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    }