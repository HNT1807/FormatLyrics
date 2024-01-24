import streamlit as st

st.title('Lyrics Formatter')

# Text area for input
lyrics = st.text_area("Enter your lyrics here:", height=250)

# Button to format lyrics
if st.button('Format Lyrics'):
    if lyrics:
        formatted_lyrics = lyrics.replace("\n", "|")
        st.text_area("Formatted Lyrics:", value=formatted_lyrics, height=250, key='output')
    else:
        st.error("Please enter some lyrics to format.")
