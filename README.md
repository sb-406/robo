# Bachelorarbeit Simon
## Titel: Digitalisierung einer manuellen Presse zur Integration in IoT-Anwendungen 
- andere Idee war: Digitalisierung und Automatisierung eines manuellen Umformprozesses
## Aufgaben
	• Entwurf einer Ablaufsteuerung des Umformprozesses
		○ Definition der Teilschritte des Umformprozesses
		○ Analyse der Sicherheitsanforderungen
		○ Konzeption eines Ablaufdiagramms unter Berücksichtigung der Sicherheits- und  Bearbeitungsvorgaben
	• Implementierung der Schnittstelle zu Roboter
		○ Recherche der seriellen Kommunikationsschnittstelle des Roboters
		○ Implementierung der Schnittstelle auf dem Raspberry zur Kommunikation mit dem Roboter
		○ Definition der möglichen Kommandos 
	• Nachrüstung der Sensorik
		○ Anforderungsanalyse und Auswahl geeigneter Sensoren
		○ Anbringung der Sensoren
		○ Auslesen der Sensoren mit Raspi 
	• Nachrüstung der Aktorik zur automatisierten Bedienung der Presse
	• Automatisierung des Roboters
		○ Implementierung der Ablaufsteuerung basierend auf dem Ablaufdiagramm und der Sensorik
		○ Teachen der Wegpunkte und Aktionen
		○ Kalibrierung bei Gerätestart / Positionskorrektur
	• Bereitstellung der Prozessdaten auf ThingWorX
		○ Aufbereitung der Prozessdaten (Sensordaten, Metadaten, Zustände, Status, …)
		○ Implementierung der Schnittstelle zu ThingWorkX
	• Entwicklung und Implementierung der Prozessübersicht auf ThingWorX
		○ Darstellung der Sensordaten
		○ Visualisierung des Ablaufdiagramms inkl. Prozesszustand und ggf. Metadaten
	• Ideen
		○ Steuerung des Roboters von der Cloud aus oder einfach remote von anderem Rechner
		○ Live-CAD-Visualisierung des Umformungsprozesses
