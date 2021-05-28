import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.model_selection import cross_val_score

import base64


def run_ml():

    classifier_name = st.sidebar.selectbox(
        'Select classifier',
        ('KNN', 'SVM', 'Random Forest', 'Logistic Regression', 'Decision Tree')
    )

    def build_model(df):

        X = df.iloc[:, :-1]  # Using all column except for the last column as X
        y = df.iloc[:, -1]  # Selecting the last column as Y
        st.write('Shape of dataset:', X.shape)
        #st.write('number of classes:', len(np.unique(y)))

        st.markdown('A model is being built to predict the following **Y** variable:')
        st.info(y.name)

        #############################
        def add_parameter_ui(clf_name):
            params = dict()
            if clf_name == 'SVM':
                C = st.sidebar.slider('C', 0.01, 100.0)
                params['C'] = C


            elif clf_name == 'KNN':
                K = st.sidebar.slider('K', 1, 150)
                params['K'] = K


            elif clf_name == 'Logistic Regression':
                Iteration = st.sidebar.slider('Iteration', 10, 100)
                params['Iteration'] = Iteration


            elif clf_name == 'Decision Tree':
                Random_state = st.sidebar.slider('Random_state', 0, 100)
                params['Random_state'] = Random_state

            else:
                max_depth = st.sidebar.slider('max_depth', 2, 15)
                params['max_depth'] = max_depth
                n_estimators = st.sidebar.slider('n_estimators', 1, 100)
                params['n_estimators'] = n_estimators

            return params

        params = add_parameter_ui(classifier_name)

        def get_classifier(clf_name, params):
            clf = None
            if clf_name == 'SVM':
                clf = SVC(C=params['C'])

            elif clf_name == 'KNN':
                clf = KNeighborsClassifier(n_neighbors=params['K'])


            elif clf_name == 'Logistic Regression':
                clf = LogisticRegression(max_iter=params['Iteration'])


            elif clf_name == 'Decision Tree':
                clf = tree.DecisionTreeClassifier(random_state=params['Random_state'])

            else:
                clf = RandomForestClassifier(n_estimators=params['n_estimators'],
                                             max_depth=params['max_depth'], random_state=1234)

            return clf

        def filedownload(df):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
            href = f'<a href="data:file/csv;base64,{b64}" download="model_performance.csv">Download CSV File</a>'
            return href

        clf = get_classifier(classifier_name, params)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

        clf.fit(X_train, y_train)
        cv = cross_val_score(clf, X_train, y_train, cv=5)
        st.write("The cross validation score: ")
        st.info(cv)
        st.write("Mean cross validation score:")
        st.info(cv.mean()*100)

        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        st.write(f'Classifier = {classifier_name}')
        st.write(f'Accuracy =', acc*100)

        y_hat = clf.predict(X)
        list1 = y_hat.tolist()
        #st.write("Output")
        #st.write(y_hat)
        y_hat = pd.DataFrame(y_hat)
        st.write("Complete Results: ")
        results = pd.concat([X, y_hat], axis=1)
        st.write(results)
        st.markdown(filedownload(results), unsafe_allow_html=True)
        st.info("Conclusion: ")
        st.write("Students who Passed:", list1.count(1))
        st.write("Students who Failed:", list1.count(0))
        st.write("Predictions are made at the accuracy of: ",acc*100 )

    # Uploading ...

    st.header("Build your Machine learning model")

    with st.sidebar.header('1. Upload your CSV data'):
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        build_model(df)

    st.sidebar.markdown("""
    [Example CSV input file](https://github.com/Swapnil-Prajapati/Student_dataset/blob/main/file1.csv)
    """)






