import streamlit as st
from typing import List, Optional

title = "HHhH"
img = "https://static.streamlit.io/examples/cat.jpg"
productor = "Cédric Jimenez"
actors = ["Jason Clarke", "Rosamund Pike", "Mia Wasikowska"]
writters = ["David Farr", "Audrey Diwan", "Cédric Jimenez"]
year = 2017
resume = "Au début des années 1930, Reinhard Heydrich, militaire renvoyé de la Reichsmarine, rejoint le nazisme sur la suggestion de sa femme Lina. Il devient alors le bras droit du chef de la SS naissante, Heinrich Himmler. Celui-ci le nomme en 1939 à la tête du RSHA, l'organe principal de police secrète et judiciaire du Reich, dont l'une des sections est la célèbre Gestapo. Principal adjoint de Himmler, il est l’un des hommes les plus puissants du régime. En septembre 1941, Hitler lui donne en complément les attributions de vice-gouverneur de Bohême-Moravie, la partie occupée de la Tchécoslovaquie : pour cela, il a des bureaux à Prague où il règne en maître, car le gouverneur en titre Konstantin von Neurath est vieillissant et malade. Comme Heydrich est resté chef du RSHA, il a aussi pour mission de mener à son terme le plan déjà entamé d’extermination des Juifs d’Europe, dit « solution finale de la question juive ». Par ailleurs, ayant quitté la Tchécoslovaquie en 1939, le Tchèque Jan Kubiš et le Slovaque Jozef Gabčík sont engagés depuis 1940 aux côtés de la Résistance pour lutter contre l’occupation allemande. Après un entraînement prolongé en Grande-Bretagne, les deux jeunes soldats se portent volontaires pour une mission secrète aussi importante que risquée : éliminer le général de la police SS Heydrich. La veille de la Saint-Sylvestre 1941, ils sont parachutés à proximité de Prague et, pendant plusieurs mois, sont hébergés par des familles pragoises, dont les Moravec et les Novak. Jan fait ainsi la connaissance d'Anna Novak, mais il sait que sa mission doit passer avant l'amour."
imbdbid = 4190536
rating = 6.7


def show_one_movies(title: str,                     # titre du film
                    img: Optional[str],             # url ou path de l'image (optionelle car peut manquer)
                    productor:list[str],            # liste des producteurs
                    actors: list[str],              # liste des acteurs
                    writters: list[str],            # liste des réalisateurs
                    year: int,                      # année de sortie
                    resume: str,                    # résumé du film
                    imbdbid: int,                   # identifiant IMDB
                    rating: Optional[float] = None  # note du film (optionnelle car pourra manquer sur de nouveaux ajouts afin que le paramètre ne soit pas OBLIGATOIRE)
                    ) -> None:
    

    col_img, col_info = st.columns(2)
    
    with col_img:
        if img:
            st.image(img, width="stretch")                              # width="stretch" permet d'adapter la taille de l'image à la colonne
        else:
            st.write("Image non disponible")
    
    with col_info:
        if title:
            st.markdown(f"**Titre:** {title}")
        if productor:
            st.markdown(f"**De:** {', '.join(productor)}")              # ".join()" permet de transformer une liste en chaîne de caractères en mettant une virgule entre chaque élément
        if actors:
            st.markdown(f"**Avec:** {', '.join(actors)}")
        else: 
            st.markdown("**Avec:** Information non disponible")
        if writters: 
            st.markdown(f"**Par:** {', '.join(writters)}")
        if rating is not None:
            st.markdown(f"**Note:** {rating:.1f}")
        if year:
            st.markdown(f"**Année:** {year}")
    if resume:
        st.markdown(f"**Synopsis:** {resume}")
    else: 
        st.markdown("**Synopsis:** Information non disponible")
            

show_one_movies(title, img, [productor], actors, writters, year, resume, imbdbid, rating)