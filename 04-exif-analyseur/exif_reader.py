import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyseur EXIF (GPS)")
    parser.add_argument("--input", help="Chemin vers une image JPG")
    parser.add_argument("--demo", action="store_true", help="Mode demo sans image")
    args = parser.parse_args()

    if args.demo:
        print("GPSLatitude: 48 deg 51' 29.99\"")
        print("GPSLongitude: 2 deg 17' 40.98\"")
        return

    try:
        import exifread  # type: ignore
    except Exception:
        print("exifread requis. Installez: pip install exifread")
        print("Astuce: relancez avec --demo pour une demo.")
        return

    path = args.input or input("Chemin image JPG: ").strip()
    with open(path, "rb") as handle:
        tags = exifread.process_file(handle)

    gps_lat = tags.get("GPS GPSLatitude")
    gps_lon = tags.get("GPS GPSLongitude")
    print("GPSLatitude:", gps_lat)
    print("GPSLongitude:", gps_lon)


if __name__ == "__main__":
    main()
