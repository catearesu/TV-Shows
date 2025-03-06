import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Función para generar el WordCloud de la serie seleccionada
def generate_wordcloud(serie_reviews):
    # Concatenamos todas las reseñas para crear el WordCloud
    text = " ".join(serie_reviews)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)


# Función para mostrar las reseñas
def user_reviews():
    st.header("TV-Shows Reviews")
    st.write("Let's see what other people think about your favourite serie 🤔")
    df_reviews = pd.read_csv("Dataset/df_reseñas_wordcloud.csv")  

    # Seleccionamos la serie
    series_list = df_reviews["Title"].unique()
    selected_series = st.selectbox(":tv: Please select a Tv-Show:", options= ["Select a TV-Show"]+ series_list.tolist())

    if selected_series != "Select a TV-Show":
        # Filtramos las reseñas para la serie seleccionada
        filtered_df = df_reviews[df_reviews["Title"] == selected_series]

        # Filtramos reseñas positivas y negativas
        positive_reviews = filtered_df[filtered_df["Sentiment_Lemmatized"] == 1]
        negative_reviews = filtered_df[filtered_df["Sentiment_Lemmatized"] == -1]
        neutral_reviews = filtered_df[filtered_df["Sentiment_Lemmatized"]== 0]

        # Mostramos el WordCloud de la serie seleccionada
        st.subheader("WordCloud")
        generate_wordcloud(filtered_df["Lemmatized_reviews"])

        # RESEÑAS POSITIVAS
        if not positive_reviews.empty:  # Si hay reseñas positivas
            random_positive_review = positive_reviews.sample(1)["Reviews"].values[0] # pongo el values si no me aparece mal el formato
            st.subheader("Positive Review 👍")
            st.write(random_positive_review)
        
        # RESEÑAS NEUTRAS
        if not neutral_reviews.empty:  # Si hay reseñas neutras
            random_neutral_review = neutral_reviews.sample(1)["Reviews"].values[0]
            st.subheader("Neutral Review 😐")
            st.write(random_neutral_review)

        # RESEÑAS NEGATIVAS
        if not negative_reviews.empty:  # Si hay reseñas negativas
            random_negative_review = negative_reviews.sample(1)["Reviews"].values[0]
            st.subheader("Negative Review 👎")
            st.write(random_negative_review)
        else:  # Si no hay reseñas negativas y tampoco neutras
            if not positive_reviews.empty and neutral_reviews.empty:
                st.subheader("No Negative Reviews Found 😀")
                st.write("This show is awesome!!!")