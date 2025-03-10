import streamlit as st

def show_overview():
    # Título principal de la presentación
    st.title("TV Shows Analysis, Searcher & Much More!")

    st.markdown("""
    This project is an interactive application that allows users to explore a variety of TV shows,
    make predictions about their chances of winning an Emmy, and much more...
    """)

    st.image("https://m.media-amazon.com/images/I/91FReOrpBZL._AC_UF1000,1000_QL80_.jpg", width=800)

    
    st.subheader("1. Data Collection via API")
    st.image("Streamlit/images/tmdb.jpg", width=100)  

    st.write("""
    The first step was **collecting data** using **APIs**. I gathered information about TV shows from all over the world, including:
    - **Title**
    - **Genre**
    - **Release Date**
    - **Rating**
    - **Number of Seasons, Number of Episodes, Episodes Duration**
    - **Platforms**
    - **Cast**
    - **Reviews**

    The data was collected from multiple sources (TMDB API and some datasets from kaggle) to ensure a rich dataset that covers a broad range of shows, including historical data and information on the most recent nominees.
    """)
    st.markdown("---") # para que slga una linea que separe

    st.subheader("2. Exploratory Data Analysis (EDA)")
    st.write("""
    Once the data was collected, I performed **Exploratory Data Analysis (EDA)** to better understand the relationships between different features in the dataset. This process included:
    - **Data Cleaning**: Dealing with missing or inconsistent values, outliers, drop columns, replacing values.
    - **Feature Engineering**: Grouping variables, such as genre and platforms.
    - **Visualizations**: Using **Tableau** to generate insightful and interactive graphs. These included:
             Distribution of series through the years
             - Relation between genre and country
             - Platforms with most series
             - Most recurrent actors etc.
    """)
    st.markdown("---") # para que slga una linea que separe

    st.subheader("3. Machine Learning Models")
    st.image("Streamlit/images/Captura de pantalla 2025-03-03 a las 16.30.30.png", width=800)
    st.write("""
    After preparing the data, I applied several **Machine Learning models** to predict whether a serie is likely to win the **Emmy Awards**. The models used were:
    - **Logistic Regression**
    - **K-Nearest Neighbors (KNN)**
    - **Decision Trees**
    - **Random Forest**
    """)
    st.markdown("---") # para que slga una linea que separe

    st.subheader("4. Sentiment Analysis")
    st.image ("https://getthematic.com/insights/content/images/size/w1384/2024/12/20241012-How-to---Sentiment-analysis-of-reviews.png", width=400)
    st.write("""
    Another part of this analysis involved diving into **public opinion** through **sentiment analysis**. I conducted sentiment analysis on reviews to evaluate how each TV show was perceived by its audience. The goal was to assess the overall sentiment—whether it was **positive**, **negative**, or **neutral**—and understand how viewers rated each show.
    To achieve this, I used **tokenization** and **lemmatization** techniques to process the reviews and extract meaningful insights from the text. Additionally, I employed the **compound score** from the VADER sentiment analysis tool, which helped quantify the overall sentiment in a more comprehensive way.
    To further enhance the analysis, I generated a **WordCloud** that visually represents the most frequently occurring words in the reviews.
             """)
