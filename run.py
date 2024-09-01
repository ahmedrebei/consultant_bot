from dataclasses import dataclass
import streamlit as st


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
            payload="Je suis un assitant pour le gouvernement du Quebec. Je spécialise en immigration et education. Comment puis-je vous aider?",
        )
    ]

msg: Message
for msg in st.session_state[MESSAGES]:
    st.chat_message(msg.actor).write(msg.payload)


def main() -> None:
    prompt: str = st.chat_input("Enter a prompt here")

    if prompt:
        st.session_state[MESSAGES].append(Message(actor=USER, payload=prompt))
        st.chat_message(USER).write(prompt)
        response: str = f"{prompt}"
        st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response))
        st.chat_message(ASSISTANT).write(response)


if __name__ == "__main__":
    main()
