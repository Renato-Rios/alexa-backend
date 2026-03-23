import requests

COOKIE = "at-main=Atza|gQBIONw4AwEBAOfd9PhQwslohlzYMyEoTLyF4pMPXB_3Dg5qrS7jVWMyEveTLHaQA9xMAgZDkPSBDrLwuevOZI-756fNC2PkNwykgcadU_lRqe5CrXI8REJZoJEmxp4o0JVNkxI55GZIKgURIYNNL33rfu7PTsNzQtNPhxXn_Z1kvJbIxjNE59k6E5NTdi7Y3If7_Vx8Z7Mef3QdWwGLcYkd3mfFPSpY8lZ2MYENsAqx46Lij0OtcVyAefXqjUbEnzEhIXP_reJArFubylC0AjHsDg7Y9MoyMLKQX-2-TYcwyV75tDthyohkI98278ZuetYlEaalGsJQ82IJPYejPUd4iUKytzKH1g; sess-at-main=L2vNuhhP3Up/WGTrZD9FJWEwu1sVzoSWvcIEQsYSFck=; session-id=139-4813171-6633649; session-token=UL5nmymQpduwmYAeJ0+E55GYmASBJFBsNbiLiV5H65/Gv7DHWkmwNg0S+x9G9gQ3CLcrlQc3GCFbil1U+eKhpm3EuDXZ4kSlaTFNvV7ET4kxqKCfp/zy2TEeYuI6FpD+e3eZnTUAN3dKYFqbPocsU8J81TUT8zYTyYjNKTtWXMcLeEA18z94sLSfRamwxkKosKVQ6RqHqM37yviA9Q28AT2Capplo5JHeMFmHf5ZZaMOXuti4CXwGtQfx5bOkaC2; sst-main=Sst1|PQKWcsGGMJ_OT9CWG230A2aSCQfQQfkfhx4KanOXretgH-Fg9I-Xu04G85hjOfmn7anCIsTvmaXjhQbAn7JfvOIFMRG4YO160McZNlnV_1BAD7c2DBaa_fe5AbwewskkkJgUubnXd35Vi-l7IFWKmoTvqwLsvJcwMBHfGJtk4NaPVqWw2AwZwGpcIw58mvC6dM1LhS_LZBvtAbhHS3PVEJXtKxMAjQlgRFsnXdKFHeqN6tk_UqhhBAcJWtGACfGhIzJVaHcY2PoimeL4crIG0XSnKfqZb2rvWFQzHgAK44G1lY8; ubid-main=135-6720884-2739651; x-main=c@ZMv@nZatRX9aAmkKij9LEDr3@N?rfcgWm8NGl@uIKFqZ?G2rUNYLHlICFra5Lg;"

def alexa_hablar(texto):
    url = "https://alexa.amazon.com/api/behaviors/preview"

    headers = {
        "Content-Type": "application/json",
        "Cookie": COOKIE,
        "Origin": "https://alexa.amazon.com",
        "Referer": "https://alexa.amazon.com/",
    }

    data = {
        "behaviorId": "PREVIEW",
        "sequenceJson": f'''
        {{
            "type": "Alexa.Speak",
            "payload": {{
                "type": "text",
                "textToSpeak": "{texto}"
            }}
        }}
        ''',
        "status": "ENABLED"
    }

    r = requests.post(url, headers=headers, json=data)

    print("Status:", r.status_code)
    print("Respuesta:", r.text)


alexa_hablar("Hola Renato, esto ya funciona")