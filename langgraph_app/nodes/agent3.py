import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
from langgraph_app.state import AppState

def blog_writer(state: AppState) -> AppState:
    transcript = state.get("transcript")
    title = state.get("title")
    if not transcript or not title:
        raise ValueError("Transcript or title missing in AppState.")

    prompt = PromptTemplate.from_template("""\"\"\"
You are a professional blog writer.

Your task is to write a well-structured and engaging blog post based on the provided title and transcript.

- The blog must be under 1000 words.
- Use clear headings and smooth transitions.
- Do not include any internal thoughts, markdown, or explanations of what you’re doing.
- Do not include anything like <think>, "Let me", or notes to self.
- Just return the plain blog content.

Title: {title}
Transcript: {transcript}

Write the full blog post below:
""")

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        max_tokens=1000,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    chain = prompt | llm | StrOutputParser()
    blog = chain.invoke({"title": title, "transcript": transcript})

    state["blog"] = blog.strip()
    return state