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


> 🧭 **Note importante :**  
> Ce projet fait partie d’une série de **5 étapes** qui seront publiées progressivement.  
> Chaque étape correspond à une fonctionnalité clé du projet **CyberCrawler-Python**.  
>  
> 🔔 **Pensez à suivre le dépôt GitHub**  
> Chaque étape sera documentée, testée et illustrée avec des exemples pratiques.

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

---

## Pourquoi ce projet est moderne et utile

Ce projet fournit un environnement de cybersécurité moderne et pédagogique, conçu pour reproduire les pratiques réelles des ingénieurs en sécurité offensive.

###  Une approche structurée et réaliste
- Le projet est découpé en étapes claires et modulaires : Crawler → Détection SQLi → Détection XSS → Recherche de données sensibles → Rapports.  
- Chaque étape est indépendante, automatisable et testable.  
- L’environnement repose sur des machines virtuelles isolées (Parrot OS & Debian) pour garantir sécurité et légalité des tests.

### 🕸️ Le Crawler HTML récursif
- Cœur du **Projet 1** : explore automatiquement les pages d’un site interne.  
- Conçu pour découvrir les liens internes, éviter les doublons et fournir une carte claire du site - utile pour l’analyse de vulnérabilités.  
- Implémenté en Python 3 avec `requests` et `BeautifulSoup`, des bibliothèques éprouvées et faciles à maintenir.

### 💡 Ce qui rend le projet moderne
- Code simple, lisible et commenté - idéal pour l’apprentissage et la collaboration.  
- Conçu pour évoluer facilement vers des technologies plus avancées :
  - `asyncio` + `httpx` pour un crawl asynchrone et plus rapide ;  
  - `logging` et configuration pour une exécution professionnelle ;  
  - génération automatique de rapports JSON / Markdown ;  
  - intégration possible de Playwright pour crawler les sites dynamiques (JS).  
- Respect des bonnes pratiques : le projet s’exécute dans un réseau local isolé et ne cible jamais des sites publics sans autorisation.

### En résumé
Ce projet montre comment construire, étape par étape, un outil d’analyse web moderne, éthique et automatisé, alliant programmation Python, méthodologie de tests et bonnes pratiques de cybersécurité.

> 🚧 **État du développement — Projet 1**  
> Ce dépôt contient actuellement **l’Étape 1 : Crawler HTML récursif** (configuration réseau + démonstration sur Juice Shop).  
>  
> 🔜 **Prochaine étape : Détection d’injection SQL**  
> Je travaille maintenant sur l’Étape 2 (détection automatique d’injection SQL).  
> Suivez le dépôt pour recevoir les mises à jour — la v2 proposera :  
> - Un scanner automatique de formulaires et paramètres ;  
> - Des tests de payloads SQL basiques et avancés ;  
> - Des rapports clairs (logs + JSON) pour reproduction et triage.