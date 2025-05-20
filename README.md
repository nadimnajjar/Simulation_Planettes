# 🌌 Simulation du Système Solaire

Ce projet est une simulation visuelle du système solaire réalisée en **Python** avec **Pygame**.

---

## 🎮 Fonctionnalités

- **Écran d'accueil** interactif avec deux boutons :
  - ✅ **Start** : lance la simulation des planètes
  - ❌ **Exit** : ferme l'application
- **Simulation graphique** fluide des planètes autour du soleil
- **Orbite circulaire** des planètes avec vitesses angulaires différentes
- **Interface graphique propre** avec image de fond
- **Architecture orientée objet** respectant les bonnes pratiques de programmation

---

## 🧱 Structure du projet

\`\`\`
.
├── main.py              # Contrôle principal du jeu (navigation entre scènes)
├── home.py              # Écran d’accueil avec boutons Start/Exit
├── Simulation.py        # Simulation des planètes et de leurs mouvements
├── planets.py           # Classe représentant une planète avec orbite
├── Button.py            # Classe réutilisable pour dessiner des boutons
├── constantes.py        # Constantes globales (taille écran, couleurs, etc.)
├── planets1.jpg         # Image utilisée dans l’écran d’accueil
\`\`\`

---

## ▶️ Instructions pour lancer le projet

1. ✅ Installez les dépendances (seulement `pygame`) :

\`\`\`bash
pip install pygame
\`\`\`

2. ▶️ Lancez le fichier principal :

\`\`\`bash
python main.py
\`\`\`

---

## 💡 Personnalisation possible

Tu peux facilement améliorer ce projet en ajoutant :

- Un bouton **Retour** dans la simulation
- Une **musique de fond** avec `pygame.mixer`
- Des **infos interactives** sur chaque planète (nom, distance, etc.)
- Un **mode nuit** ou **mode éducatif**
- Des **animations plus réalistes** avec textures et vitesses orbitales réelles

---

## 📷 Aperçu

![Aperçu Simulation](python/planets1.jpg)

---

## 📚 Objectif pédagogique

Ce projet a été réalisé pour :

- Apprendre à structurer un projet Python en POO
- Utiliser **Pygame** pour les interfaces et animations
- S'entraîner à créer une **navigation entre écrans** dans un programme graphique

---

## 📄 Licence

Ce projet est fourni à titre éducatif. Tu peux le modifier et le partager librement.

---

### 🚀 Bon voyage dans l’espace !
