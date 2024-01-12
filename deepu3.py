import streamlit as st

st.header('DEEPTHI SUNINAA')
st.write('DEEPU')

# Embedding YouTube video using iframe
video_url = 'https://www.youtube.com/watch?v=PbPODDfgQMA' 
st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
