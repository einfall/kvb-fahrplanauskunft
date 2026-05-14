# KVB Fahrplanauskunft für Home Assistant

Custom Integration + Lovelace Card für KVB-/VRS-Fahrplanauskünfte in Home Assistant.

[![Open your Home Assistant instance and open this repository inside HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=DEIN_GITHUB_NAME&repository=kvb-fahrplanauskunft&category=integration)

## Funktionen

- Start- und Zielhaltestelle suchen
- Scrollbare Trefferliste
- Journey-Abfrage mit Datum und Uhrzeit
- „Jetzt“, „Vorher“ und „Next“
- KVB API Proxy über Home Assistant
- Debug-Ausgaben im Home-Assistant-Log
- KVB Brand-Logo
- Kompakte Lovelace Card

## HACS Installation

1. Repository auf GitHub erstellen.
2. Inhalt dieses Repos hochladen.
3. In `README.md` und `manifest.json` `DEIN_GITHUB_NAME` ersetzen.
4. HACS öffnen.
5. Custom repository hinzufügen:
   ```text
   https://github.com/DEIN_GITHUB_NAME/kvb-fahrplanauskunft
   ```
6. Kategorie:
   ```text
   Integration
   ```
7. Installieren.
8. Home Assistant komplett neu starten.

## Lovelace Card

Die Card-Datei liegt im Repo als:

```text
kvb-journey-card.js
```

Kopiere sie nach:

```text
/config/www/kvb-journey-card.js
```

Dann Dashboard Resource hinzufügen:

```text
/local/kvb-journey-card.js?v=1
```

Typ:

```text
JavaScript-Modul
```

Karte:

```yaml
type: custom:kvb-journey-card
```

## Debug

Optional in `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.kvb_journey: debug
```

## Struktur

```text
custom_components/
└── kvb_journey/
    ├── __init__.py
    ├── config_flow.py
    ├── const.py
    ├── manifest.json
    ├── views.py
    └── brand/
        ├── icon.png
        └── logo.png

kvb-journey-card.js
hacs.json
README.md
LICENSE
.gitignore
```

## Hinweis

HACS unterscheidet zwischen Integration und Frontend-Plugin. Dieses Repo ist als Integration aufgebaut. Die Card-Datei ist enthalten, muss aber aktuell als Lovelace Resource eingebunden werden.
