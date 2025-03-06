import streamlit as st
import math
import joblib

def predict_emmy():
    # Cargamos el modelo
    rf_best_model = joblib.load("/Users/caterina/IronHack/Projects/TV-Shows/Dataset/rf_best_model.pkl")
    st.header("Emmy Prediction for TV Shows")
    st.image("https://gifdb.com/images/high/winner-benedict-townsend-ciee9zgfd6zuq8w8.gif", width=600)

    st.markdown("---") # para que slga una linea que separe
    st.write("""
    This section aims to predict the winners of the **Emmy Awards** using **Machine Learning** techniques. The idea is to leverage historical data on series nominated for the Emmy Awards and apply predictive models to determine whether a serie is likely to win.
    """)
    st.subheader("Data Preprocessing")
    st.write("""
    Data preprocessing is crucial to preparing the right features for analysis. Steps followed:
    - **Data Cleaning**: Dealing with missing or inconsistent values, outliers, drop columns, replacing values (mean) etc.
    - **Feature Scaling**: Normalizing or standardizing the data to ensure all features are comparable.
    - **Encoding**: Converting categorical variables (like genre) into numerical formats for the models.
    - **Feature Selection**: Choosing the most relevant variables that influence the award prediction.
    """) 
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("*Anova*")
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/Captura de pantalla 2025-03-03 a las 21.48.54.png", width=300)
    with col2:
        st.markdown("*Chi Cuadrado*")
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/Captura de pantalla 2025-03-03 a las 21.48.06.png", width=300)

    # SMOTE
    st.subheader("Handling Imbalanced Data with SMOTE")
    st.write("""
    One of the key challenges in predicting Emmy Award winners is the **data imbalance** in the dataset. For instance, we have far more losing nominations than winning ones. To address this, I used **SMOTE (Synthetic Minority Over-sampling Technique)**.
    
    SMOTE works by generating synthetic samples for the minority class, thereby balancing the dataset and helping the models generalize better. This is especially helpful for improving the accuracy of classifiers when faced with highly imbalanced data.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("*Before Smote*")
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/Captura de pantalla 2025-03-03 a las 21.43.34.png", width=300)
    with col2:
        st.markdown("*After applying Smote*")
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/Captura de pantalla 2025-03-03 a las 21.40.03.png", width=300)
    
    # MACHINE LEARNING MODELS
    st.subheader("Machine Learning Models Used")
    st.write ("**Precision**: Precision is the ratio of true positive predictions to the total positive predictions. It measures the accuracy of positive predictions.")
    st.write("**Recall** (Sensitivity): Recall measures the ratio of true positive predictions to the total actual positives. It calculates the ability of the classifier to find all positive instances.")
    st.write("**F1-Score**: The F1-score is the harmonic mean of precision and recall. It gives a balance between precision and recall.")
    st.write("**Accuracy**: Accuracy is the ratio of correctly predicted observations to the total observations. It gives an overall performance of the model.")
    st.write("Among all these scores, I considered more appropriate to use the *ACCURACY*.")
    st.write("To predict the Emmy winners, I used different **Machine Learning** models:")

    # LOGISTIC REGRESSION
    st.markdown("- **<span style='font-size: 20px;'><b>Logistic Regression</b></span>**: Ideal for binary classification, such as predicting whether a series will win or not.", unsafe_allow_html=True)
    st.write ("The model assumes that the relationship between the features and the log-odds of the response variable is linear. It also assumes independence of observations and absence of multicollinearity")
    st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/Captura de pantalla 2025-03-03 a las 20.26.42.png")
    col1, col2 = st.columns(2)
    with col1:
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/confmatrixlogregress.png", caption="Confusion Matrix", width=300)
    with col2:
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/roccurvelogregress.png", caption="Roc Curve", width=300)
    st.markdown("---") # para que slga una linea que separe

    # KNN 
    st.markdown("- **<span style='font-size: 20px;'><b>K-Nearest Neighbors (KNN)</b></span>**: A non-parametric algorithm that classifies based on the nearest neighbors in the feature space.", unsafe_allow_html=True)
    st.write('''*Problems*
- *Noisy Data*: KNN Performs poorly with a lot of irrelevant features or outliers
- *Curse of Dimensionality*: Degrade significantly as the number of dimensions increases''')
    st.markdown("*Hyperparameter Tuning*")
    # accuracy score y best parameters
    st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/Captura de pantalla 2025-03-04 a las 19.34.43.png")
    col1, col2 = st.columns(2)
    with col1:
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/knnconfmatrix.png", caption="Confusion Matrix", width=300)
    with col2:
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/knnroccurve.png", caption="Roc Curve", width=300)
    st.markdown("---") # para que slga una linea que separe

    # DECISION TREE
    st.markdown("- **<span style='font-size: 20px;'><b>Decision Tree</b></span>**: A model that works with stratifying or segmenting the predictor space into a number of binary decisions to make the prediction. Each binary split consists of a decision rule which either sends us left or sends us right.", unsafe_allow_html=True)
    st.markdown("*Hyperparameter Tuning*")
    # best parameters
    st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/Captura de pantalla 2025-03-04 a las 19.51.21.png")
    # accuracy score
    st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/Captura de pantalla 2025-03-03 a las 20.23.55.png")
    col1, col2 = st.columns(2)
    with col1:
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/dtconfmatr.png", caption="Confusion Matrix", width=300)
    with col2:
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/dtroccurve.png", caption="Roc Curve", width=300)
    st.image ("//Users/caterina/IronHack/Projects/TV-Shows/images/dt.png") # decision tree
    st.markdown("---") # para que slga una linea que separe

    # RANDOM FOREST
    st.markdown("- **<span style='font-size: 20px;'><b>Random Forest</b></span>**: An ensemble of decision trees, which improves the performance by averaging the predictions of multiple trees to reduce overfitting and increase robustness.", unsafe_allow_html=True)
    st.markdown("*Hyperparameter Tuning*")
       #Best parameters: {'max_depth': 20, 'min_samples_split': 2, 'n_estimators': 50}
    # Best parameters
    st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/Captura de pantalla 2025-03-03 a las 20.22.05.png")
    # accuracy score
    st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/Captura de pantalla 2025-03-03 a las 20.21.35.png")
    col1, col2 = st.columns(2)
    with col1:
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/rfconfmatr.png", caption="Confusion Matrix", width=300)
    with col2:
        st.image("/Users/caterina/IronHack/Projects/TV-Shows/images/rfroccurve.png", caption="Roc Curve", width=300)
    st.markdown("---") # para que slga una linea que separe


    st.write("""
    Let's try to use **Random Forest** to predict whether a TV-Show has a chance to win an Emmy
    """)
    # Pedimos los inputs al usuario
    rating = int(st.number_input("What rating does the show have? (1 to 10): ", min_value=1.00))
    if rating < 1 or rating > 10:
        st.error("Please insert a rating between 1 and 10.")
        st.stop()  # deja de ejectuar el codigo si el rating es menor que 1 o mayor que 10
    popularity = int(st.number_input("How popular is it?: "))
    vote_count = int(st.number_input("How many votes does it have?: "))
    seasons = int(st.number_input("How many seasons?: "))
    episodes = int(st.number_input("How many episodes: "))
    duration = int(st.number_input("What's the average duration? (in minutes): "))
    positioncat = st.selectbox("Which genre is it?", ["Comedy", "Drama", "Family", "Animation", "Entertainment", "Action & Adventure", "Documentary"])
    # transformo los datos
    popularity_log = math.log(popularity) if popularity > 0 else float("nan")
    vote_count_log = math.log(vote_count) if vote_count > 0 else float("nan")
    seasons_log = math.log(seasons) if seasons > 0 else float("nan")
    episodes_log = math.log(episodes) if episodes > 0 else float("nan")
    duration_log = math.log(duration) if duration > 0 else float("nan")
    # One-hot encoding para los géneros
    if positioncat.lower() == "comedy":
        genero = [1, 0, 0, 0]
    elif positioncat.lower() == "drama":
        genero = [0, 1, 0, 0]
    elif positioncat.lower() == "family":
        genero = [0, 0, 1, 0]
    elif positioncat.lower() == "animation":
        genero = [0, 0, 0, 1]
    else:
        genero = [0, 0, 0, 0]  # Si el género no coincide con drama, comedy, family o animation lo marcamos como todos ceros.

    # Preparamos las features en el formato adecuado para la predicción
    features = [rating, popularity_log, vote_count_log, seasons_log, episodes_log, duration_log] + genero

    # Realizamos la predicción
    if st.button("Predict"):
        if rf_best_model.predict([features])[0] == 1:
            st.success("**The show has a chance to win an Emmy!**")
            st.image("https://i.gifer.com/embedded/download/D9SC.gif", width=400)

        else:
            st.error("**The show doesn't have a chance to win an Emmy**")
            st.image("https://i.gifer.com/origin/2b/2bef5dcb100766198394e5bd1bcff395_w200.gif", width=200)
            st.image("https://i.gifer.com/9GO.gif", width=400)