from langgraph_app.nodes.agent2 import title_creater

mock_state = {
    "transcript": "In this video, we discuss how artificial intelligence is changing the world of education..."
}

updated_state = title_creater(mock_state)

print("Generated title:", updated_state["title"])