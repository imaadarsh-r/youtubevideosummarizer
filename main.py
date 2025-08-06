import streamlit as st
from langgraph_app.graph import build_graph

# Set page configuration
st.set_page_config(page_title="🎬 YouTube Blog Generator", layout="centered")

# Custom styles
st.markdown("""
    <style>
        .big-title {
            text-align: center;
            font-size: 3em;
            font-weight: bold;
            color: #4b0082;
            margin-bottom: 0.5em;
        }
        .subtext {
            text-align: center;
            font-size: 1.2em;
            color: #555;
            margin-bottom: 1.5em;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="big-title">🎬 YouTube Blog Generator</div>
<div class="subtext">Paste a YouTube video URL and get a blog with title and summary using AI</div>
""", unsafe_allow_html=True)

# Input field
url = st.text_input("Paste a YouTube video URL:", placeholder="https://youtube.com/watch?v=...")

# Generate button
if st.button("Generate Blog ✨"):
    if not url:
        st.warning("⚠️ Please paste a YouTube URL first.")
    else:
        with st.spinner("🧠 Processing video and generating content..."):
            try:
                graph = build_graph()
                state = {"url": url}
                result = graph.invoke(state)

                st.subheader("📝 Title")
                st.markdown(f"**{result['title']}**")

                st.subheader("📘 Full Blog")
                st.text_area("Blog Post", result["blog"], height=400)

                st.subheader("🔍 Summary")
                st.success(result["summary"])

            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")