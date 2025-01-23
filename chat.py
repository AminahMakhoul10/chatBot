# 1 - Import the langchain functions

from langchain_aws import ChatBedrock
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)


# 2 - Create function to imvoke the model

def titan_llm(input_text):
    logging.info(f"Input text: {input_text}")
    llm = ChatBedrock(
        model_id="amazon.titan-text-express-v1",
        model_kwargs={
            "temperature": 0.7,
            "topP": 0.9,
        },
    )

    response = llm.invoke(input_text)
    logging.info(f"Response: {response}")
    return response

def create_memory():
    llm = ChatBedrock(
        model_id="amazon.titan-text-express-v1",
        model_kwargs={
            "temperature": 0.5,
            "topP": 1,
        },
    )
    return ConversationSummaryBufferMemory(llm=llm)

def get_chat_response(input_text, memory):
    conversation_with_memory = ConversationChain(
        llm=ChatBedrock(
            model_id="amazon.titan-text-express-v1",
            model_kwargs={
                "temperature": 0.5,
                "topP": 1,
            },
        ),
        memory=memory,
    )
    return conversation_with_memory.run(input_text)