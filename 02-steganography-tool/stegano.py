import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Steganography LSB")
    parser.add_argument("--input", default="sample_input.png")
    parser.add_argument("--output", default="sample_output.png")
    parser.add_argument("--message", default="Secret demo")
    parser.add_argument("--generate-sample", action="store_true", help="Genere une image d'entree simple")
    parser.add_argument("--demo", action="store_true", help="Mode demo sans Pillow")
    args = parser.parse_args()

    if args.demo:
        print("Demo: message cache dans une image (simulation).")
        print(f"Input: {args.input}")
        print(f"Output: {args.output}")
        return

    try:
        from PIL import Image  # type: ignore
    except Exception:
        print("Pillow requis. Installez: pip install pillow")
        print("Astuce: relancez avec --demo pour une demo.")
        return

    if args.generate_sample:
        img = Image.new("RGB", (200, 200), color=(240, 240, 240))
        img.save(args.input)

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
