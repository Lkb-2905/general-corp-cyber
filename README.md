# General Corp - Cyber (demo portfolio)

Objectif: demonstrer des concepts cyber courants avec des outils simples
et un mode demo quand il y a des dependances.

## Contenu
- `01-keylogger-educatif`: capture clavier (mode demo).
- `02-steganography-tool`: LSB image (mode demo).
- `03-portail-captif-phishing-demo`: page HTML statique.
- `04-exif-analyseur`: lecture EXIF (mode demo).
- `05-encrypted-chat`: chat chiffre (mode demo).

## Demarrage rapide (demos)
```
cd 01-keylogger-educatif
python keylogger.py --demo --output keys.demo.log

cd ../02-steganography-tool
python stegano.py --demo

cd ../03-portail-captif-phishing-demo
start index.html

cd ../04-exif-analyseur
python exif_reader.py --demo

cd ../05-encrypted-chat
python server.py --demo
python client.py --demo
```

## Captures conseillees
- `01-keylogger-educatif/keys.demo.log`
- Terminal: EXIF demo + chat demo.
- Page HTML: `03-portail-captif-phishing-demo/index.html`

## Dependances
Voir `requirements.txt`.

## Roadmap et suggestions
- `ROADMAP.md`
- `CODE_SUGGESTIONS.md`
