from langgraph.graph import StateGraph, END
from langgraph_app.nodes.agent1 import process_video
from langgraph_app.nodes.agent2 import title_creater
from langgraph_app.nodes.agent3 import blog_writer
from langgraph_app.nodes.agent4 import summarizer
from langgraph_app.state import AppState

def build_graph():
    builder = StateGraph(AppState)

    builder.add_node("transcribe", process_video)
    builder.add_node("generate_title", title_creater)
    builder.add_node("generate_blog", blog_writer)
    builder.add_node("generate_summary", summarizer)

    builder.set_entry_point("transcribe")
    builder.add_edge("transcribe", "generate_title")
    builder.add_edge("generate_title", "generate_blog")
    builder.add_edge("generate_blog", "generate_summary")
    builder.add_edge("generate_summary", END)

    return builder.compile()