import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the app
st.title('Simple Streamlit App')

# Add a header
st.header('Welcome to My First Streamlit App!')

# Add some text
st.write('This is a simple Streamlit app example.')

# Create a slider
slider_value = st.slider('Select a value', 0, 100, 50)
st.write(f'Slider value: {slider_value}')

# Generate random data
data = np.random.randn(100, 3)
columns = ['Column 1', 'Column 2', 'Column 3']
df = pd.DataFrame(data, columns=columns)

# Display the dataframe
st.write('Here is a sample dataframe:')
st.write(df)

# Create a line chart
st.line_chart(df)

# Add an image with a caption
st.image('https://via.placeholder.com/150', caption='Sample Image')
