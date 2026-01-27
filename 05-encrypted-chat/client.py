import argparse
import os
import socket


def get_cipher():
    try:
        from cryptography.fernet import Fernet  # type: ignore
    except Exception:
        return None
    key = os.getenv("CHAT_KEY")
    if not key:
        print("Definissez CHAT_KEY depuis le serveur.")
        return None
    return Fernet(key.encode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Client de chat chiffre")
    parser.add_argument("--demo", action="store_true", help="Mode demo sans socket")
    args = parser.parse_args()

    if args.demo:
        print("Moi: Salut, connexion OK ?")
        print("Serveur: Oui, messages chiffres.")
        return

    host = "127.0.0.1"
    port = 5001
    cipher = get_cipher()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            msg = input("Moi: ")
            if cipher:
                s.sendall(cipher.encrypt(msg.encode("utf-8")))
            else:
                s.sendall(msg.encode("utf-8"))
            data = s.recv(4096)
            if not data:
                break
            if cipher:
                print("Serveur:", cipher.decrypt(data).decode("utf-8"))
            else:
                print("Serveur:", data.decode("utf-8"))


if __name__ == "__main__":
    main()
