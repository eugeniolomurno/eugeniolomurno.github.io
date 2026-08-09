# -*- coding: utf-8 -*-
"""Tabella di traduzione per i .tex del CV che non sono generati da data.py:
pubblicazioni, progetti, riconoscimenti, competizioni. I file generati escono
gia nella lingua giusta e non passano di qui."""

# ordine significativo: le stringhe piu lunghe per prime
TR = [
    # stati di pubblicazione e luoghi: restavano in inglese nel CV italiano
    ("Status: Under Review", "Stato: in revisione"),
    ("Status: Under review", "Stato: in revisione"),
    ("Status: Accepted", "Stato: accettato"),
    ("Status: Published", "Stato: pubblicato"),
    ("Status: In press", "Stato: in stampa"),
    ("Malmo, Sweden", "Malmo, Svezia"),
    ("Lancaster, England", "Lancaster, Inghilterra"),
    ("Grasmere, England", "Grasmere, Inghilterra"),
    ("Aberdeen, Scotland", "Aberdeen, Scozia"),
    ("Kolkata, India", "Calcutta, India"),
    ("Bremen, Germany", "Brema, Germania"),
    ("Bruges, Belgium", "Bruges, Belgio"),
    ("Coimbra, Portugal", "Coimbra, Portogallo"),
    ("Gold Coast, Australia", "Gold Coast, Australia"),
    ("Maastricht, Netherlands", "Maastricht, Paesi Bassi"),
    ("Malaga, Spain", "Malaga, Spagna"),
    ("Xiamen, China", "Xiamen, Cina"),
    ("Angers, France", "Angers, Francia"),
    ("Lille, France", "Lille, Francia"),
    ("Padova, Italy", "Padova, Italia"),
    ("Siena, Italy", "Siena, Italia"),
    ("Lecce, Italy", "Lecce, Italia"),
    ("Bologna, Italy", "Bologna, Italia"),
    ("Workshop on Sustainable Pattern Recognition and Computer Vision Developments",
     "Workshop on Sustainable Pattern Recognition and Computer Vision Developments"),
    # titoli di sezione
    (r"\cvsection{Education}", r"\cvsection{Formazione}"),
    (r"\cvsection{Theses}", r"\cvsection{Tesi}"),
    (r"\cvsection{Journal Publications}", r"\cvsection{Pubblicazioni su rivista}"),
    (r"\cvsection{Conference and Workshop Publications}",
     r"\cvsection{Pubblicazioni a conferenze e workshop}"),
    (r"\cvsection{Awards and Prizes}", r"\cvsection{Riconoscimenti}"),
    (r"\cvsection{Projects}", r"\cvsection{Progetti}"),
    (r"\cvsection{Teaching}", r"\cvsection{Didattica}"),
    (r"\cvsection{MSc Thesis Supervised and Co-Supervised }",
     r"\cvsection{Tesi magistrali seguite e co-seguite}"),
    (r"\cvsection{Competitions}", r"\cvsection{Competizioni}"),
    # titoli di studio e ruoli
    ("PhD in Information Technology - Cum Laude", "Dottorato in Information Technology --- con lode"),
    ("MSc in Computer Science and Engineering", "Laurea magistrale in Ingegneria Informatica"),
    ("BSc in Information Engineering", "Laurea triennale in Ingegneria dell'Informazione"),
    ("Postdoctoral Fellow", "Assegnista di ricerca"),
    (r"PhD Thesis \emph{Cum Laude}", r"Tesi di dottorato \emph{con lode}"),
    ("PhD Thesis", "Tesi di dottorato"),
    ("MSc Thesis", "Tesi magistrale"),
    # contesti didattici
    ("Master Course at MADE S.C.A R.L.", "Corso magistrale presso MADE S.C.A R.L."),
    ("Master Course at Universit\u00e0 Commerciale Luigi Bocconi",
     "Corso magistrale presso l'Universit\u00e0 Bocconi"),
    ("Master Course at Politecnico di Milano", "Corso magistrale al Politecnico di Milano"),
    ("PhD Course at Politecnico di Milano", "Corso di dottorato al Politecnico di Milano"),
    ("Techcamp at Politecnico di Milano", "Techcamp al Politecnico di Milano"),
    ("Master in Data Science \\& Artificial Intelligence by CEFRIEL",
     "Master in Data Science \\& Artificial Intelligence di CEFRIEL"),
    ("NOKIA Master AI\\&ML project by CEFRIEL", "Progetto NOKIA Master AI\\&ML di CEFRIEL"),
    ("SIAE Master AI\\&ML project by CEFRIEL", "Progetto SIAE Master AI\\&ML di CEFRIEL"),
    ("Master Course", "Corso magistrale"),
    # etichette ricorrenti
    ("Teacher Assistant", "Assistente alla didattica"),
    ("Role: Teacher", "Ruolo: Docente"),
    ("Role:", "Ruolo:"),
    ("Supervisor:", "Relatore:"),
    ("Authors:", "Autori:"),
    ("Publisher:", "Editore:"),
    ("Status: Under review", "Stato: in revisione"),
    ("Status: Under Review", "Stato: in revisione"),
    ("Project Homepage:", "Sito del progetto:"),
    ("Framework:", "Ambito:"),
    ("Project ID:", "ID progetto:"),
    ("Paper:", "Articolo:"),
    ("Specialization", "Specializzazione"),
    ("Professors:", "Docenti:"),
    ("Professor:", "Docente:"),
    ("editions", "edizioni"),
    ("Gold medal:", "Medaglia d'oro:"),
    ("Bronze medal:", "Medaglia di bronzo:"),
    ("position on", "posizione su"),
    ("leaderboard", "classifica"),
    # luoghi e date
    ("Milan, Italy", "Milano, Italia"),
    ("Zurich, Switzerland", "Zurigo, Svizzera"),
    ("Paris, France", "Parigi, Francia"),
    ("Grosseto, Italy", "Grosseto, Italia"),
    ("Lancaster, England", "Lancaster, Inghilterra"),
    ("In progress", "in corso"),
    ("January", "gennaio"), ("February", "febbraio"), ("March", "marzo"), ("April", "aprile"),
    ("May", "maggio"), ("June", "giugno"), ("July", "luglio"), ("August", "agosto"),
    ("September", "settembre"), ("October", "ottobre"), ("November", "novembre"),
    ("December", "dicembre"),
    # intestazione
    (r"\position{Postdoctoral Fellow", r"\position{Assegnista di ricerca"),
]


def apply_tr(s):
    for k, v in TR:
        s = s.replace(k, v)
    return s
