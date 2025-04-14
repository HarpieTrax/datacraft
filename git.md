# 📖 Guide Git & GitHub 

Ce document explique les bases de **Git** et **GitHub**, leurs objectifs, les bonnes pratiques, les commandes essentielles et un workflow type. Parfait pour débuter et structurer son travail en développement.

---

## 📌 Qu'est-ce que Git et GitHub ?

- **Git** : logiciel de gestion de versions décentralisé. Il permet de suivre l'évolution d’un projet, collaborer et gérer plusieurs versions du code.
- **GitHub** : plateforme en ligne pour héberger des dépôts Git, collaborer en équipe et versionner le code à distance.

---

## 🎯 Pourquoi utiliser Git et GitHub ?

- Sauvegarder les différentes versions du projet.
- Collaborer à plusieurs sans écraser le travail des autres.
- Travailler sur des fonctionnalités séparées via les branches.
- Publier son code et le partager facilement.





## 🛠️ Installation et configuration de Git sous WSL et Visual Studio Code

Avant de commencer à utiliser Git et GitHub, voici comment l’installer et le configurer correctement sous **WSL (Windows Subsystem for Linux)**, et l’utiliser depuis **Visual Studio Code**.

---

### 📥 1. Installer Git sous WSL

Dans ton terminal WSL (Ubuntu, Debian...) :

```bash
sudo apt update
sudo apt install git
```

Vérifie ensuite l'installation avec :

```bash
git --version
```

Si la version s'affiche, Git est bien installé ✅.

---

### 🔧 2. Configurer Git pour la première fois

Indique ton nom et ton adresse email (ils apparaîtront dans l’historique des commits) :

```bash
git config --global user.name "Ton Nom"
git config --global user.email "tonemail@example.com"
```

Pour vérifier la configuration :

```bash
git config --list
```

---

### 📝 3. Configurer VS Code comme éditeur par défaut pour Git

Pour que Git ouvre les messages de commit ou les conflits dans **Visual Studio Code** :

```bash
git config --global core.editor "code --wait"
```

---

### 📦 4. Installer l’extension GitHub sur Visual Studio Code

Dans Visual Studio Code :
- Va dans l'onglet Extensions (ou `Ctrl+Shift+X`)
- Recherche `GitHub` et installe l'extension officielle
- Tu pourras ensuite te connecter facilement à ton compte GitHub et gérer tes dépôts depuis l'interface VS Code.

---

### 📁 5. Ouvrir ton projet WSL dans Visual Studio Code

Dans le terminal WSL :
1. Place-toi dans ton dossier de projet :
```bash
cd /chemin/vers/ton/projet
```

2. Ouvre Visual Studio Code depuis WSL :
```bash
code .
```

Le `.` signifie que VS Code ouvrira le dossier courant.  
⚠️ Il faut que **l'extension "Remote - WSL"** soit installée dans VS Code pour que ça fonctionne.

---

### 📄 6. Initialiser un dépôt Git dans ton projet

Une fois dans ton projet :

```bash
git init
```

Puis continue avec les commandes de base (`git add`, `git commit`, `git push`...).

---

## 📖 Résumé des prérequis et installations

| Outil                  | Commande / Action                                        |
|:----------------------|:---------------------------------------------------------|
| Mise à jour des paquets | `sudo apt update`                                        |
| Installer Git          | `sudo apt install git`                                    |
| Configurer Git          | `git config --global user.name` et `git config --global user.email` |
| Définir VS Code comme éditeur | `git config --global core.editor "code --wait"`         |
| Installer l'extension WSL | Depuis le Marketplace Extensions dans Visual Studio Code |
| Ouvrir un dossier WSL dans VS Code | `code .`                                        |

---

## ✅ Conclusion

Une fois Git installé et configuré sous WSL, et Visual Studio Code prêt, tu peux travailler confortablement sur tes projets Python tout en versionnant proprement ton code et en collaborant avec GitHub.




## 🚀 Commandes de base à connaître

### 📦 Initialiser un projet Git
```bash
git init
```

### 🔄 Cloner un dépôt existant
```bash
git clone url_du_repo
```

### 📑 Vérifier l’état du projet
```bash
git status
```

### ➕ Ajouter des fichiers à l’index
```bash
git add nom_du_fichier
# ou tout le dossier :
git add .
```

### 📌 Valider les changements (commit)
```bash
git commit -m "Message clair et descriptif"
```

### 📤 Envoyer les modifications sur GitHub
```bash
git push
```

### 📥 Récupérer les modifications du dépôt distant
```bash
git pull
```

### 📝 Voir l’historique des commits
```bash
git log
```

### 📝 Renommer un fichier
```bash
git mv ancien_nom nouveau_nom
```

---

## 📂 Exemple de fichier `.gitignore`

Ce fichier permet d’ignorer certains fichiers ou dossiers lors des commits.

Exemple :
```
# Fichiers Python
*.pyc
__pycache__/

# Dossiers système
.DS_Store

# Variables d'environnement
.env
```

---

## 🌱 Bonnes pratiques à respecter

- Écrire des **messages de commit explicites**.
- Utiliser des **branches pour chaque fonctionnalité**.
- Faire des **commits réguliers et logiques**.
- Ne pas commettre de fichiers inutiles : utiliser `.gitignore`.
- Documenter le projet avec un `README.md`.
- Synchroniser régulièrement avec le dépôt distant (`git pull`).

---

## 📖 Exemple de workflow éducatif

```bash
# Initialiser un projet local
git init

# Ajouter un fichier
git add mon_fichier.py

# Valider le fichier
git commit -m "Ajout du fichier principal"

# Lier un dépôt distant
git remote add origin url_du_repo

# Envoyer les fichiers sur GitHub
git push -u origin main
```

---

## 📚 Ressources utiles

- [Documentation Git](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/)
- [Cheat Sheet Git (GitHub)](https://education.github.com/git-cheat-sheet-education.pdf)

---

## 💡 Conclusion

Git et GitHub sont essentiels pour bien structurer un projet et collaborer efficacement. En appliquant ces bases et bonnes pratiques, vous gagnerez en rigueur et en organisation dans vos projets de développement.

```

---
