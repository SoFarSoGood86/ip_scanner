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



