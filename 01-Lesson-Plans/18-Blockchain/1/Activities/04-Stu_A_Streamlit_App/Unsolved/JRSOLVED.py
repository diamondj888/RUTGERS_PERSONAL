# @TODO: Import the libraries for Pandas and Streamlit
# YOUR CODE HERE!
import streamlit as st
import pandas as pd
# @TODO: Create a title for your application using markdown syntax and the
# Streamlit `write` function.
# YOUR CODE HERE!
st.write("# Python Web App")

# @TODO: Create an opening sentence for your application using regular text and
# the Streamlit `write` function.
# YOUR CODE HERE!
st.write("Hi, you should really check this out and try it!")
# @TODO: Create a Pandas dataframe
# YOUR CODE HERE!
df = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})
# @TODO: Write the Pandas dataframe to the page
# YOUR CODE HERE!

st.write(df)
# @TODO: Create a text input box using the Streamlit `text_input` function.
input_value = st.text_input("Enter a Message")

# @TODO: Save the input as a variable.
# YOUR CODE HERE!

# @TODO: Utilize the Streamlit `button` function to display the text input
# variable created in the prior step to the page.
# YOUR CODE HERE!
if st.button("Display Message"): 
    st.write(input_value)