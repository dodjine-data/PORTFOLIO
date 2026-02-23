import os
import nbformat
from nbconvert import PythonExporter
import matplotlib.pyplot as plt

# Dossier pour enregistrer les images
images_dir = "images"
os.makedirs(images_dir, exist_ok=True)

# Nom du notebook
notebook_file = "analysis.ipynb"

# Convertir le notebook en script Python
with open(notebook_file, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

exporter = PythonExporter()
source, _ = exporter.from_notebook_node(nb)

# Créer un fichier temporaire pour exécuter le code
temp_script = "temp_notebook_exec.py"
with open(temp_script, 'w', encoding='utf-8') as f:
    f.write(source)

# Exécuter le script et attraper les figures
import runpy
import matplotlib

# Forcer le backend pour l’export
matplotlib.use('Agg')

# Préparer le compteur pour les noms de fichiers
plot_counter = 1

# Rediriger plt.savefig pour enregistrer automatiquement toutes les figures
original_savefig = plt.Figure.savefig
def custom_savefig(self, fname=None, *args, **kwargs):
    global plot_counter
    if fname is None:
        fname = os.path.join(images_dir, f"figure_{plot_counter}.png")
        plot_counter += 1
    return original_savefig(self, fname, *args, **kwargs)
plt.Figure.savefig = custom_savefig

# Exécuter le script
runpy.run_path(temp_script)

# Supprimer le script temporaire
os.remove(temp_script)

print(f"✅ Tous les plots ont été exportés automatiquement dans '{images_dir}/'")

import os
import nbformat
from nbconvert import PythonExporter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import runpy

# Dossier pour enregistrer les images
images_dir = "images"
os.makedirs(images_dir, exist_ok=True)

# Nom du notebook
notebook_file = "analysis.ipynb"

# Convertir le notebook en script Python
with open(notebook_file, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

exporter = PythonExporter()
source, _ = exporter.from_notebook_node(nb)

# Fichier temporaire pour exécuter le code
temp_script = "temp_notebook_exec.py"
with open(temp_script, 'w', encoding='utf-8') as f:
    f.write(source)

# Préparer le compteur pour les noms de fichiers
plot_counter = 1

# Rediriger plt.savefig pour enregistrer automatiquement toutes les figures
original_savefig = plt.Figure.savefig
def custom_savefig(self, fname=None, *args, **kwargs):
    global plot_counter
    if fname is None:
        fname = os.path.join(images_dir, f"figure_{plot_counter}.png")
        plot_counter += 1
    return original_savefig(self, fname, *args, **kwargs)
plt.Figure.savefig = custom_savefig

# Exécuter le script
runpy.run_path(temp_script)

# Supprimer le fichier temporaire
os.remove(temp_script)

print(f"✅ Tous les plots ont été exportés automatiquement dans '{images_dir}/'")