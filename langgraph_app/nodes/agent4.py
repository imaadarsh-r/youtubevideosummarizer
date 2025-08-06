import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
from langgraph_app.state import AppState

def summarizer(state: AppState) -> AppState:
    transcript = state.get("transcript")
    blog = state.get("blog")
    if not transcript or not blog:
        raise ValueError("Transcript or blog post missing in AppState.")

    prompt = PromptTemplate.from_template("""
        You are a professional summarizer.

Your task is to write a clear, concise summary based on the provided blog post and transcript.

Only output the summary, in 1-2 short paragraphs (max 200 words), covering the key themes. Do not include any explanations or thoughts. Avoid internal reasoning, planning, or markdown formatting.

Focus on the following points:
- The blog discusses how kindness, courage, perseverance, and self-growth help overcome conflict and fear.
- Include impactful metaphors or quotes briefly if necessary.
- Do not include phrases like "I think", "let's", "we", or model reasoning like <think>.

Input:
Transcript: {transcript}
Blog: {blog}

Summary:
    """)

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        max_tokens=200,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    chain = prompt | llm | StrOutputParser()
    summary = chain.invoke({"transcript": transcript, "blog": blog})

    state["summary"] = summary.strip()
    return state
