from dataclasses import dataclass
import streamlit as st
from workflow import WorkFlow


@dataclass
class Message:
    actor: str
    payload: str


USER = "user"
ASSISTANT = "ai"
MESSAGES = "messages"
if MESSAGES not in st.session_state:
    st.session_state[MESSAGES] = [
        Message(
            actor=ASSISTANT,
            payload="I am a Quebec gouverment assistant. How can I help you today?",
        )
    ]

msg: Message
for msg in st.session_state[MESSAGES]:
    st.chat_message(msg.actor).write(msg.payload)


def main() -> None:
    workflow = WorkFlow()
    
    query: str = st.chat_input("Write your message here")

    if query:
        st.session_state[MESSAGES].append(Message(actor=USER, payload=query))
        st.chat_message(USER).write(query)
        
        response = workflow.run(query=query)
        
        st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response))
        
        
        st.chat_message(ASSISTANT).write(response)


if __name__ == "__main__":
    main()
