#🕷️ CyberCrawler-Python
[![Python CI](https://github.com/virg736/CyberCrawler-Python/actions/workflows/python-ci.yml/badge.svg)](https://github.com/virg736/CyberCrawler-Python/actions/workflows/python-ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

<p align="center">
  <img src="https://github.com/virg736/CyberCrawler-Python/blob/main/Projet%20Python.PNG" 
       alt="Illustration du projet CyberCrawler-Python" width="850">
  <br>
  <em>Illustration du projet <strong>CyberCrawler-Python</strong></em>
</p>


<div align="center">

© 2026 Virginie Lechene 

<a href="https://creativecommons.org/licenses/by-nd/4.0/" target="_blank">
  <img src="https://licensebuttons.net/l/by-nd/4.0/88x31.png" alt="Licence Creative Commons BY-ND 4.0">
</a>

</div>

---

## Sommaire - Projet 1 : CyberCrawler-Python

- [Vue d'ensemble](#projet-1--cybercrawler-python)
- [Objectif](#objectif)
- [Fonctionnalités clés / Étapes](#fonctionnalités-clés--étapes)
  - [Étape 1 - Crawler HTML récursif](#étape-1---crawler-html-récursif)
  - [Étape 2 - Détection d'injections SQL](#étape-2---détection-dinjections-sql)
  - [Étape 3 - Détection de failles XSS](#étape-3---détection-de-failles-xss)
  - [Étape 4 - Recherche de données sensibles](#étape-4---recherche-de-données-sensibles)
  - [Étape 5 - Génération de rapports JSON / Markdown](#étape-5---génération-de-rapports-json--markdown)
- [Outils utilisés](#outils-utilisés)
- [Résumé du contenu du dépôt](#résumé-du-contenu-du-dépôt)
- [Topologie réseau](#topologie-réseau)
- [Procédure et commandes (chronologie)](#procédure--commandes-chronologie)
- [Tests de fonctionnement](#tests-de-fonctionnement)
- [État du développement / Prochaine étape](#état-du-développement--prochaine-étape)
- [Licence et Avertissement](#licence--avertissement)


---

# Projet 1    

🕷️ CyberCrawler-Python  

 Projet 1 - Réseau VM & Docker (Parrot ↔ Debian + OWASP Juice Shop)  

 *Python Project - Cybersecurity & Automation (préparation de l’infrastructure)*    
 **Auteur :** Virginie Lechene    
 **Année :** 2025   

---

 💡 Objectif

Mettre en place un **laboratoire de cybersécurité isolé** (VirtualBox) entre deux machines virtuelles :   

- **Parrot OS** - VM attaquante    
- **Debian** - VM victime   

---

##  Fonctionnalités clés / Étapes du projet
Le projet est divisé en plusieurs étapes pédagogiques et modulaires :

| Étape | Fonction |
|---:|:---|
| ✅ Étape 1 | Crawler HTML récursif |
| ✅ Étape 2 | Détection d'injections SQL |
| ✅ Étape 3 | Détection de failles XSS |
| ✅ Étape 4 | Recherche de données sensibles |
| ✅ Étape 5 | Génération de rapports JSON / Markdown |


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
- **Docker** - Pour exécuter l’application vulnérable (*OWASP Juice Shop*)  
- **ip** & **ss** - Commandes réseau modernes (remplaçant *ifconfig* / *netstat*)  
- **curl** - Pour tester les pages web depuis la VM  
- **Git & GitHub** - Pour la gestion et le partage du code  

> 💡 Tous les outils utilisés sont récents, stables et conformes aux standards modernes de la cybersécurité et du développement Python.

---

##  Résumé (ce que contient ce dépôt)
Ce dépôt documente et automatise la préparation de l’environnement pour l’Étape 1 :
1. Configuration réseau VirtualBox (réseau interne `Lan-Test`) entre Parrot et Debian.
2. Attribution d’adresses IP statiques temporaires (192.168.100.10 pour Debian, 192.168.100.20 pour Parrot).
3. Lancement du conteneur OWASP Juice Shop sur Debian (exposé sur le port 3000).
4. Vérification de la connectivité depuis (ping, curl) depuis Parrot.

Toutes les commandes sont exécutées dans les VMs (captures d’écran disponibles dans le dossier `screenshots/` si fourni).

---

##  🔎 Topologie réseau
- VirtualBox : réseau interne nommé `Lan-Test`.
- **Debian (victime)** : 192.168.100.10/24
- **Parrot (attaquant)** : 192.168.100.20/24
- **Juice Shop (Docker)** : conteneur exposé sur le port 3000 `0.0.0.0:3000` de la VMs Debian

> 🔎 Important : vérifiez dans VirtualBox que les adaptateurs sont configurés sur **le même réseau interne** (`Lan-Test`) et que l'option **Câble branché** est cochée.

---

##  Outils utilisés
- **VirtualBox** - virtualisation des machines.
- **Parrot OS** - VM attaquante (outils pentest).
- **Debian (12/13)** - VM victime (héberge Docker).
- **Docker** - exécution de Juice Shop (conteneur).
- **OWASP Juice Shop** - application vulnérable utilisée comme cible (port 3000).
- **Python 3** (+ `requests`, `beautifulsoup4`) - scripts du projet (crawler & futurs modules).
- **nmap**, **nikto**, **curl**, **ping**, **ss** - outils de vérification et reconnaissance réseau.
- **Git / GitHub** - gestion de versions et partage.

-----

## 🧭 Topologie du laboratoire

> **Note :** Toutes les opérations décrites dans ce projet ont été réalisées dans un **réseau interne isolé (VirtualBox - LAN-Test)**.  
> Une connexion Internet a pu être utilisée uniquement pour l’installation préalable des dépendances. Les tests ont ensuite été réalisés exclusivement dans le réseau interne isolé.

---

##  Commandes & procédure (chronologique, à exécuter dans les VMs)

### 1) Vérifier les interfaces (sur chaque VM)  

ip -br a  

2) Assigner une IP temporaire & activer l’interface    

(remplace enp0s3 par l’interface active si différent)    

Sur Debian (victime) :    

sudo ip addr add 192.168.100.10/24 dev enp0s3    
sudo ip link set dev enp0s3 up    
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
sudo ip link set dev enp0s3 up    
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


<p align="center">
  <img src="https://github.com/virg736/CyberCrawler-Python/blob/main/projet_python1_juice%20Shop.PNG" 
       alt="Ping et lancement de Juice Shop dans Docker (Debian)" width="850">
  <br>
  <em>Ping entre Parrot ↔ Debian et lancement de Juice Shop dans Docker</em>
</p>

(*) Note : Le token affiché sur une capture d’écran provenait d’une instance locale (VirtualBox). 
Le conteneur Juice Shop est actuellement arrêté et supprimé, le token n’est plus valide. 
Toutes les démonstrations ont été effectuées dans un environnement isolé à des fins pédagogiques.

5) Tester l'accés HTTP (depuis Parrot)    

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


6) Nettoyage    

Retirer les adresses IP ajoutées :  

sudo ip addr del 192.168.100.10/24 dev enp0s3   # sur Debian  
sudo ip addr del 192.168.100.20/24 dev enp0s3   # sur Parrot  

---

### ✅ Tests de fonctionnement  

Le script `crawler.py` a été testé avec succès :    
- Environnement : **Parrot OS (VirtualBox)**    
- Python 3.11, `requests`, `beautifulsoup4`    
- Cible test : **Juice Shop `http://192.168.100.10:3000`**    
- Résultat :    
Exploration terminée - 1 page trouvée.  
➡️ Le script fonctionne correctement.


<p align="center">
  <img src="https://github.com/virg736/CyberCrawler-Python/blob/main/projet_python_test_script.2.PNG" 
       alt="Test du script crawler exécuté sur Parrot OS" width="850">
  <br>
  <em>Installation des dépendances et exécution du script crawler sur Parrot OS</em>
</p>

---

## Pourquoi ce projet est moderne et utile

Ce projet fournit un environnement de cybersécurité moderne et pédagogique, conçu pour reproduire les pratiques réelles des ingénieurs en sécurité offensive.

###  Une approche structurée et réaliste  
- Le projet est découpé en étapes claires et modulaires : Crawler → Détection SQLi → Détection XSS → Recherche de données sensibles → Rapports.    
- Chaque étape est indépendante, automatisable et testable.    
- L’environnement repose sur des machines virtuelles isolées (Parrot OS & Debian) afin de garantir la sécurité et la légalité des tests.   

### 🕸️ Le Crawler HTML récursif  
- Cœur du **Projet étape 1** : explore automatiquement les pages d’un site interne.    
- Conçu pour découvrir les liens internes, éviter les doublons et fournir une cartographie claire du site - utile pour l'analyse des vulnérabilités.    
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
> Ce dépôt contient actuellement **l'Étape 1 : Crawler HTML récursif** (configuration réseau + démonstration sur OWASP Juice Shop).  
>  
> 🔜 **Prochaine étape : Détection d'injections SQL**  
> Je travaille actuellement sur l'Étape 2 (détection automatique d'injections SQL).  
> Suivez le dépôt pour recevoir les mises à jour. 

---

## Vocabulaire & termes techniques (explications simples)

✅**VM (Machine virtuelle)**  
Une machine « logique » qui tourne à l'intérieur de ton ordinateur (ex. Parrot, Debian).  
Elle permet d'isoler des environnements.  

✅**VirtualBox**  
Logiciel qui crée et gère des machines virtuelles.  
Ici on configure les deux VM sur un réseau interne pour qu'elles puissent communiquer entre elles.  

✅**Docker / Conteneur**  
Docker exécute des applications empaquetées (« conteneurs »).   
Un conteneur contient l’application et ses dépendances (ex. OWASP Juice Shop).  

✅**Image Docker**  
Fichier standard qui sert à créer un conteneur (par ex. `bkimminich/juice-shop`).

✅**Juice Shop**  
Application web volontairement vulnérable utilisée pour apprendre la sécurité web.

✅ **Parrot OS / Debian**    
Distributions Linux utilisées dans ce projet :    
- **Parrot OS** → pour les outils de test d’intrusion (attaquant)    
- **Debian** → pour héberger l’application vulnérable (victime)  

✅**Interface réseau (ex. `enp0s3`)**  
Nom de la carte réseau dans la VM. On lui assigne une adresse IP pour communiquer.

✅**IP / CIDR (ex. `192.168.100.10/24`)**  
Adresse qui identifie une machine sur le réseau + format réseau (`/24` = masque réseau).

✅**Réseau interne (VirtualBox)**  
Mode réseau qui permet aux VM de communiquer entre elles sans sortir sur Internet.

✅**Ping**  
Commande qui vérifie si une machine répond (ICMP). Utile pour tester la connectivité réseau.

✅**curl**  
Outil permettant d'effectuer des requêtes HTTP depuis le terminal (tester une page web ou obtenir les en-têtes).

✅**Port (ex. 3000)**  
Canal sur lequel une application écoute. OWASP Juice Shop écoute sur le port 3000.

✅**ss / netstat**  
Outils permettant de lister les connexions et les services à l'écoute sur les ports (ex. `ss -tlnp`).

✅**Crawler HTML**  
Programme qui parcourt automatiquement les pages d’un site en suivant les liens internes.

✅**URL**  
Adresse d’une page web (ex. `http://192.168.100.10:3000`).

✅**HTTP / code 200**  
Protocole web. Code `200` signifie « OK » (page accessible).

✅**BeautifulSoup4 / Requests**  
Bibliothèques Python utilisées pour récupérer et analyser le contenu HTML.

✅**Asynchrone (asyncio / httpx)**  
Technique pour accélérer le crawler en lançant plusieurs requêtes en parallèle.

✅**Logging**  
Enregistrement des actions du programme (utile pour déboguer et générer des rapports).

✅**SQL Injection (SQLi)**  
Type de faille où un attaquant injecte du code SQL dans un champ afin manipuler la base de données.

✅**XSS (Cross-Site Scripting)**  
Faille permettant d’injecter du code JavaScript malveillant dans une page web.

✅**Données sensibles**  
Informations qu’il ne faut pas exposer publiquement (mots de passe, clés API, adresses privées).

✅**JSON / Markdown**  
Formats de sortie utilisées pour les rapports : JSON (machine-readable) et Markdown (lisible par l'humain).

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

## 📷 Droits sur les visuels

Les visuels de ce dépôt sont protégés par la licence CC BY-ND 4.0.
Attribution obligatoire – Modification interdite.

© 2026 Virginie Lechene





