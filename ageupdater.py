import json
from datetime import date, datetime
from pathlib import Path


json_fil = Path(__file__).with_name("UGdataset.json")
datum_format = "%Y-%d-%m"


def calculate_age(birthdate: str, today: date) -> int:
    born = datetime.strptime(birthdate, datum_format).date()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def main() -> None:
    with json_fil.open(encoding="utf-8") as file:
        artists = json.load(file)

    if not isinstance(artists, list):
        raise ValueError(f"Expected a list of artists in {json_fil}")

    for artist in artists:
        if not isinstance(artist, dict) or not isinstance(artist.get("birthdate"), str):
            raise ValueError("Each artist must be an object with a string 'birthdate'")
        artist["age"] = calculate_age(artist["birthdate"], date.today())

    json_fil.write_text(
        json.dumps(artists, indent=4, ensure_ascii=False) + "\n",
        encoding="utf-8",

    )

if __name__ == "__main__":
    main()
