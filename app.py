import streamlit as st
import requests

# PAGE CONFIG
st.set_page_config(
    page_title="Social Post Generator",
    page_icon="🚀",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: #38bdf8;
    margin-top: 10px;
}

.sub-title {
    text-align: center;
    color: #cbd5e1;
    font-size: 20px;
    margin-bottom: 40px;
}

.input-box {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
}

.output-box {
    background: linear-gradient(to right, #2563eb, #1d4ed8);
    padding: 25px;
    border-radius: 20px;
    margin-top: 25px;
    color: white;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
}

.history-box {
    background-color: #334155;
    padding: 18px;
    border-radius: 15px;
    margin-bottom: 15px;
    color: white;
}

.stButton button {
    width: 100%;
    border-radius: 12px;
    height: 3.2em;
    background: linear-gradient(to right, #38bdf8, #2563eb);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton button:hover {
    transform: scale(1.02);
    transition: 0.2s;
}

.feature-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    '<div class="main-title">🚀 Social Post Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Generate viral captions, hashtags & image ideas instantly using AI ✨</div>',
    unsafe_allow_html=True
)

# FEATURE CARDS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
        <h3>📝 Captions</h3>
        <p>Create catchy social media captions instantly</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
        <h3>#️⃣ Hashtags</h3>
        <p>Generate trending hashtags automatically</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
        <h3>🎨 Image Ideas</h3>
        <p>Get creative visual concepts for your posts</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# INPUT SECTION
st.markdown('<div class="input-box">', unsafe_allow_html=True)

st.subheader("📌 Create Your Post")

col1, col2 = st.columns(2)

with col1:
    topic = st.text_input(
        "Enter Topic",
        placeholder="Example: Pongal Sale"
    )

with col2:
    tone = st.selectbox(
        "Select Tone",
        [
            "catchy",
            "funny",
            "professional",
            "emotional"
        ]
    )

st.markdown('</div>', unsafe_allow_html=True)

# SESSION STATE
if "history" not in st.session_state:
    st.session_state.history = []

if "latest_output" not in st.session_state:
    st.session_state.latest_output = ""

# BUTTONS
col1, col2 = st.columns(2)

with col1:
    generate_btn = st.button("✨ Generate Post")

with col2:
    regen_btn = st.button("🔄 Regenerate")

# GENERATE
if generate_btn:

    if topic.strip() == "":
        st.error("⚠ Please enter a topic")

    else:

        with st.spinner("Generating amazing content..."):

            response = requests.get(
                "http://127.0.0.1:8000/generate",
                params={
                    "prompt": topic,
                    "tone": tone
                }
            )

            output = response.json()["output"]

            st.session_state.latest_output = output
            st.session_state.history.append(output)

# REGENERATE
if regen_btn:

    if topic.strip() != "":

        with st.spinner("Creating another version..."):

            response = requests.get(
                "http://127.0.0.1:8000/generate",
                params={
                    "prompt": topic,
                    "tone": tone
                }
            )

            output = response.json()["output"]

            st.session_state.latest_output = output
            st.session_state.history.append(output)

# OUTPUT DISPLAY
if st.session_state.latest_output != "":

    st.markdown(
        f"""
        <div class="output-box">
        <h2>✨ Generated Post</h2>
        <pre style="color:white; font-size:16px;">{st.session_state.latest_output}</pre>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.download_button(
        label="📥 Download Post",
        data=st.session_state.latest_output,
        file_name="social_post.txt",
        mime="text/plain"
    )

# HISTORY
st.write("")
st.subheader("🕘 Recent History")

if len(st.session_state.history) == 0:
    st.info("No posts generated yet")

else:

    for item in reversed(st.session_state.history[-5:]):

        st.markdown(
            f"""
            <div class="history-box">
            <pre style="color:white;">{item}</pre>
            </div>
            """,
            unsafe_allow_html=True
        )