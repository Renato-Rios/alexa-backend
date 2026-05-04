import os
import psycopg2

def get_connection():
    database_url = os.environ.get("postgresql://admin:HGjBPcY5YLIWaVtBNzWsvtmns6NAO8fN@dpg-d7klgul7vvec73cebok0-a.oregon-postgres.render.com/asistentec")  # ponlo en Render y en local
    return psycopg2.connect(database_url)