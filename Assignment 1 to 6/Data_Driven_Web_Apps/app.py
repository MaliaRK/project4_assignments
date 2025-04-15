import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data_Driven",page_icon="📝")

st.title("Data Driven App")

st.write("You can upload, analyze, interact charts and filter your data easily.")

uploaded_file = st.file_uploader("choose file", type=['xlsx', 'csv'])

try:  
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            file_read = pd.read_csv(uploaded_file)
            st.dataframe(file_read)
        else:
            file_read = pd.read_excel(uploaded_file)
            st.dataframe(file_read)

        st.session_state.df = file_read

        st.success("File read successfully!")
        st.write(f"Rows: {len(file_read)}, Columns: {len(file_read.columns)}")

except Exception as e:
    st.error(f"Error reading file:", {str(e)})


chart_type = st.selectbox("Select chart type: ", options=('Bar', 'Line', 'Pie'))

if 'df' in st.session_state:
    numeric_cols = st.session_state.df.select_dtypes(include=['number']).columns
    selected_columns = st.selectbox("Select Column", numeric_cols)

    if chart_type == 'Bar':
        fig, ax = plt.subplots()
        ax.bar(st.session_state.df.index, st.session_state.df[selected_columns])
        ax.set_xlabel("Index")
        ax.set_ylabel(selected_columns)
        st.pyplot(fig)
        
    elif chart_type == 'Pie':
        cat_cols = st.session_state.df.select_dtypes(include=['object', 'category']).columns

        if len(cat_cols) > 0:
            selected_columns = st.selectbox("Select Column", cat_cols)
            pie_data = st.session_state.df[selected_columns].value_counts()

            if len(pie_data) > 10:
                st.warning("Too many categories for pie chart (max 10 allowed)")
            elif len(pie_data) == 0:
                st.warning("No data availabe for pie chart")
            else:
                fig, ax = plt.subplots()
                ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
                ax.set_title(f"Distribution of {selected_columns}")
                ax.axis('equal')
                st.pyplot(fig)
        else:
            st.error("No categorical columns available for pie chart.")
    else:
        fig, ax = plt.subplots()
        ax.plot(st.session_state.df[selected_columns])
        ax.set_title(f"Trend of {selected_columns}")
        st.pyplot(fig)
