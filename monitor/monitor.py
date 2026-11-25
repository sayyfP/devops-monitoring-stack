import urllib.request
import time
from datetime import datetime

URL = "http://web:80"
LOG_FILE = "/app/logs/health.log"

def check_service():
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        reponse = urllib.request.urlopen(URL, timeout=5)
        message = f"[{horodatage}] [OK] {URL} répond avec le code {reponse.getcode()}\n"
    except Exception as erreur:
        message = f"[{horodatage}] [ERREUR] {URL} inaccessible : {erreur}\n"
    
    print(message.strip(), flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as fichier:
        fichier.write(message)

if __name__ == "__main__":
    print("Démarrage de la sonde de surveillance...", flush=True)
    while True:
        check_service()
        time.sleep(10)
