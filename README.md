# KVB Fahrplanauskunft für Home Assistant

Eine Home Assistant Custom Integration für Live-Fahrplanauskünfte von KVB / VRS mit Haltestellensuche, Verbindungsabfragen, Vorher-/Nächste-Verbindungen und moderner Lovelace-Card.

Die Integration stellt einen Home-Assistant-internen API-Proxy für die offizielle KVB Journey API bereit. Dadurch funktionieren die Abfragen zuverlässig auch auf iPhone, Android-Tablets, Fully Kiosk Browser und eingebetteten WebViews ohne CORS-Probleme.

## Funktionen

- Haltestellensuche für KVB / VRS
- Auswahl von Start- und Zielhaltestelle
- Fahrplanauskunft mit Datum und Uhrzeit
- Vorher-/Nächste-Verbindungen per recallId
- Kompakte Fahrplanansicht im ÖPNV-Stil
- Erkennung von Bahn, Bus und Fußwegen
- Anzeige von Fahrzeit und Haltestellenanzahl
- Speicherung der letzten Start-/Zielhaltestelle
- KVB-Branding
- Optimierungen für Fully Kiosk Browser und Android-Tablets
- Home Assistant API-Proxy
- Debug-Logging im Home Assistant Log
- Unterstützung für eine Lovelace Custom Card

## Fahrplanfunktionen

- Aktuelle Verbindungen
- Zukünftige Abfahrten
- Frühere Abfahrten
- Manuelle Datumsauswahl
- Manuelle Uhrzeitauswahl
- Vorher-/Nächste-Navigation


## Installation

[![Open your Home Assistant instance and open this repository inside HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=einfall&repository=kvb-fahrplanauskunft&category=integration)
