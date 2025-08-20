import time

import streamlit as st
from qdrant_client import QdrantClient

from agent.alexupport_agent import AlexupportAgent

def _typing_stream(text):
    """Simulate typing effect"""
    for word in text.split():
        yield word + " "
        time.sleep(0.05)

if "agent" not in st.session_state:
    st.session_state["agent"] = AlexupportAgent()
agent = st.session_state["agent"]

QDRANT_URL = "https://63ad19dc-7779-4868-bc81-41f5fae4353a.europe-west3-0.gcp.cloud.qdrant.io:6333"
QDRANT_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0._mnughDNgXpg2I_tMDwpIIKZJiDqma2o_YDld0ZseR4"
COLLECTION_NAME = "data_collection"

# Get all points (limit to 2,000 for performance)
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
points = client.scroll(collection_name=COLLECTION_NAME, limit=2000)[0]

# Extract unique ASINs and map to product titles
asin_title_map = {}
asin_list = sorted({point.payload['asin'] for point in points})

st.title("Alexupport - Amazon AI Support Agent 🤖")
st.text(agent.get_agent_introduction())

# Step 1: User selects an ASIN (starts empty)
asin_options = ["Select an ASIN..."] + asin_list
selected_asin = st.selectbox("Choose a product (ASIN):", asin_options)

if selected_asin == "Select an ASIN...":
    st.info("Please select an ASIN to continue.")
    st.stop()

asin_list = sorted(asin_title_map.keys())
# Find the product title for the selected ASIN
product = next((point for point in points if point.payload.get('asin') == selected_asin), None)
product_title = product.payload['productTitle'] if product else 'No title found'

st.info(f"**Product Title:** {product_title}\n\nYou can view the product page here: \nhttps://www.amazon.com/dp/{selected_asin}")
st.markdown("---")

# Initialize chat history and reset if ASIN changes
if "asin" not in st.session_state or st.session_state["asin"] != selected_asin:
    st.session_state["asin"] = selected_asin
    st.session_state["messages"] = []

    agent.memory.clear()

    chat_start_msg = agent.get_agent_chat_start(product_title)
    st.session_state["messages"].append({"role": "assistant", "content": chat_start_msg})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat starts here
if prompt := st.chat_input("Your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        response = agent.answer_user_query(user_query=prompt, product_asin=selected_asin)
        response = st.write_stream(_typing_stream(response))

    st.session_state.messages.append({"role": "assistant", "content": response})
