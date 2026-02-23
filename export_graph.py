import os
import matplotlib.pyplot as plt

# Dossier pour enregistrer les images
images_dir = "images"
os.makedirs(images_dir, exist_ok=True)

# Exemple : liste de vos graphiques (remplace par tes DataFrames/plots réels)
# Remplace ces sections par tes propres plots du notebook
def save_all_graphs():
    # Top Produits
    plt.figure(figsize=(10,6))
    # Remplace par ton code de graphique réel
    plt.plot([10,20,30],[100,200,150])
    plt.title("Top Produits")
    plt.savefig(os.path.join(images_dir, "top_products.png"))
    plt.close()

    # Top Pays
    plt.figure(figsize=(10,6))
    plt.plot([1,2,3],[50,60,70])
    plt.title("Top Pays")
    plt.savefig(os.path.join(images_dir, "top_countries.png"))
    plt.close()

    # Ventes Mensuelles
    plt.figure(figsize=(10,6))
    plt.plot([1,2,3],[200,300,250])
    plt.title("Ventes Mensuelles")
    plt.savefig(os.path.join(images_dir, "monthly_sales.png"))
    plt.close()

    # Top Clients
    plt.figure(figsize=(10,6))
    plt.plot([1,2,3],[5,15,25])
    plt.title("Top Clients")
    plt.savefig(os.path.join(images_dir, "top_clients.png"))
    plt.close()

save_all_graphs()
print("✅ Tous les graphiques ont été exportés dans 'images/'")