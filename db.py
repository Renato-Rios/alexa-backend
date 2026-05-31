import os
import psycopg2

def get_connection():
    database_url = os.environ.get("postgresql://renato:oXjjvt32e0qErXXoeJtpPKqPlZqAULCz@dpg-d8e7pme8bjmc73asb3p0-a.oregon-postgres.render.com/asistentec_ev22")  # ponlo en Render y en local
    return psycopg2.connect(database_url)