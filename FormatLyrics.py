import streamlit as st
import html

st.title('Lyrics Formatter')

# Text area for input
lyrics = st.text_area("Enter your lyrics here:", height=250)

# Button to format lyrics
if st.button('Format Lyrics'):
    if lyrics:
        # Format the lyrics
        formatted_lyrics = lyrics.replace("\n", "|")
        st.session_state['formatted_lyrics'] = formatted_lyrics

        # Display formatted lyrics in a text area
        st.text_area("Formatted Lyrics:", value=formatted_lyrics, height=250, key='output')

        # JavaScript for Copy to Clipboard functionality
        copy_js = f"""
            <textarea id="text_to_copy" style="opacity: 0; position: absolute; top: -9999px;">{formatted_lyrics}</textarea>
            <button onclick="var copyText = document.getElementById('text_to_copy'); copyText.select(); document.execCommand('copy');">Copy Formatted Lyrics</button>
        """
        st.markdown(copy_js, unsafe_allow_html=True)
    else:
        st.error("Please enter some lyrics to format.")
elif 'formatted_lyrics' in st.session_state:
    # Display previously formatted lyrics if available
    st.text_area("Formatted Lyrics:", value=st.session_state['formatted_lyrics'], height=250, key='output')

    # JavaScript for Copy to Clipboard functionality
    copy_js = f"""
        <textarea id="text_to_copy" style="opacity: 0; position: absolute; top: -9999px;">{st.session_state['formatted_lyrics']}</textarea>
        <button onclick="var copyText = document.getElementById('text_to_copy'); copyText.select(); document.execCommand('copy');">Copy Formatted Lyrics</button>
    """
    st.markdown(copy_js, unsafe_allow_html=True)
