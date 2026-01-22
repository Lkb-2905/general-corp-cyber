def main() -> None:
    try:
        import exifread  # type: ignore
    except Exception:
        print("exifread requis. Installez: pip install exifread")
        return

    path = input("Chemin image JPG: ").strip()
    with open(path, "rb") as handle:
        tags = exifread.process_file(handle)

    gps_lat = tags.get("GPS GPSLatitude")
    gps_lon = tags.get("GPS GPSLongitude")
    print("GPSLatitude:", gps_lat)
    print("GPSLongitude:", gps_lon)


if __name__ == "__main__":
    main()
