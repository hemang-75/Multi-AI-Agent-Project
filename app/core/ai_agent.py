from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from fastapi import HTTPException

logger = get_logger(__name__)

def get_response_from_ai_agents(llm_id , query, allow_search , system_prompt):

    logger.info(f"Setting the llm model ")
    llm = ChatGroq(model=llm_id)

    logger.info("Setting the tools")
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    logger.info("Creating the AI Agent")
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt= system_prompt
    )
    logger.info("AI Agent created successfully")
    
    state = {"messages" : query}

    logger.info(f"Invoking the agent with query:{query}")
    try:
        response = agent.invoke(state)
        logger.info("Successfully got response from agent")
    except CustomException as e:
        logger.error("Some error occured during agent invocation")
        raise HTTPException(
            status_code=500, 
            detail=str(CustomException("Failed to get AI response",error_detail=e))
            )

    messages = response.get("messages")

    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]

    return ai_messages[-1]



