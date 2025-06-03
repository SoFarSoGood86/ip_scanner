# IP Scanner

IP Scanner est une intégration Home Assistant qui scanne instantanément toutes les machines connectées sur le réseau local. Elle expose pour chaque machine :

- l'adresse IP
- l'adresse MAC
- la puissance du signal Wi-Fi (RSSI)

## 📦 Installation via HACS

1. Ajouter le dépôt GitHub :
   ```
   https://github.com/SoFarSoGood86/ip-scanner
   ```
2. Rechercher `IP Scanner` dans HACS et installer.
3. Redémarrer Home Assistant.

## ⚙️ Configuration manuelle

Dans `configuration.yaml` :

```yaml
sensor:
  - platform: ip_scanner
```

## 📘 Exemple d'entités

- `sensor.ip_scanner_192_168_1_42`
- `sensor.ip_scanner_192_168_1_17`

## 🧠 Dépendances

- `scapy` (installée automatiquement)
