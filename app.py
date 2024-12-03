import streamlit as st
import pandas as pd
import numpy as np

##Title of application
st.title("Hello Streamlit")

## Display a simple text
st.write("This is a simpl text")

## Create a dataframe
df=pd.DataFrame({
    'first_col':[1,2,3,4],
    'second_col':[10,20,30,40]
})

## Display the data frame
st.write('Here is the dataframe')
st.write(df)

##create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)