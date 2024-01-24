import streamlit as st
import html

def format_lyrics(lyrics):
    return lyrics.replace("\n", "|")

st.title('Lyrics Formatter')

# Text area for input
lyrics = st.text_area("Enter your lyrics here:", height=250)

# Button to format lyrics
if st.button('Format Lyrics'):
    if lyrics:
        # Format the lyrics
        formatted_lyrics = format_lyrics(lyrics)
        st.session_state['formatted_lyrics'] = formatted_lyrics

        # Display formatted lyrics in a text area
        st.text_area("Formatted Lyrics:", value=formatted_lyrics, height=250, key='output')

        # Escaping HTML characters in formatted lyrics for safe HTML embedding
        formatted_lyrics_html = html.escape(formatted_lyrics)

        # Create a button for copying to clipboard
        copy_button = f'''
            <button onclick="navigator.clipboard.writeText('{formatted_lyrics_html}')">Copy Formatted Lyrics</button>
        '''
        st.markdown(copy_button, unsafe_allow_html=True)
    else:
        st.error("Please enter some lyrics to format.")
elif 'formatted_lyrics' in st.session_state:
    # Display the previously formatted lyrics if available
    st.text_area("Formatted Lyrics:", value=st.session_state['formatted_lyrics'], height=250, key='output')
    formatted_lyrics_html = html.escape(st.session_state['formatted_lyrics'])
    copy_button = f'''
        <button onclick="navigator.clipboard.writeText('{formatted_lyrics_html}')">Copy Formatted Lyrics</button>
    '''
    st.markdown(copy_button, unsafe_allow_html=True)
