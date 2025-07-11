# 📡 HTTP Header Analyzer GUI

**HTTP Header Analyzer** est une application graphique Linux développée en Python avec Tkinter.  
Elle permet d’analyser facilement les en-têtes HTTP d’un site web (URL ou domaine).

---

## 🖥️ Fonctionnalités

- ✅ Interface graphique simple (Tkinter)
- ✅ Saisie d’une URL (avec ou sans `http://`)
- ✅ Affichage de tous les en-têtes de réponse
- ✅ Détection des en-têtes de sécurité (X-*, CSP, HSTS, etc.)
- ✅ Compatible Debian / Kali / Ubuntu
- ✅ Paquet `.deb` avec menu, icône, et exécution globale

---

## 📷 Capture d’écran

*(Ajouter votre propre image si vous le souhaitez)*  
![HTTP Header GUI](httpheader.png)

---

## 📦 Installation

```bash
wget https://github.com/Ghassenz/httpheader-gui/releases/download/v1.0/http-header-gui.deb
sudo dpkg -i http-header-gui.deb
```

---

## 🚀 Lancement

- Depuis le menu Linux : `HTTP Header Analyzer`
- Ou dans le terminal :
```bash
httpheader
```

---

## 🔧 Dépendances

```bash
sudo apt install python3 python3-tk python3-requests
```

---

## 👤 Auteur

Développé par **Ghassenz**  
Projet personnel en cybersécurité et Python (Kali Linux)

🔗 [https://github.com/Ghassenz](https://github.com/Ghassenz)

---

## ✅ Licence

Projet open-source — libre d’utilisation à des fins personnelles ou pédagogiques.
