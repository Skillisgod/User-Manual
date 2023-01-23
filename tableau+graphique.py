import pandas as pd
import matplotlib.pyplot as plt

# Ouverture et lecture du fichier dumpfile
with open("/Users/damie/Documents/DumpFile.txt", "r") as f:
    data = f.read()

# Initialisation d'une liste qui contiendra les données de chaque trame
frames_data = []

# Séparation du fichier en trames
frames = data.split('\n\n')

# Parcours de toutes les trames
for frame in frames:
    # Découpage de la trame en lignes
    lines = frame.split('\n')

    # Parcours de toutes les lignes de la trame
    for line in lines:
        # Si la ligne est vide, on passe à la suivante
        if not line:
            continue
        # Si la ligne commence par un chiffre, cela signifie qu'elle contient les informations de temps et d'adresse
        if line[0].isdigit():
            # Extraction de l'heure et de l'adresse
            parts = line.split(' ')
            address = parts[2]
            # Extraction des adresses IP source 
            ip_addresses = address.split(">")
            source_ip = ip_addresses[0].strip()
            # Ajout de l'IP source au dictionnaire de données
            frames_data.append(source_ip)

# Création d'un DataFrame
df = pd.DataFrame(frames_data, columns=['source_ip'])

# Grouper les adresses IP source et compter le nombre d'occurences
grouped_data = df.groupby(['source_ip']).size().reset_index(name='counts')

# Filtrer les adresses qui ont moins de 5 occurences
filtered_data = grouped_data[grouped_data['counts'] >= 5]

# Enregistrer les données filtrées dans un fichier CSV
filtered_data.to_csv("/Users/damie/Documents/IUT/SAE1.05/IP_counts.csv", index=False)

# affichage du graphique
filtered_data.plot(kind='bar', x='source_ip', y='counts')
plt.show()
