import streamlit as st
from main import agent_executor, parser

# Configure Streamlit page
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔍",
    layout="wide"
)

# Title and description
st.title("🤖 AI Research Assistant")
st.markdown(
    """
    This tool helps you research topics using AI. It can:
    - 🔎 Search the web for current information
    - 📚 Query Wikipedia
    """
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if query := st.chat_input("What would you like to research?"):
    # Display user query
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})
    
    # Display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Researching..."):
            try:
                # Get response from the agent
                raw_response = agent_executor.invoke({"query": query})
                response_text = raw_response.get("output", "No response received.")

                # Attempt to parse structured response
                try:
                    structured_response = parser.parse(response_text)

                    # Display structured response
                    st.markdown(f"**Topic:** {structured_response.topic}")
                    st.markdown(f"**Summary:** {structured_response.summary}")

                    if structured_response.sources:
                        st.markdown("**Sources:**")
                        for source in structured_response.sources:
                            st.markdown(f"- {source}")

                    if structured_response.tools_used:
                        st.markdown("**Tools Used:**")
                        for tool in structured_response.tools_used:
                            st.markdown(f"- {tool}")
                
                # Fallback to raw output if parsing fails
                except Exception as e:
                    st.warning("Couldn’t structure the response. Displaying raw output:")
                    st.markdown(response_text)

                # Save assistant response to chat history
                st.session_state.messages.append(
                    {"role": "assistant", "content": response_text}
                )

            # Error handling
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
