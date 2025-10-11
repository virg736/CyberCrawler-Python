# Projet 1 - Réseau VM & Docker (Parrot ↔ Debian + Juice Shop)

**Auteur :** Virginie Lechene  
**Projet :** Python Project - Cybersecurity & Automation (préparation infra)  
**Objectif :** Mettre en place un laboratoire isolé (VirtualBox) entre deux machines virtuelles - **Parrot OS** (attaquant) et **Debian** (victime) - lancer une application vulnérable (OWASP Juice Shop) dans Docker sur la VM victime et vérifier l’accès depuis la VM attaquante.

---

##  Fonctionnalités / Étapes du projet
Le projet est divisé en plusieurs étapes pédagogiques et modulaires :

| Étape | Fonction |
|---:|:---|
| ✅ Étape 1 | Crawler HTML récursif |
| 🔜 Étape 2 | Détection d’injection SQL |
| 🔜 Étape 3 | Détection de failles XSS |
| 🔜 Étape 4 | Recherche de données sensibles |
| 🔜 Étape 5 | Génération de rapport JSON / Markdown |

---

##  Résumé (ce que contient ce dépôt)
Ce dépôt documente et automatise la préparation de l’environnement pour l’Étape 1 :
1. Configuration réseau VirtualBox (réseau interne `Lan-Test`) entre Parrot et Debian.
2. Attribution d’adresses IP statiques temporaires (192.168.100.10 pour Debian, 192.168.100.20 pour Parrot).
3. Lancement du conteneur Juice Shop sur Debian (port 3000).
4. Vérification de la connectivité (ping, curl) depuis Parrot.

Toutes les commandes sont exécutées dans les VMs (captures d’écran disponibles dans le dossier `screenshots/` si fourni).

---

##  Topologie réseau
- VirtualBox : réseau interne nommé `Lan-Test`.
- **Debian (victime)** : 192.168.100.10/24
- **Parrot (attaquant)** : 192.168.100.20/24
- **Juice Shop (Docker)** : exposé sur `0.0.0.0:3000` dans Debian

> Important : vérifier que, dans VirtualBox, les adaptateurs internes ont **le même nom exact** (`Lan-Test`) et que l'option **Câble branché** est cochée.

---

##  Outils utilisés
- **VirtualBox** - virtualisation des machines.
- **Parrot OS** - VM attaquante (outils pentest).
- **Debian (12/13)** - VM victime (héberge Docker).
- **Docker** - exécution de Juice Shop (conteneur).
- **OWASP Juice Shop** - application vulnérable utilisée comme cible (port 3000).
- **Python 3** (+ `requests`, `beautifulsoup4`) - scripts du projet (crawler & futurs modules).
- **nmap**, **nikto**, **curl**, **ping**, **ss** - outils de vérification et reconnaissance réseau.
- **Git / GitHub** - versioning et partage.

---

##  Commandes & procédure (chronologique, à exécuter dans les VMs)

### 1) Vérifier les interfaces (sur chaque VM)

ip -br a

2) Assigner une IP temporaire & activer l’interface  

(remplace enp0s3 par l’interface active si différent)  

Sur Debian (victime) :

sudo ip addr add 192.168.100.10/24 dev enp0s3  
sudo ip link set enp0s3 up  
ip -br a  
ip route  

Sur Parrot (attaquant) :  
sudo ip addr add 192.168.100.20/24 dev enp0s3  
sudo ip link set enp0s3 up  
ip -br a    

3) Vérifier la connectivité depuis Parrot  
ping -c 4 192.168.100.10  
✅ Attendu : 4 packets transmitted, 4 received, 0% packet loss     

4) Lancer Juice Shop dans Docker (sur Debian)  
si Docker est déjà installé)  

docker run -d --restart unless-stopped --name juice-shop -p 3000:3000 bkimminich/juice-shop  
docker ps  
ss -tlnp | grep 3000    

docker run -d --restart unless-stopped --name juice-shop -p 3000:3000 bkimminich/juice-shop  
docker ps  
ss -tlnp | grep 3000    

5) Tester HTTP (depuis Parrot)  

curl -I http://192.168.100.10:3000  
ou récupérer le HTML  
curl http://192.168.100.10:3000  
✅ Attendu : HTTP/1.1 200 OK et contenu HTML  
