import streamlit as st
import streamlit.components.v1 as components

st.title('Lyrics Formatter')

# Text area for input
lyrics = st.text_area("Paste your lyrics here:", height=250)

# Function to create a styled copy button
def create_copy_button(text):
    button_html = f"""
    <style>
        .copy-btn {{
            background-color: transparent;
            border: 1px solid #ccc;
            color: #555;
            padding: 5px 10px;
            border-radius: 5px;
            cursor: pointer;
            text-align: center;
            display: inline-block;
            margin: 0;
        }}
    </style>
    <input type='text' value='{text}' id='copy_input' style='position: absolute; left: -9999px;'>
    <button class='copy-btn' onclick='copyText()'>Copy Formatted Lyrics</button>
    <script>
    function copyText() {{
        var copyText = document.getElementById("copy_input");
        copyText.select();
        document.execCommand("copy");
    }}
    </script>
    """
    components.html(button_html, height=30)

# Button to format lyrics
if st.button('Format Lyrics'):
    if lyrics:
        formatted_lyrics = lyrics.replace("\n", "|")
        st.session_state['formatted_lyrics'] = formatted_lyrics
        st.text_area("Formatted Lyrics:", value=formatted_lyrics, height=250, key='output')
        create_copy_button(formatted_lyrics)
    else:
        st.error("Please enter some lyrics to format.")
elif 'formatted_lyrics' in st.session_state:
    # Display previously formatted lyrics if available
    st.text_area("Formatted Lyrics:", value=st.session_state['formatted_lyrics'], height=250, key='output')
    create_copy_button(st.session_state['formatted_lyrics'])
