# -*- coding: utf-8 -*-
"""Da tracciato academicons a PDF vettoriale: rigenera ai-scholar.pdf e ai-scopus.pdf.

Non serve alla compilazione - i due PDF sono gia in curriculum_vitae/ - ma va rilanciato
se cambia il colore d accento:  python3 src/icons_pdf.py

Il sandbox non ha academicons e non puo installarlo; i tracciati pero ce li ho gia,
estratti dal font. Convertirli in PDF da icone vere anche nell'anteprima, identiche
a quelle che il pacchetto disegnerebbe.
"""
import os
import cairosvg
from icons_academic import ACADEMICONS

# regola di riempimento pari-dispari: il glifo Scopus e un quadrato pieno con le due
# lettere ritagliate dentro. Con la regola predefinita le lettere sparirebbero.
SVG = ("<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'>"
       "<path fill='%s' fill-rule='evenodd' d='%s'/></svg>")


def write(outdir, colour="#98461F"):
    made = []
    for name, path in ACADEMICONS.items():
        svg = SVG % (colour, path)
        p = os.path.join(outdir, "ai-%s.pdf" % name)
        cairosvg.svg2pdf(bytestring=svg.encode("utf-8"), write_to=p,
                         output_width=24, output_height=24)
        made.append(p)
    return made


def shim(scale="1.0em", raise_="-0.13em"):
    # 1.0em, non 0.86: misurando l'inchiostro a 400 dpi i glifi academicons uscivano
    # 85 px contro i 99 px dei FontAwesome accanto, cioe il 16% piu piccoli.
    # Il fattore 99/85 applicato a 0.86em da esattamente 1.00em.
    """Sostituisce academicons.sty: stessi nomi di macro, glifi veri."""
    out = [r"\ProvidesPackage{academicons}[glifi veri da PDF]",
           r"\RequirePackage{graphicx}"]
    for name, macro in (("scholar", "aiGoogleScholar"), ("scopus", "aiScopus")):
        out.append(r"\newcommand*{\%s}{\raisebox{%s}{\includegraphics[height=%s]{ai-%s.pdf}}}"
                   % (macro, raise_, scale, name))
    out.append(r"\newcommand*{\aiOrcid}{\textbullet}")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    d = "/sessions/festive-jolly-mccarthy/mnt/outputs/icontest"
    os.makedirs(d, exist_ok=True)
    for p in write(d):
        print("scritto", p, os.path.getsize(p), "byte")
    # controllo visivo: converto in PNG grandi e li guardo, invece di fidarmi
    for name in ACADEMICONS:
        cairosvg.svg2png(bytestring=(SVG % ("#98461F", ACADEMICONS[name])).encode(),
                         write_to=os.path.join(d, "check-%s.png" % name),
                         output_width=200, output_height=200)
    print("controlli in", d)
