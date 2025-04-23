from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat
from prompts.prompt_agent_pesquisa import prompt_agente_pesquisa

class AgentPesquisa:
    def __init__(self, session_id: str, user_id: str):
        self.agent = Agent(
            name="Agente de Pesquisa",
            role="Coletar Dados de Ativos Financeiros",
            description=prompt_agente_pesquisa,
            tools=[DuckDuckGo()],
            instructions=[
                "Pesquise dados relevantes para o agente financeiro",
                "Gere a resposta no idioma Português do Brasil"
            ],
            model=OpenAIChat(id='gpt-4o-mini'),
            session_id=session_id,
            user_id=user_id,
            show_tool_calls=True,
            markdown=True,
            verbose=True,
            show_reasoning=True,
        )