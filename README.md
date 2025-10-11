# Projet 1 - Réseau VM & Docker (Parrot ↔ Debian + Juice Shop)

**Auteur :** Virginie Lechene  
**Projet :** Python Project - Cybersecurity & Automation (préparation de l'infrastructure)  
**Objectif :** Mettre en place un laboratoire isolé (VirtualBox) entre deux machines virtuelles - **Parrot OS** (attaquant) et **Debian** (victime) - lancer une application vulnérable (OWASP Juice Shop) dans Docker sur la VM victime et vérifier l'accès depuis la VM attaquante.

---

##  Fonctionnalité clé / Étapes du projet
Le projet est divisé en plusieurs étapes pédagogiques et modulaires :

| Étape | Fonction |
|---:|:---|
| ✅ Étape 1 | Crawler HTML récursif |
| 🔜 Étape 2 | Détection d'injection SQL |
| 🔜 Étape 3 | Détection de failles XSS |
| 🔜 Étape 4 | Recherche de données sensibles |
| 🔜 Étape 5 | Génération de rapport JSON / Markdown |


> 🧭 **Note importante :**  
> Ce projet fait partie d'une série de **5 étapes** qui seront publiées progressivement.  
> Chaque étape correspond à une fonctionnalité clé du projet **CyberCrawler-Python**.  
>  
> 🔔 **Pensez à suivre le dépôt GitHub**  
> Chaque étape sera documentée, testée et illustrée avec des exemples pratiques.

---

## 🧰 Outils modernes utilisés

- **Python 3** - Langage principal du projet  
- **Requests** & **BeautifulSoup4** - Pour le crawler web  
- **Docker** - Pour exécuter l’application vulnérable (*Juice Shop*)  
- **ip** & **ss** - Commandes réseau modernes (remplaçant *ifconfig* / *netstat*)  
- **curl** - Pour tester les pages web depuis la VM  
- **Git & GitHub** - Pour la gestion et le partage du code  

> 💡 Tous les outils utilisés sont récents, stables et conformes aux standards modernes de la cybersécurité et du développement Python.

---

##  Résumé (ce que contient ce dépôt)
Ce dépôt documente et automatise la préparation de l’environnement pour l’Étape 1 :
1. Configuration réseau VirtualBox (réseau interne `Lan-Test`) entre Parrot et Debian.
2. Attribution d’adresses IP statiques temporaires (192.168.100.10 pour Debian, 192.168.100.20 pour Parrot).
3. Lancement du conteneur Juice Shop sur Debian (port 3000).
4. Vérification de la connectivité (ping, curl) depuis Parrot.

Toutes les commandes sont exécutées dans les VMs (captures d’écran disponibles dans le dossier `screenshots/` si fourni).

---

##  🔎 Topologie réseau
- VirtualBox : réseau interne nommé `Lan-Test`.
- **Debian (victime)** : 192.168.100.10/24
- **Parrot (attaquant)** : 192.168.100.20/24
- **Juice Shop (Docker)** : exposé sur `0.0.0.0:3000` dans Debian

> 🔎 Important : vérifier que, dans VirtualBox, les adaptateurs internes ont **le même nom exact** (`Lan-Test`) et que l'option **Câble branché** est cochée.

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


<p align="center">
  <img src="https://github.com/virg736/CyberCrawler-Python/blob/main/projet_python_1.PNG" 
       alt="Ping + lancement Juice Shop (Debian)" width="850">
  <br>
  <em>Ping Parrot ↔ Debian et démarrage de Juice Shop dans Docker</em>
</p>


Sur Parrot (attaquant) :  
sudo ip addr add 192.168.100.20/24 dev enp0s3  
sudo ip link set enp0s3 up  
ip -br a    


<p align="center">
  <img src="https://github.com/virg736/CyberCrawler-Python/blob/main/projet_python_ip.PNG" 
       alt="Test de connectivité IP entre Parrot et Debian" width="850">
  <br>
  <em>Test de connectivité entre Parrot (attaquant) et Debian (victime) - Ping réussi</em>
</p>


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


<p align="center">
  <img src="https://github.com/virg736/CyberCrawler-Python/blob/main/projet_python1_juice%20Shop.PNG" 
       alt="Ping et lancement de Juice Shop dans Docker (Debian)" width="850">
  <br>
  <em>Ping entre Parrot ↔ Debian et lancement de Juice Shop dans Docker</em>
</p>


5) Tester HTTP (depuis Parrot)    

curl -I `http://192.168.100.10:3000`  
ou récupérer le HTML  
curl `http://192.168.100.10:3000`  
✅ Attendu : HTTP/1.1 200 OK et contenu HTML  


<p align="center">
  <img src="https://github.com/virg736/CyberCrawler-Python/blob/main/projet_python1_curl_ok.PNG" 
       alt="Test HTTP avec curl depuis Parrot vers Juice Shop" width="850">
  <br>
  <em>Test HTTP (curl) depuis Parrot vers Juice Shop - Réponse 200 OK</em>
</p>


---

## Pourquoi ce projet est moderne et utile

Ce projet fournit un environnement de cybersécurité moderne et pédagogique, conçu pour reproduire les pratiques réelles des ingénieurs en sécurité offensive.

###  Une approche structurée et réaliste  
- Le projet est découpé en étapes claires et modulaires : Crawler → Détection SQLi → Détection XSS → Recherche de données sensibles → Rapports.    
- Chaque étape est indépendante, automatisable et testable.    
- L’environnement repose sur des machines virtuelles isolées (Parrot OS & Debian) pour garantir sécurité et la légalité des tests.   

### 🕸️ Le Crawler HTML récursif  
- Cœur du **Projet 1** : explore automatiquement les pages d’un site interne.    
- Conçu pour découvrir les liens internes, éviter les doublons et fournir une carte claire du site - utile pour l’analyse des vulnérabilités.    
- Implémenté en Python 3 avec `requests` et `BeautifulSoup`, des bibliothèques éprouvées et faciles à maintenir.   

### 💡 Ce qui rend le projet moderne
- Code simple, lisible et commenté - idéal pour l'apprentissage et la collaboration.  
- Conçu pour évoluer facilement vers des technologies plus avancées :
- `asyncio` + `httpx` pour un crawl asynchrone et plus rapide ;  
- `logging` et configuration pour une exécution professionnelle ;  
- génération automatique de rapports JSON / Markdown ;  
- intégration possible de Playwright pour crawler les sites dynamiques (JavaScript).  
- Respect des bonnes pratiques : le projet s’exécute dans un réseau local isolé et ne cible jamais des sites publics sans autorisation.

### En résumé
Ce projet montre comment construire, étape par étape, un outil d’analyse web moderne, éthique et automatisé, alliant programmation Python, méthodologie de test et bonnes pratiques de cybersécurité.

---

> 🚧 **État du développement - Projet 1**  
> Ce dépôt contient actuellement **l’Étape 1 : Crawler HTML récursif** (configuration réseau + démonstration sur Juice Shop).  
>  
> 🔜 **Prochaine étape : Détection d’injection SQL**  
> Je travaille actuellement sur l'Étape 2 (détection automatique d’injections SQL).  
> Suivez le dépôt pour recevoir les mises à jour. 

---

## Vocabulaire & termes techniques (explications simples)

✅**VM (Machine virtuelle)**  
Une machine « logique » qui tourne à l'intérieur de ton ordinateur (ex. Parrot, Debian).  
Elle permet d'isoler des environnements.  

✅**VirtualBox**  
Logiciel qui crée et gère des VM.  
Ici on met les deux VM sur un réseau interne pour qu'elles puissent communiquer.  

✅**Docker / Conteneur**  
Docker exécute des applications empaquetées (« conteneurs »).   
Un conteneur contient l’application et ses dépendances (ex. Juice Shop).  

✅**Image Docker**  
Fichier standard qui sert à créer un conteneur (par ex. `bkimminich/juice-shop`).

✅**Juice Shop**  
Application web volontairement vulnérable utilisée pour apprendre la sécurité web.

✅ **Parrot OS / Debian**    
Distributions Linux utilisées dans ce projet :    
- **Parrot OS** → pour les outils de tests d’intrusion (attaquant)    
- **Debian** → pour héberger l’application vulnérable (victime)  

✅**Interface réseau (ex. `enp0s3`)**  
Nom de la carte réseau dans la VM. On lui assigne une adresse IP pour communiquer.

✅**IP / CIDR (ex. `192.168.100.10/24`)**  
Adresse qui identifie une machine sur le réseau + format réseau (`/24` = masque).

✅**Réseau interne (VirtualBox)**  
Mode réseau qui permet aux VM de communiquer entre elles sans sortir sur Internet.

✅**Ping**  
Commande qui vérifie si une machine répond (ICMP). Utile pour tester la connectivité réseau.

✅**curl**  
Outil permettant d'effectuer des requêtes HTTP depuis le terminal (tester une page web ou obtenir les en-têtes).

✅**Port (ex. 3000)**  
Canal sur lequel une application écoute. Juice Shop écoute sur le port 3000.

✅**ss / netstat**  
Outils permettant de lister les connexions et les services écoutant sur les ports (ex. `ss -tlnp`).

✅**Crawler HTML**  
Programme qui parcourt automatiquement les pages d’un site en suivant les liens internes.

✅**URL**  
Adresse d’une page web (ex. `http://192.168.100.10:3000`).

✅**HTTP / code 200**  
Protocole web. Code `200` signifie « OK » (page accessible).

✅**BeautifulSoup / Requests**  
Bibliothèques Python utilisées pour récupérer et analyser le contenu HTML.

✅**Asynchrone (asyncio / httpx)**  
Technique pour accélérer le crawler en faisant plusieurs requêtes en même temps.

✅**Logging**  
Enregistrement des actions du programme (utile pour déboguer et générer des rapports).

✅**SQL Injection (SQLi)**  
Type de faille où un attaquant injecte du code SQL dans un champ afin manipuler la base de données.

✅**XSS (Cross-Site Scripting)**  
Faille permettant d’injecter du code JavaScript malveillant dans une page web.

✅**Données sensibles**  
Informationss qu’il ne faut pas exposer publiquement (mots de passe, clés API, adresses privées).

✅**JSON / Markdown**  
Formats de sortie utilisées pour les rapports : JSON (machine-readable) et Markdown (lisible par humain).

✅**Playwright**  
Outil permettant d'automatiser un navigateur (utile pour crawler des sites générés par JavaScript).

✅**Bonnes pratiques & légalité**  
Ce projet s’exécute dans un laboratoire isolé (VM + réseau interne). Ne scannez ni n’attaquez jamais des sites réels sans autorisation écrite.

---


✍️ Auteur : *Virginie Lechene*

---

## Licence
Le script est publié sous la licence MIT.

## À propos de l’usage
Ce projet est destiné exclusivement à des fins pédagogiques, notamment dans le cadre de :
- d’une formation en cybersécurité,
- de tests d’intrusion légaux (pentest),
- d’analyses réseau dans un environnement contrôlé.

⚠️ L’auteure ne cautionne ni n’autorise l’utilisation de ce script en dehors d’un cadre légal strictement défini.
Toute utilisation non conforme est interdite et relève uniquement de la responsabilité de l’utilisateur.

## Droits sur les visuels
Les visuels, illustrations ou captures présents dans ce dépôt sont la propriété exclusive de l’auteure.
Toute reproduction ou utilisation non autorisée est interdite.







