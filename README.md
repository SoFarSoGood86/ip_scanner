# 🕵️ IP Scanner

![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)
![GitHub release](https://img.shields.io/github/v/release/SoFarSoGood86/ip_scanner)

Détecte instantanément les appareils connectés à ton réseau local via ARP, et expose chaque appareil comme une entité capteur dans Home Assistant.

---

## 🔧 Fonctionnalités

- Scan des adresses IP et MAC sur le réseau local (ARP).
- Exposition des appareils détectés comme entités `sensor`.
- Détection automatique toutes les 5 minutes.
- Compatible HACS.

---

## 📦 Installation via HACS

1. Dans HACS, va dans `Intégrations` → `3 points` → `Dépôts personnalisés`.
2. Ajoute le dépôt GitHub : https://github.com/SoFarSoGood86/ip_scanner

en tant que **Intégration**.
3. Rechercher `IP Scanner` dans les intégrations HACS et installe-le.
4. Redémarre Home Assistant.
5. Va dans `Paramètres` → `Appareils & services` → `Ajouter une intégration` → cherche `IP Scanner`.

---

## 🖥️ Installation manuelle

1. Télécharge ce dépôt sous forme de `.zip`.
2. Copie le dossier `custom_components/ip_scanner/` dans : <config>/custom_components/ip_scanner/

3. Redémarre Home Assistant.
4. Ajoute l’intégration comme ci-dessus.

---

## 📡 Exemple de capteur créé

Une entité sera créée pour chaque appareil détecté, par exemple :

- `sensor.ip_scanner_00_11_22_33_44_55`

Attributs :

```yaml
ip: 192.168.1.42
mac: 00:11:22:33:44:55
signal: null

ℹ️ Le champ signal est actuellement non utilisé (support futur du RSSI Wi-Fi envisagé).

🚧 Limitations
Le scan se base uniquement sur l’ARP, donc :

Nécessite que les appareils aient communiqué récemment avec le réseau.

Ne fonctionne que sur le même sous-réseau.

Le champ signal Wi-Fi n’est pas encore disponible.


🧩 1. Ajout de ton dépôt dans HACS (pour toi ou pour d'autres)
Tu peux proposer ton intégration comme dépôt personnalisé HACS, sans passer par l'organisation officielle. Voici comment :

🔧 Étapes dans Home Assistant :
Va dans HACS > Intégrations.

Clique sur les ⋮ (3 points en haut à droite) > Dépôts personnalisés.

Renseigne l'URL de ton dépôt GitHub :

bash
Copier
Modifier
https://github.com/SoFarSoGood86/ip_scanner
Choisis le type : Intégration.

Clique sur Ajouter.

L’intégration apparaîtra alors dans HACS sous le nom IP Scanner, grâce à hacs.json.

🌍 2. Exemple de carte Lovelace (interface Home Assistant)
Tu peux créer une carte qui affiche tous les appareils détectés par l'intégration.

🧱 Exemple de carte entities :
yaml
Copier
Modifier
type: entities
title: Appareils détectés sur le réseau
entities:
  - entity: sensor.ip_scanner_00_11_22_33_44_55
    name: PC Bureau
  - entity: sensor.ip_scanner_aa_bb_cc_dd_ee_ff
    name: Smartphone Alice
  - entity: sensor.ip_scanner_11_22_33_44_55_66
    name: Smart TV
Tu peux automatiser l’affichage dynamique avec des filtres si tu utilises des noms dynamiques ou un groupement de sensors.
