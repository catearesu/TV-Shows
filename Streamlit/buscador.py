
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import streamlit.components.v1 as components



def tv_shows_finder():
    st.header("TV-Shows Searcher")
    st.write("Here you can explore content of more than 9000 TV-Shows from all over the world!!!")
    st.image("https://acf.geeknetic.es/imagenes/auto/2023/5/2/h3o-ahorra-dinero-planificando-ver-tus-series-favoritas.jpg", width=550)
    df_finder= pd.read_csv("Streamlit/data/df_buscador_streamlit2.csv")
    st.write ("#### How would you like to search?")
    search_type = st.radio("Select an option",
                                options= ["Search by Name", "Search by Filters"])
    if search_type == "Search by Name":
        search_by_name(df_finder)  
    elif search_type == "Search by Filters":
        search_by_filters(df_finder)  

# buscamos una serie cualquiera por filtros
def search_by_filters(df_finder):
        # ponemos los filtros 
        # Filtro por GENERO
        df_finder= df_finder.dropna(subset=["Genero"])
        genero_opciones = df_finder["Genero"].str.split(', ').explode().unique()
        selected_generos = st.sidebar.multiselect("Select genres:", options=["All"] + list(genero_opciones))
        if selected_generos and "All" not in selected_generos:
            df_finder = df_finder[df_finder["Genero"].apply(lambda x: any(genero in x for genero in selected_generos))]

        # Filtro por RATING
        rating_min, rating_max = df_finder["Rating"].min(), df_finder["Rating"].max()
        selected_rating = st.sidebar.slider(
            "Select a rating range:",
            min_value=int(rating_min),
            max_value=int(rating_max),
            value=(int(rating_min))
        )
        df_finder = df_finder[df_finder["Rating"]>= selected_rating]
        df_finder= df_finder[df_finder["Rating"]<= rating_max]

        # Filtro por IDIOMA
        idioma_opciones = df_finder["Original Language"].unique()
        selected_idioma = st.sidebar.multiselect("Select languages:", options=["All"] + list(idioma_opciones))
        if selected_idioma and "All" not in selected_idioma:
            df_finder = df_finder[df_finder["Original Language"].apply(lambda x: any(idioma in x for idioma in selected_idioma))]

        # Filtro por AÑO DE ESTRENO
        year_min, year_max = pd.to_datetime(df_finder["First Air Date"]).dt.year.min(), pd.to_datetime(df_finder["First Air Date"]).dt.year.max()
        selected_year = st.sidebar.slider(
            "Select release year range:",
            min_value=int(year_min),
            max_value=int(year_max),
            value=(int(year_min), int(year_max))
        )
        df_finder = df_finder[df_finder["First Air Date"].apply(lambda x: pd.to_datetime(x).year).between(selected_year[0], selected_year[1])]

        # Filtro por PRODUCCIÓN
        produccion = df_finder["In production"].unique()
        selected_produccion = st.sidebar.selectbox("In production", options=["All"] + list(produccion))
        if selected_produccion != "All":
            df_finder = df_finder[df_finder["In production"] == selected_produccion]

        # Filtro por NUMERO DE TEMPORADAS
        st.sidebar.markdown('<p style="font-size: 14px;">Select season length:</p>', unsafe_allow_html=True)
        short = st.sidebar.checkbox("Short (up to 3)")
        medium = st.sidebar.checkbox("Medium (between 4 and 8)")
        long = st.sidebar.checkbox("Long (more than 8)")
        if short:
            df_finder = df_finder[df_finder["Number of Season"] <= 3]
        elif medium:
            df_finder = df_finder[(df_finder["Number of Season"] >= 4) & (df_finder["Number of Season"] <= 8)]
        elif long:
            df_finder = df_finder[df_finder["Number of Season"] >= 9]

        # Filtro por DURACIÓN EPISODIOS
        duration_min, duration_max = df_finder["Episode Duration"].min(), df_finder["Episode Duration"].max()
        selected_duration = st.sidebar.slider(
            "Select episodes duration (min):",
            min_value=int(duration_min),
            max_value=int(duration_max),
            value=(int(duration_min), int(duration_max))
        )
        df_finder = df_finder[df_finder["Episode Duration"].between(selected_duration[0], selected_duration[1])]
        
        # Filtro por ACTOR
        df_actores = df_finder.dropna(subset=["Cast"])
        # Extraemos los actores únicos
        actor_opciones = df_actores["Cast"].str.split(', ').explode().dropna().unique()
        selected_actors = st.sidebar.multiselect("Select actors:", options=["All"] + list(actor_opciones))
        if selected_actors and "All" not in selected_actors:
            df_finder = df_finder[df_finder["Cast"].apply(lambda x: isinstance(x, str) and any(actor in x for actor in selected_actors))]
    
        if len(df_finder) == 0:
            st.write("No TV Shows match the selected filters. Try changing your filters")
        else:
            st.write(f"Found {len(df_finder)} TV-Shows")
        if len(df_finder)!=1:
            # muestro el dataframe de las primeras 10 series ordenadas por rating
            df_finder_filtered= df_finder.sort_values(by=["Rating", "Vote Count"], ascending= False).head(10)
            df_finder_filtered = df_finder_filtered.set_index("Title")
            df_finder_filtered["Rating"]= df_finder_filtered["Rating"].round(1)
            st.dataframe(df_finder_filtered[["Genero", "Rating", "Original Language"]])
            # mostrar los detalles de la serie al hacer click en la serie
            selected_serie = st.selectbox("Select a TV-Show for more details: ", options= ["Select a TV-Show"]+ df_finder["Title"].tolist())
            if selected_serie != "Select a TV-Show":
                    serie_info = df_finder[df_finder["Title"] == selected_serie] 
                            
                    for index, row in serie_info.iterrows():
                        st.subheader(row['Title'])
                        poster_url = row['Poster']
                        if poster_url:
                            st.image(poster_url, width=200)
                            
                        if pd.notna(row['Synopsis']):
                            st.write(f"📜 **Synopsis:** {row['Synopsis']}")
                            
                        if pd.notna(row['Genero']):
                            st.write(f"🎬 **Genre:** {row['Genero']}")
                            
                        st.write(f"📅 **Release date:** {row['First Air Date']}")
                            
                        if pd.notna(row['Rating']):
                            st.write(f"⭐ **Rating:** {round(row['Rating'], 1)}")
                            
                        st.write(f"📆 **Number of Seasons:** {row['Number of Season']}")
                        st.write(f"🎥 **Number of Episodes:** {row['Number of Episodes']}")
                        st.write(f"⏱️ **Episode Duration:** {row['Episode Duration']} min")
                        st.write(f"🗣️ **Original Language:** {row['Original Language']}")
                        st.write(f"🌐 **Origin Country:** {row['Origin Country']}")
                            
                        if row['Where to Watch'] != "No platforms available":
                            st.write(f"📱 **Platforms:** {row['Where to Watch']}")
                            
                        if pd.notna(row['Cast']):
                            st.write(f"🎭 **Cast:** {row['Cast']}")
                            
                        if row['Trailer'] != "No trailer available":
                            st.video(row['Trailer'])
        else: # si la serie que filtro coincide exactamente con una sola serie
            st.subheader(df_finder["Title"].values[0])
            poster_url = df_finder["Poster"].values[0]
            if poster_url:
                st.image(poster_url, width=200) 
            if pd.notna(df_finder["Synopsis"].values[0]):
                st.write(f"**Synopsis:** {df_finder['Synopsis'].values[0]}")
            st.write(f"**Genre:** {df_finder['Genero'].values[0]}")
            st.write(f"**Release date:** {df_finder['First Air Date'].values[0]}")
            if pd.notna(df_finder["Rating"].values[0]):
                st.write(f"**Rating:** {round(df_finder['Rating'].values[0],1)}")
            st.write(f"**Number of Seasons:** {df_finder['Number of Season'].values[0]}")
            st.write(f"**Number of Episodes:** {df_finder['Number of Episodes'].values[0]}")
            st.write(f"**Episode Duration:** {df_finder['Episode Duration'].values[0]} min")
            st.write(f"**Original Language:** {df_finder['Original Language'].values[0]}")
            st.write(f"**Origin Country:** {df_finder['Origin Country'].values[0]}")
            if df_finder["Where to Watch"].values[0]!= "No platforms available":
                st.write(f"**Platforms:** {df_finder['Where to Watch'].values[0]}")
            if pd.notna(df_finder["Cast"].values[0]):
                st.write(f"**Cast:** {df_finder['Cast'].values[0]}")
            if df_finder["Trailer"].values[0] != "No trailer available":
                st.video(df_finder["Trailer"].values[0])
                 
                    
# buscamos la serie x nombre
def search_by_name(df_finder):
        search = st.text_input("Find a TV-Show:")
        if search:
            df_finder =  df_finder[df_finder["Title"].str.contains(search, case=False, na=False)]
        
            # Si se encuentra exactamente una serie
            if len(df_finder) == 1:
                st.subheader(df_finder["Title"].iloc[0])
                poster_url = df_finder["Poster"].iloc[0]
                if poster_url:
                    st.image(poster_url, width=200) 
                if pd.notna(df_finder["Synopsis"].iloc[0]):
                    st.write(f"📜 **Synopsis:** {df_finder['Synopsis'].iloc[0]}")
                if pd.notna(df_finder["Genero"].iloc[0]):
                    st.write(f"🎬 **Genre:** {df_finder['Genero'].iloc[0]}")
                st.write(f"📅 **Release date:** {df_finder['First Air Date'].iloc[0]}")
                if pd.notna(df_finder["Rating"].iloc[0]):
                    st.write(f"⭐ **Rating:** {round(df_finder['Rating'].iloc[0], 1)}")
                st.write(f"📆 **Number of Seasons:** {df_finder['Number of Season'].iloc[0]}")
                st.write(f"🎥 **Number of Episodes:** {df_finder['Number of Episodes'].iloc[0]}")
                st.write(f"⏱️ **Episode Duration:** {df_finder['Episode Duration'].iloc[0]} min")
                st.write(f"🗣️ **Original Language:** {df_finder['Original Language'].iloc[0]}")
                st.write(f"🌐 **Origin Country:** {df_finder['Origin Country'].iloc[0]}")
                if df_finder["Where to Watch"].iloc[0]!= "No platforms available":
                        st.write(f"📱 **Platforms:** {df_finder['Where to Watch'].iloc[0]}")
                if pd.notna(df_finder["Cast"].iloc[0]):
                        st.write(f"🎭 **Cast:** {df_finder['Cast'].iloc[0]}")
                if df_finder["Trailer"].iloc[0] != "No trailer available":
                        st.video(df_finder["Trailer"].iloc[0])
            elif len(df_finder)>1:
                # mostramos los resultados
                st.write(f"Found {len(df_finder)} TV-Shows")
                df_finder_filtered= df_finder.sort_values(by=["Rating", "Vote Count"], ascending= False).head(10)
                df_finder_filtered = df_finder_filtered.set_index("Title")
                df_finder_filtered["Rating"]= df_finder_filtered["Rating"].round(1)
                st.dataframe(df_finder_filtered[["Genero", "Rating", "Original Language"]])
            
                # mostrar los detalles de la serie al hacer click en la serie
                selected_serie = st.selectbox("Select a TV-Show for more details: ", options= ["Select a TV-Show"]+ df_finder["Title"].tolist())
                if selected_serie != "Select a TV-Show":
                        serie_info = df_finder[df_finder["Title"] == selected_serie] 
                        # itero por si hay una serie que se llama igual pero son diferentes (ej. the office) 
                        # así me muestra los detalles de todas las que se llaman the office   
                        for index, row in serie_info.iterrows():
                            st.subheader(row['Title'])
                            poster_url = row['Poster']
                            if poster_url:
                                st.image(poster_url, width=200)
                            
                            if pd.notna(row['Synopsis']):
                                st.write(f"📜 **Synopsis:** {row['Synopsis']}")
                            
                            if pd.notna(row['Genero']):
                                st.write(f"🎬 **Genre:** {row['Genero']}")
                            
                            st.write(f"📅 **Release date:** {row['First Air Date']}")
                            
                            if pd.notna(row['Rating']):
                                st.write(f"⭐ **Rating:** {round(row['Rating'], 1)}")
                            
                            st.write(f"📆 **Number of Seasons:** {row['Number of Season']}")
                            st.write(f"🎥 **Number of Episodes:** {row['Number of Episodes']}")
                            st.write(f"⏱️ **Episode Duration:** {row['Episode Duration']} min")
                            st.write(f"🗣️ **Original Language:** {row['Original Language']}")
                            st.write(f"🌐 **Origin Country:** {row['Origin Country']}")
                            
                            if row['Where to Watch'] != "No platforms available":
                                st.write(f"📱 **Platforms:** {row['Where to Watch']}")
                            
                            if pd.notna(row['Cast']):
                                st.write(f"🎭 **Cast:** {row['Cast']}")
                            
                            if row['Trailer'] != "No trailer available":
                                st.video(row['Trailer'])

            else:
                st.write(f"No TV-Shows found")

                 