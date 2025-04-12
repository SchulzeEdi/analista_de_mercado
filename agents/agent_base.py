from dataclasses import dataclass
from typing import List, Optional
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

@dataclass
class AgentConfig:
    """Configuration class for agent parameters"""
    name: str
    role: str
    description: str
    session_id: str
    user_id: str
    tools: List[any]
    instructions: List[str]
    model_id: str = "gpt-4o-mini"
    markdown: bool = True
    show_tool_calls: bool = True
    num_history_responses: int = 15

class AgentBase:
    
    def __init__(self, config: AgentConfig):
        """
        Initialize agent with configuration
        
        Args:
            config (AgentConfig): Configuration object containing all agent parameters
        """
        self.config = config
        self._agent: Optional[Agent] = None

    def initialize_agent(self) -> Agent:
        """
        Creates and initializes a base agent with the configured parameters.
        
        Returns:
            Agent: Initialized phi agent
        """
        if not self._agent:
            self._agent = Agent(
                name=self.config.name,
                role=self.config.role,
                description=self.config.description,
                tools=self.config.tools,
                instructions=self.config.instructions,
                markdown=self.config.markdown,
                show_tool_calls=self.config.show_tool_calls,
                num_history_responses=self.config.num_history_responses,
                model=OpenAIChat(self.config.model_id),
                session_id=self.config.session_id,
                user_id=self.config.user_id,
            )
        return self._agent

    def get_agent(self) -> Agent:
        """
        Returns the initialized agent, creating it if necessary.
        
        Returns:
            Agent: The initialized agent
        """
        return self._agent if self._agent else self.initialize_agent()

    def execute_query(self, query: str, stream: bool = True) -> str:
        """
        Executes a query using the agent
        
        Args:
            query (str): The query to execute
            stream (bool): Whether to stream the response
            
        Returns:
            str: Agent's response
        """
        agent = self.get_agent()
        return agent.print_response(query, stream=stream)