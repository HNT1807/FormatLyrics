import streamlit as st
import pyperclip

st.title('Lyrics Formatter')

# Text area for input
lyrics = st.text_area("Enter your lyrics here:", height=250)
formatted_lyrics = ""

# Button to format lyrics
if st.button('Format Lyrics'):
    if lyrics:
        formatted_lyrics = lyrics.replace("\n", "|")
        st.text_area("Formatted Lyrics:", value=formatted_lyrics, height=250, key='output')
    else:
        st.error("Please enter some lyrics to format.")

# Button to copy lyrics
if st.button('Copy Lyrics'):
    if formatted_lyrics:
        pyperclip.copy(formatted_lyrics)
        st.success("Formatted lyrics copied to clipboard!")
    else:
        st.error("There are no formatted lyrics to copy.")
