import os
import shutil
from pathlib import Path

DATEI_TYPEN = {
    "Bilder":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Dokumente":  [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv"],
    "Code":       [".py", ".js", ".html", ".css", ".java", ".json"],
    "Archive":    [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Sonstiges":  []
}


def get_kategorie(dateiname: str) -> str:
    """Gibt die Kategorie für eine Datei zurück."""
    endung = Path(dateiname).suffix.lower()
    for kategorie, endungen in DATEI_TYPEN.items():
        if endung in endungen:
            return kategorie
    return "Sonstiges"


def testordner_erstellen(pfad: str) -> None:
    """Erstellt einen Testordner mit Beispieldateien."""
    test_dateien = [
        "urlaubsfotos.jpg",
        "selfie.png",
        "bericht_q1.pdf",
        "notizen.txt",
        "daten.xlsx",
        "script.py",
        "index.html",
        "backup.zip",
        "praesentation.docx",
        "logo.svg",
        "unbekannt.xyz",
        "musik.mp3",
    ]

    os.makedirs(pfad, exist_ok=True)

    for datei in test_dateien:
        (Path(pfad) / datei).touch()

    print(f"✓ Testordner erstellt: {pfad}")
    print(f"  {len(test_dateien)} Dateien angelegt\n")


def dateien_sortieren(quell_pfad: str) -> dict:
    """Sortiert alle Dateien in Unterordner nach Typ."""
    zusammenfassung = {}
    quell_dir = Path(quell_pfad)

    for entry in os.scandir(quell_pfad):
        if not entry.is_file():
            continue

        kategorie = get_kategorie(entry.name)
        ziel_ordner = quell_dir / kategorie

        os.makedirs(ziel_ordner, exist_ok=True)

        try:
            shutil.move(entry.path, ziel_ordner / entry.name)
            zusammenfassung[kategorie] = zusammenfassung.get(kategorie, 0) + 1
        except Exception as fehler:
            print(f"  ✗ Fehler bei {entry.name}: {fehler}")

    return zusammenfassung


def ergebnis_anzeigen(zusammenfassung: dict) -> None:
    """Gibt eine formatierte Zusammenfassung aus."""
    gesamt = sum(zusammenfassung.values())

    print("=" * 35)
    print("  SORTIERUNG ABGESCHLOSSEN")
    print("=" * 35)

    for kategorie, anzahl in sorted(zusammenfassung.items()):
        print(f"  {kategorie:<12} → {anzahl} Datei(en)")

    print("-" * 35)
    print(f"  Gesamt: {gesamt} Dateien sortiert")
    print("=" * 35)


if __name__ == "__main__":
    TESTORDNER = "mein_download_ordner"

    print("DATEI-ORGANIZER\n")
    print("Schritt 1: Testordner erstellen...")
    testordner_erstellen(TESTORDNER)

    print("Schritt 2: Dateien werden sortiert...")
    ergebnis = dateien_sortieren(TESTORDNER)

    print("Schritt 3: Ergebnis\n")
    ergebnis_anzeigen(ergebnis)