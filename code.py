import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

st.set_page_config(
    page_title="PolyLingo",
    layout="centered"
)

st.markdown("""
<style>

/* Pink background */

.stApp{
background:#ffc0cb;
}

/* PolyLingo title */

h1.title{
text-align:center !important;
color:#C2185B !important;
font-family:Georgia, serif !important;
font-size:55px !important;
font-weight:bold !important;
margin-bottom:10px !important;
}

/* White text boxes */

textarea{
background:white !important;
color:black !important;
border-radius:12px !important;
font-size:16px !important;
padding:10px !important;
}

/* White dropdown */

div[data-baseweb="select"] > div{
background:white !important;
color:black !important;
border-radius:12px !important;
}

/* Dark pink buttons */

.stButton button{
background:#d63384 !important;
color:white !important;
border:none !important;
border-radius:12px !important;
}

/* Reduce overall width */

.block-container{
max-width:700px;
padding-top:7rem;
}

</style>

""", unsafe_allow_html=True)

st.markdown(
    '<h1 class="title">PolyLingo</h1>',
    unsafe_allow_html=True
)
st.write("Translate text into different languages")

text = st.text_area(
    "Enter English text",
    height=120
)
languages = {
"Chinese ":"zh-CN",
"French ":"fr",
"Hindi ":"hi",
"Japanese ":"ja",
"Korean ":"ko",
"Portuguese ":"pt",
"Russian ":"ru",
"Spanish ":"es"
}

selected_language = st.selectbox(
"Choose language",
list(languages.keys())
)

if st.button("Translate"):

    if text:

        translated = GoogleTranslator(
            source="en",
            target=languages[selected_language]
        ).translate(text)

        st.text_area(
            "Translation",
            translated,
            height=100
        )

        tts = gTTS(
            text=translated,
            lang=languages[selected_language]
        )

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:

            tts.save(fp.name)

            audio_file = open(fp.name, "rb")

            st.audio(audio_file.read())

    else:

        st.info("Please enter some text.")