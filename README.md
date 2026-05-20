# 🏥 Projet CVRIE - Data Science & Machine Learning

Bienvenue dans le dépôt du projet **CVRIE**. Ce projet explore plusieurs concepts fondamentaux de **Machine Learning** avec Python, en se divisant en trois grandes parties fonctionnelles : l'apprentissage **supervisé**, l'apprentissage **non-supervisé** et la mise en pratique via une **application interactive**.

## 📂 Structure du Projet

Le dépôt est organisé de la manière suivante :

- **`supervisé/`** :
  - Consacré à la classification d'images médicales (Radiographies pulmonaires / Chest X-Rays) pour détecter des cas de pneumonie (Normal, Bactérie, Virus).
  - *Méthodes utilisées* : Normalisation d'images (256x256), aplatissement (flattening), réduction de dimensions (PCA), et entraînement de modèles de Machine Learning classiques (`RandomForest`, `KNN`, et `MLP`).
- **`non-supervisé/`** :
  - Consacré à l'analyse et à la classification de données métier/étudiants (`Student_Dataset.csv`).
  - *Méthodes utilisées* : Exploration spatiale des données, nettoyage, et méthodes de clustering pour isoler des groupes (K-Means, clustering hiérarchique, etc.).
- **`bonus/`** : 
  - Application web en Python créée via **Streamlit** (`app.py`).
  - L'application utilise les modèles entrainés (KMeans, SVG et traitement NLP) pour catégoriser des symptômes de patients et les rediriger vers les bons services hospitaliers.

## 🛠️ Technologies et Librairies

- **Langage principal** : Python
- **Manipulation de la donnée** : `numpy`, `pandas`
- **Visualisation** : `matplotlib`, `seaborn`
- **Machine Learning** : `scikit-learn`
- **Interface Web** : `streamlit`
- **Environnement de développement** : Jupyter Notebook (`jupyter`, `ipykernel`)

## 🚀 Installation & Lancement

1. **Cloner le projet** et se placer à la racine :
   ```bash
   git clone https://github.com/jawedlahrouri/Cvrie
   cd CVRIE
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python -m venv venv
   # Activation sous Windows
   .\venv\Scripts\activate 
   # Activation sous Mac/Linux
   source venv/bin/activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Explorer les notebooks** :
   Vous pouvez démarrer le serveur Jupyter pour exécuter les différentes phases métier :
   ```bash
   jupyter notebook
   ```

5. **Lancer l'application web** :
   Démarrez l'application Streamlit pour tester le système de redirection hospitalière :
   ```bash
   streamlit run bonus/app.py
   ```

---
*Projet réalisé dans le cadre du module AIA.*

## Auteurs
- Joseph Birck
- Lucas Lhomme
- Jawed Lahrouri
