# IP Scanner

**IP Scanner** est une intégration personnalisée pour Home Assistant qui permet de détecter instantanément les appareils connectés à votre réseau Wi-Fi local (`wlan0`). Pour chaque appareil, elle fournit :

- L'adresse IP
- L'adresse MAC
- La puissance du signal Wi-Fi (RSSI)
- Une entité `device_tracker` par machine connectée

---

## 🛠 Installation

### Via [HACS](https://hacs.xyz)

1. Ouvrez Home Assistant.
2. Allez dans **HACS > Intégrations > 3 points > Dépôt personnalisé**.
3. Ajoutez ce dépôt :

```
https://github.com/SoFarSoGood86/ip_scanner
```

- **Type** : Intégration
4. Recherchez `IP Scanner` dans HACS et installez l’intégration.
5. Redémarrez Home Assistant.

---

### Installation manuelle (sans HACS)

1. Téléchargez le dépôt `ip_scanner` ou récupérez l’archive `ip_scanner.zip`.
2. Décompressez et placez le dossier dans :

```
/config/custom_components/ip_scanner/
```

3. Redémarrez Home Assistant.

---

## ⚙️ Configuration

L'intégration ne nécessite aucune configuration manuelle. Elle détecte automatiquement les appareils connectés à l’interface réseau **`wlan0`** (modifiable dans le code si nécessaire).

---

### Configuration YAML optionnelle

Si vous ne passez pas par HACS ou l’interface UI, vous pouvez l’intégrer manuellement via YAML :

```yaml
device_tracker:
  - platform: ip_scanner
```

> **Remarque** : Si vous utilisez HACS ou l'interface utilisateur, cette configuration n'est pas nécessaire.

---

## 📡 Données disponibles

Chaque appareil connecté est représenté par une entité `device_tracker.ip_scanner_<identifiant>`.

Les attributs fournis sont :

- `ip_address` : adresse IP
- `mac_address` : adresse MAC
- `signal_strength` : puissance du signal Wi-Fi en dBm

---

## 🧪 Limitations

- Fonctionne uniquement sur les systèmes Linux.
- Utilise les commandes `iw dev wlan0 station dump` et `arp -n` → assurez-vous qu’elles sont disponibles.
- L’interface réseau utilisée par défaut est `wlan0` (modifiable dans le fichier `scanner.py`).

---

## 🎨 Icône

L’intégration fournit une icône personnalisée : `icon.png`

---

## 👤 Auteur

- GitHub : [SoFarSoGood86](https://github.com/SoFarSoGood86)
- Projet : [IP Scanner](https://github.com/SoFarSoGood86/ip_scanner)

---

## 📄 Licence

Ce projet est sous licence MIT.
