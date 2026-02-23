import os
import nbformat
from nbconvert import PythonExporter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import runpy

# Dossier pour images
images_dir = "images"
os.makedirs(images_dir, exist_ok=True)

# Notebook
notebook_file = "analysis.ipynb"

# Convertir notebook en script Python
with open(notebook_file, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)
exporter = PythonExporter()
source, _ = exporter.from_notebook_node(nb)
temp_script = "temp_notebook_exec.py"
with open(temp_script, 'w', encoding='utf-8') as f:
    f.write(source)

# Compteur pour images
plot_counter = 1
original_savefig = plt.Figure.savefig
def custom_savefig(self, fname=None, *args, **kwargs):
    global plot_counter
    if fname is None:
        fname = os.path.join(images_dir, f"figure_{plot_counter}.png")
        plot_counter += 1
    return original_savefig(self, fname, *args, **kwargs)
plt.Figure.savefig = custom_savefig

# Exécuter le notebook
runpy.run_path(temp_script)
os.remove(temp_script)
print(f"✅ Tous les plots exportés dans '{images_dir}/'")

# -------------------------------
# Générer un README visuel automatique
# -------------------------------
readme_file = "README.md"

with open(readme_file, 'w', encoding='utf-8') as f:
    f.write("# Portfolio Elite - Analyse de données\n\n")
    f.write("Ce portfolio présente l'analyse complète du dataset.\n\n")
    
    # Ajouter toutes les images
    for img in sorted(os.listdir(images_dir)):
        if img.endswith(".png"):
            f.write(f"![{img}]({images_dir}/{img})\n\n")

print(f"✅ README visuel généré automatiquement avec toutes les images dans '{readme_file}'")