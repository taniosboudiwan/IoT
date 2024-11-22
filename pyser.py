import serial
import time
import json
import pandas as pd

# Remplacez 'COMx' par le port série correspondant à votre Arduino
port = 'COM6'  # Modifiez ce port selon votre système
baud_rate = 115200  # La vitesse de communication (doit correspondre à celle de l'Arduino)

# Connexion au port série
ser = serial.Serial(port, baud_rate)
time.sleep(2)  # Attente pour l'établissement de la connexion

print("Lecture des données depuis le port série...")

# Créer une liste pour stocker les données
data_list = []

try:
    while True:
        if ser.in_waiting > 0:
            # Lire une ligne de données envoyée par Arduino
            line = ser.readline().decode('utf-8').strip()
            print(f"Données reçues : {line}")
            
            # Parser la ligne JSON
            try:
                parsed_data = json.loads(line)
                
                # Ajouter les données au tableau
                data_list.append(parsed_data)
                
                # Enregistrer périodiquement dans un fichier Excel (ici chaque 10 entrées)
                if len(data_list) >= 10:
                    df = pd.DataFrame(data_list)
                    df.to_excel("output_data.xlsx", index=False)
                    print("Données enregistrées dans 'output_data.xlsx'")
                    data_list.clear()  # Vider la liste pour les nouvelles données
            except json.JSONDecodeError:
                print("Erreur de parsing JSON, ligne ignorée.")
except KeyboardInterrupt:
    print("Arrêt de la lecture.")
finally:
    # Si des données sont présentes, les enregistrer avant de quitter
    if data_list:
        df = pd.DataFrame(data_list)
        df.to_excel("output_data.xlsx", index=False)
        print("Données restantes enregistrées dans 'output_data.xlsx'")
    
    ser.close()
