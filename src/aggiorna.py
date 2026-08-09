# -*- coding: utf-8 -*-
"""Rigenera sito e CV. Unico comando da lanciare dopo aver modificato i dati.

    python3 src/aggiorna.py            rigenera tutto
    python3 src/aggiorna.py sito       solo index.html
    python3 src/aggiorna.py cv         solo i due PDF

Dove stanno i dati, e cosa aggiorna cosa:

  src/data.py                          SITO + CV
      bio, metriche, formazione ed esperienza, progetti (sigle, ruoli, periodi),
      didattica (14 corsi con le ore), supervisioni (25 magistrali + 2 dottorati),
      riconoscimenti, aree di ricerca, pubblicazioni selezionate, etichette bilingui.

  curriculum_vitae/resume/*.tex        SOLO CV
      journalpublications.tex          elenco completo delle pubblicazioni su rivista
      conferencepublications.tex       elenco completo a conferenze e workshop
      projects.tex                     descrizioni, ID di finanziamento, siti
      awards_and_prizes.tex            dettagli del premio Fibonacci
      competitions.tex                 competizioni
      thesis.tex                       relatore delle due tesi proprie
      (tutoring.tex e supervision.tex vengono riscritti da data.py: non modificarli)

  src/traduzioni.py                    SOLO CV, versione italiana
      i .tex qui sopra sono in inglese; la tabella li traduce voce per voce.
      Aggiungendo una pubblicazione con termini nuovi, controlla che siano coperti.

Attenzione: le pubblicazioni stanno in due posti. Le cinque selezionate del sito sono
in data.py, l'elenco completo del CV nei .tex. Aggiungendone una importante, va messa
in entrambi.

Serve xelatex per i CV. Il sito non richiede nulla oltre a Python.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def run(script, *args):
    print("\n>>> %s %s" % (script, " ".join(args)))
    r = subprocess.run([sys.executable, os.path.join(HERE, script)] + list(args), cwd=HERE)
    if r.returncode:
        print("    FALLITO (codice %d)" % r.returncode)
    return r.returncode == 0


def sito():
    return run("finalize.py")


def cv():
    if not any(os.access(os.path.join(p, "xelatex"), os.X_OK)
               for p in os.environ.get("PATH", "").split(os.pathsep)):
        print("\n!! xelatex non trovato: i CV non possono essere compilati.")
        print("   Il sito si rigenera lo stesso con: python3 src/aggiorna.py sito")
        return False
    return run("gen_cv2.py", "--publish")


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "tutto"
    ok = True
    if what in ("tutto", "sito"):
        ok &= sito()
    if what in ("tutto", "cv"):
        ok &= cv()
    print("\n--- prodotti in %s ---" % ROOT)
    for f in ("index.html", "CV_Eugenio_Lomurno_EN.pdf", "CV_Eugenio_Lomurno_IT.pdf",
              "CV_Eugenio_Lomurno.pdf"):
        p = os.path.join(ROOT, f)
        print("   %-30s %s" % (f, "%d KB" % (os.path.getsize(p) // 1024)
                               if os.path.exists(p) else "assente"))
    sys.exit(0 if ok else 1)
