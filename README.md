# General Corp - Cyber (demo portfolio)

![Tests](https://github.com/Lkb-2905/general-corp-cyber/actions/workflows/tests.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

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

## Installation rapide
```
python -m venv .venv
source .venv/bin/activate  # ou .venv\\Scripts\\activate sous Windows
pip install -r requirements.txt
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
