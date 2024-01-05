# importing required Models 
import os
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory

#Open Ai Api for integration 
OPENAI_API_KEY=os.getenv('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')

template = """You are a tech-savvy computer science student who spends countless hours coding, building apps, and keeping up with the latest tech trends. You enjoy discussing programming languages, AI, and gadgets and are always ready to troubleshoot tech-related problems.
{chat_history}
User: {user_message}
Chatbot:"""

# Prompt Object
prompt = PromptTemplate(
    input_variables=["chat_history", "user_message"], template=template
)

memory = ConversationBufferMemory(memory_key="chat_history")

#Details of the Language Model Used in the Prompt 
llm_chain = LLMChain(
    llm=ChatOpenAI(temperature='0.5', model_name="gpt-3.5-turbo"),
    prompt=prompt,
    verbose=True,
    memory=memory,
)

def get_text_response(user_message,history):
    response = llm_chain.predict(user_message = user_message)
    return response

demo = gr.ChatInterface(get_text_response)

if __name__ == "__main__":
    demo.launch() #To create a public link, set `share=True` in `launch()`. To enable errors and logs, set `debug=True` in `launch()`.
