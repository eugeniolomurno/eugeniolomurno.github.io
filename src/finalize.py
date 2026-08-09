# -*- coding: utf-8 -*-
"""Genera l'index.html definitivo: struttura Compatta + il blocco SEO che i prototipi non avevano."""
import os, re
import data as D
import build

import os as _os
# Percorsi ricavati dalla posizione di questo file: il generatore funziona
# ovunque sia il repository, senza percorsi assoluti da aggiornare a mano.
_HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.dirname(_HERE)                     # la radice del sito


SITE = "https://eugeniolomurno.github.io/"

DESC = ("Eugenio Lomurno — Postdoctoral Fellow at AIRLab, DEIB, Politecnico di Milano. "
        "Generative and privacy-preserving deep learning, synthetic data, "
        "multimodal learning, edge-oriented neural architecture search.")

SEO = '''<meta name="description" content="%(desc)s">
<meta name="author" content="Eugenio Lomurno">
<link rel="canonical" href="%(site)s">

<!-- anteprime social: LinkedIn, X, Slack, WhatsApp -->
<meta property="og:type" content="profile">
<meta property="og:url" content="%(site)s">
<meta property="og:title" content="Eugenio Lomurno — Postdoctoral Fellow, Politecnico di Milano">
<meta property="og:description" content="%(desc)s">
<meta property="og:image" content="%(site)sphoto.jpg">
<meta property="og:image:alt" content="Portrait of Eugenio Lomurno">
<meta property="og:locale" content="en_GB">
<meta property="og:locale:alternate" content="it_IT">
<meta property="profile:first_name" content="Eugenio">
<meta property="profile:last_name" content="Lomurno">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Eugenio Lomurno — Postdoctoral Fellow, Politecnico di Milano">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(site)sphoto.jpg">

<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='22' fill='%%2398461F'/><text x='50' y='71' font-family='Georgia,serif' font-size='56' font-weight='700' fill='%%23FFFDF8' text-anchor='middle'>EL</text></svg>">

<!-- dati strutturati: aiuta i motori a legare profilo, ORCID, Scholar e Scopus alla stessa persona -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Eugenio Lomurno",
  "url": "%(site)s",
  "image": "%(site)sphoto.jpg",
  "email": "mailto:eugenio.lomurno@polimi.it",
  "jobTitle": "Postdoctoral Fellow",
  "identifier": "https://orcid.org/0000-0003-4007-3207",
  "worksFor": {
    "@type": "CollegeOrUniversity",
    "name": "Politecnico di Milano",
    "department": {"@type": "Organization",
      "name": "Dipartimento di Elettronica, Informazione e Bioingegneria (DEIB) — AIRLab"}
  },
  "alumniOf": {"@type": "CollegeOrUniversity", "name": "Politecnico di Milano"},
  "address": {"@type": "PostalAddress", "addressLocality": "Milano", "addressCountry": "IT"},
  "knowsAbout": ["Generative Deep Learning","Synthetic Dataset Generation",
    "Privacy-Preserving Deep Learning","Multimodal Deep Learning",
    "Neural Architecture Search","Healthcare AI"],
  "sameAs": [
    "https://scholar.google.com/citations?user=7VpjbGoAAAAJ",
    "https://www.scopus.com/authid/detail.uri?authorId=57226274677",
    "https://orcid.org/0000-0003-4007-3207",
    "https://github.com/eugeniolomurno",
    "https://www.linkedin.com/in/eugenio-lomurno-a28b12162/"
  ]
}
</script>
''' % {"desc": DESC, "site": SITE}


def main():
    html = build.render_layout("2-compatto", build.LAYOUTS["2-compatto"])

    # titolo senza il suffisso della variante
    html = html.replace("<title>Eugenio Lomurno — Postdoctoral Fellow (Compact)</title>",
                        "<title>Eugenio Lomurno — Postdoctoral Fellow, Politecnico di Milano</title>")
    # blocco SEO subito dopo il viewport
    html = html.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
                        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' + SEO, 1)
    # etichetta della variante: fuori dal sito vero
    html = re.sub(r'<span class="badge-note"[^>]*>[^<]*</span>', "", html)

    out = os.path.join(ROOT, "index.html")
    open(out, "w", encoding="utf-8").write(html)
    print("scritto", out, len(html), "byte")


if __name__ == "__main__":
    main()
