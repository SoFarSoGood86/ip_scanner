# IP Scanner

**IP Scanner** est une intégration Home Assistant permettant de détecter toutes les adresses IP, adresses MAC et puissances du signal Wi-Fi des appareils connectés sur votre réseau local.

## Fonctionnalités

- Scan périodique de votre réseau (`wlan0`)
- Détection IP + MAC + RSSI (dBm)
- Création d'entités `device_tracker` par appareil
- Compatible HACS

## Installation

### Via HACS

1. Aller dans HACS > Intégrations > Personnalisé > Ajouter un dépôt :
   - **URL** : `https://github.com/SoFarSoGood86/ip_scanner`
   - **Type** : Intégration
2. Rechercher `IP Scanner` et installer.
3. Redémarrer Home Assistant.

## Configuration

Aucune configuration manuelle nécessaire. L'intégration détecte automatiquement les appareils connectés.

## Limitations

- Compatible uniquement avec `Linux` et l'interface `wlan0` (adaptable).
- Nécessite que les commandes `iw` et `arp` soient disponibles sur le système.

## Auteur

GitHub : [SoFarSoGood86](https://github.com/SoFarSoGood86)
