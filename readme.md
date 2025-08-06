🎬 YouTube Blog Generator

Turn any YouTube video into a beautifully written blog post with a title and summary using AI and LangGraph.

⸻

🌟 Features
	•	🔗 Paste any YouTube video URL
	•	📝 Generates a catchy blog title
	•	📘 Full blog content written from transcript
	•	🔍 Summary section for quick reads
	•	🎨 Beautiful Streamlit UI with smooth UX
	•	🧠 Powered by LangGraph + Groq (LLMs)

⸻

🧰 Tech Stack
	•	Streamlit for frontend
	•	LangGraph for agent orchestration
	•	LangChain + Groq for LLMs
	•	yt-dlp + FasterWhisper for transcription

⸻

🚀 How to Run Locally

1. Clone the Repository

git clone  https://github.com/imaadarsh-r/youtubevideosummarizer.git


2. Create Python Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Add .env File

Create a .env file and add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here

5. Run the Backend

uvicorn backend.main:app --reload  # or the path to your FastAPI entry

6. Launch the Streamlit Frontend

streamlit run app.py


⸻

🖼 Preview


⸻

📂 Project Structure

.
├── main.py                  # Streamlit frontend
├── langgraph_app/                # LangGraph 
│   ├── nodes
│   ├──nodes/agents/             # Agent 1-4 nodes
│   └── utils/              # Transcription, YouTube download etc.
├── state          # schema
├── requirements.txt
└── README.md


⸻

📄 License

MIT License. Feel free to use and remix this project with credit.

⸻

✨ Acknowledgements

Built using LangGraph, Groq, FasterWhisper, and Streamlit. Special thanks to [@yourname] for architecting the flow.

⸻

🙌 Contribute

Pull requests are welcome. Let’s build smarter AI workflows together!

⸻

🌐 Try It Live

Want to deploy this to Streamlit Cloud or Hugging Face Spaces? Let me know, I can help with setup!

Inspired to write better blogs with less effort? You might also love Jenni AI – your intelligent writing assistant.