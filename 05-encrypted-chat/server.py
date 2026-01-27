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
        key = Fernet.generate_key().decode("utf-8")
        print(f"CHAT_KEY={key}")
    return Fernet(key.encode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Serveur de chat chiffre")
    parser.add_argument("--demo", action="store_true", help="Mode demo sans socket")
    args = parser.parse_args()

    if args.demo:
        print("Serveur en ecoute sur 127.0.0.1:5001")
        print("CHAT_KEY=demo_key_base64")
        print("Client: Salut, connexion OK ?")
        print("Moi: Oui, messages chiffres.")
        return

    host = "127.0.0.1"
    port = 5001
    cipher = get_cipher()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Serveur en ecoute sur {host}:{port}")
        conn, _ = s.accept()
        with conn:
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                msg = data.decode("utf-8")
                if cipher:
                    msg = cipher.decrypt(data).decode("utf-8")
                print("Client:", msg)
                reply = input("Moi: ")
                if cipher:
                    conn.sendall(cipher.encrypt(reply.encode("utf-8")))
                else:
                    conn.sendall(reply.encode("utf-8"))


if __name__ == "__main__":
    main()
