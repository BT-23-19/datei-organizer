import pandas as pd


def daten_erstellen() -> pd.DataFrame:
    daten = {
        "Name":      ["Anna", "Ben", "Clara"],
        "Note":      [1.3, 2.7, 1.0],
        "Bestanden": [True, True, True]
    }
    return pd.DataFrame(daten)


def auswertung(df: pd.DataFrame) -> None:
    print(f"Durchschnittsnote: {df['Note'].mean():.2f}")
    print(f"Beste Note: {df['Note'].min()}")
    print(f"Schlechteste Note: {df['Note'].max()}")


def beste_studenten(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["Note"] < 2.0]


def speichern(df: pd.DataFrame, dateiname: str) -> None:
    df.to_excel(dateiname, index=False)
    print(f"✓ Gespeichert: {dateiname}")


if __name__ == "__main__":
    df = daten_erstellen()
    auswertung(df)
    gefiltert = beste_studenten(df)
    speichern(gefiltert, "auswertung.xlsx")