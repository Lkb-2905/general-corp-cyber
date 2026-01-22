import argparse


def main() -> None:
    try:
        from PIL import Image  # type: ignore
    except Exception:
        print("Pillow requis. Installez: pip install pillow")
        return

    parser = argparse.ArgumentParser(description="Steganography LSB")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--message", required=True)
    args = parser.parse_args()

    img = Image.open(args.input)
    pixels = img.load()
    msg = args.message + "\0"
    bits = "".join(f"{ord(c):08b}" for c in msg)

    idx = 0
    for y in range(img.height):
        for x in range(img.width):
            if idx >= len(bits):
                img.save(args.output)
                print(f"Image sauvegardee: {args.output}")
                return
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(bits[idx])
            pixels[x, y] = (r, g, b)
            idx += 1


if __name__ == "__main__":
    main()
