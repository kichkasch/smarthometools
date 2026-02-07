# Anleitung, um einen "generischen" LED-Streifen in die Loxone einzubinden 

## 1) Einleitung
[Loxone](https://www.loxone.com/dede/) ist eine Hausautomatisierungslösung der gleichnamigen Firma. Ich stelle hier eine Lösung vor, wie allgemein verfügbare Komponenten für einen LED-Streifen zusammengestellt und in die Loxone-Lösung eingebunden werden können.
Diese Lösung ist maßgeblich inspiriert von folgender Diskussion im sogenannten Loxforum: [HOWTO: Günstige W-Lan RGB Controller Lösung (<35€) - Magic-UFO Wifi controller LD382](https://www.loxforum.com/forum/faqs-tutorials-howto-s/1236-howto-g%C3%BCnstige-w-lan-rgb-controller-l%C3%B6sung-35%E2%82%AC-magic-ufo-wifi-controller-ld382).

Natürlich stellt auch Loxone LED-Streifen mitsamt Zubehör zur Verfügung, die per Kabel (Loxone Tree) oder kabellos (Loxone Air) eingebunden werden können. Meine Recherche ergab jedoch, dass die Loxone-Lösung preislich ein Vielfaches der hier vorgestellten Lösung bedeutet.

*Anmerkung: Grundsätzliche Loxone-Programmierkenntnisse werden vorausgesetzt; an dieser Stelle werden nur die Spezifika für die Integration der LED-Streifen beschrieben.*

## 2) Benötige Hardware
*Der Markt ist mit Produkten für LED-Beleuchtung seit einigen Jahren überschwemmt; die Preise sind erheblich gefallen. Laut oben referenzierter Diskussion im Forum funktionieren auch verschiedene Produkte verschiedener Hersteller. Ich beschränke mich in folgender Auflistung auf immer genau einen Produktvorschlag, der im Zusammenspiel mit allen Komponenten erfolgreich gestestet ist und robust und verlässlich funktioniert.*

* Einen LED-Streifen selbst: BTF-LIGHTING 5M 5050 RGBWW 4 in 1 RGB +Warm White ([Amazon Link](https://www.amazon.de/gp/product/B01D1I50UW/ref=ppx_yo_dt_b_asin_title_o07_s01?ie=UTF8&psc=1)), ca. 30 € für 5 Meter
* Einen LED-Controller mit WLAN-Schnittsteller (Typ LD382A, Produktnummer ZJ-WFUF-170F): Generic DC12-24 V Magic UFO-WiFi LED-Controller ([Amazon Link](https://www.amazon.de/gp/product/B00Q7STR4E/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1)), ca. 20 €
* Ein Netzteil: Leicke Netzteil 60W 12V 5A ([Amazon Link](https://www.amazon.de/gp/product/B001W3UYLY/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1)), ca. 15 €
* Einen Loxone Server (Miniserver oder Miniserver Go), welcher sich im lokalen Netzwerk befindet.

## 3) Inbetriebnahme
Die Inbetriebnahme des LED-Streifens (ohne Loxone) erfolgt mittels einer App (z.B. "Magic Home" unter Android). Die Beschreibung ist dem LED-Controller beigefügt.

Am Ende der Intriebnahme muss sich der Controller per WLAN im gleichen Netz wie der Loxone Miniserver befinden.

## 4) Integration in Loxone

### Kurzbeschreibung der Gesamtlösung
Für spezifische Anwendungsfälle können in der Loxone-Lösung [Skripte hinterlegt werden](https://www.loxone.com/dede/kb/script-programming/). Diese Skripte müssen in der Sprache [PicoC](https://gitlab.com/zsaleeba/picoc) geschrieben sein (eine *abgespeckte* C-Variante). 

Das [in diesem Projekt hinterlegte Skript](https://github.com/kichkasch/kichkasch_loxonetools/blob/master/magichome/magichome.picoc.txt) für die LED-Steuerung wird in einen sogenannten Programm-Baustein reinkopiert. Dann können - wie gewohnt- die Eingänge genutzt werden.

### Vorbereitung
Die IP-Adresse der LED-Controllers wird benötigt - entweder aus dem Geräte-Manager der Magic-Home-App oder bspw. aus dem WLAN-Router.

### Einbindung in Loxone

1) Neuen [Programmbaustein](https://www.loxone.com/dede/kb/script-programming/) im Loxone-Programm anlegen (Name bspw. "MagicHome")
2) Inhalte von [magichome.picoc.txt](https://github.com/kichkasch/kichkasch_loxonetools/blob/master/magichome/magichome.picoc.txt) in den Baustein kopieren.
3) IP-Adresse in Zeile 18 auf die eigene IP-Adresse des LED-Controllers (s.o. Vorbereitung) ändern.
4) Neuen Loxone-Standardbaustein [RGB-Lichtszene](https://www.loxone.com/dede/kb/rgb_lichtszene/) hinzufügen.
5) Eine Konstante mit Name *Eins* und Wert *1* anlegen.
6) Die drei Komponenten wie in der [hinterlegten Abbildung](https://github.com/kichkasch/kichkasch_loxonetools/blob/master/magichome/magicHome.loxone.jpg) dargestellt miteinander verbinden.

Programm in Miniserver überspielen und neu starten. Off you go.

## Kontakt
Michael Pilgermann (kichkasch@gmx.de)
