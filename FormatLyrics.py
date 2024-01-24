import streamlit as st

st.title('Lyrics Formatter')

# Initialize session state for formatted lyrics
if 'formatted_lyrics' not in st.session_state:
    st.session_state['formatted_lyrics'] = ''

# Text area for input
lyrics = st.text_area("Enter your lyrics here:", height=250)

# Button to format lyrics
if st.button('Format Lyrics'):
    if lyrics:
        st.session_state['formatted_lyrics'] = lyrics.replace("\n", "|")
        st.text_area("Formatted Lyrics:", value=st.session_state['formatted_lyrics'], height=250, key='output')
    else:
        st.error("Please enter some lyrics to format.")

# Button to copy lyrics
if st.button('Copy Formatted Lyrics'):
    if st.session_state['formatted_lyrics']:
        # Create a temporary textarea to hold the formatted text
        copy_js = f"""
            <textarea id="temp_textarea" style="position: absolute; left: -9999px;">{st.session_state['formatted_lyrics']}</textarea>
            <script>
            var textarea = document.getElementById("temp_textarea");
            textarea.select();
            document.execCommand("copy");
            textarea.remove();
            </script>
        """
        st.markdown(copy_js, unsafe_allow_html=True)
        st.success("Formatted lyrics copied to clipboard!")
    else:
        st.error("There are no formatted lyrics to copy.")

