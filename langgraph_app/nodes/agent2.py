import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
from langgraph_app.state import AppState

def title_creater(state: AppState) -> AppState:
    transcript = state.get("transcript")
    if not transcript:
        raise ValueError("No transcript available in AppState.")

    prompt = PromptTemplate.from_template("""
        You are a creative title generator.
        Based on the transcript, generate a catchy and SEO-friendly blog title.

        Constraints:
        - No more than 15 words
        - Avoid special characters

        Transcript:
        {transcript}
    """)

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        max_tokens=50,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    chain = prompt | llm | StrOutputParser()
    title = chain.invoke({"transcript": transcript})

    state["title"] = title.strip()
    return state

