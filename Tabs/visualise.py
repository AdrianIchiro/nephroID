# import warnings
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.metrics import plot_confusion_matrix
# from sklearn import tree
# import streamlit as st

# from web_function import train_model

# def app(df, x, y):
#     warnings.filterwarnings('ignore')
#     st.set_option('deprecation.showPyplotGlobalUse', False)
    
#     st.title("Visualisasi Prediksi Batu Ginjal")

#     if st.checkbox("Plot Confusion Matrix"):
#         model, score = train_model(x, y)
#         plt.figure(figsize=(10,6))
#         plot_confusion_matrix(model, x, y, value_format='d')
#         st.pyplot

#     if st.checkbox("Plot Decision Tree"):
#         model, score = train_model(x, y)
#         dot_data = tree.export_graphviz(
#             decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True,
#             feature_names=x.columns, class_names=['nockd', 'ckd']
#         )

#         st.graphviz_chart(dot_data)


# import warnings
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# from sklearn import tree
# import streamlit as st

# from web_function import train_model

# def app(df, x, y):
#     warnings.filterwarnings('ignore')
#     # st.set_option('deprecation.showPyplotGlobalUse', False)
    
#     st.title("Visualisasi Prediksi Batu Ginjal")

#     if st.checkbox("Plot Confusion Matrix"):
#         model, score = train_model(x, y)
#         y_pred = model.predict(x)
#         cm = confusion_matrix(y, y_pred)
#         disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        
#         fig, ax = plt.subplots(figsize=(10, 6))
#         disp.plot(ax=ax)
#         st.pyplot(fig)

#     if st.checkbox("Plot Decision Tree"):
#         model, score = train_model(x, y)
#         dot_data = tree.export_graphviz(
#             decision_tree=model, max_depth=4, out_file=None, filled=True, rounded=True,
#             feature_names=x.columns, class_names=['nockd', 'ckd']
#         )
#         st.graphviz_chart(dot_data)

import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree
import streamlit as st

from web_function import train_model

def app(df, x, y):
    warnings.filterwarnings('ignore')
    st.title("📊 Visualisasi Prediksi Batu Ginjal")
    st.markdown("---")
    
    st.markdown(
        """
        <style>
        .stCheckbox>label {
            font-size: 16px;
            font-weight: bold;
            color: #4A90E2;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    if st.checkbox("📉 Plot Confusion Matrix"):
        model, score = train_model(x, y)
        y_pred = model.predict(x)
        cm = confusion_matrix(y, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        disp.plot(ax=ax, cmap='Blues')
        st.pyplot(fig)
    
    if st.checkbox("🌳 Plot Decision Tree"):
        model, score = train_model(x, y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=4, out_file=None, filled=True, rounded=True,
            feature_names=x.columns, class_names=['No CKD', 'CKD']
        )
        st.graphviz_chart(dot_data)
