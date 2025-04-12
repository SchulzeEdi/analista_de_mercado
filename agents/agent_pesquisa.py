from agents.agent_base import AgentBase, AgentConfig
from phi.tools.duckduckgo import DuckDuckGo
from prompts.prompt_agent_pesquisa import prompt_agente_pesquisa

class AgentPesquisa(AgentBase):
    def __init__(self, session_id: str, user_id: str):
        config = AgentConfig(
            name="Agente de Pesquisa",
            role="Coletar Dados de Ativos Financeiros",
            description=prompt_agente_pesquisa,
            tools=[
                DuckDuckGo()
            ],
            instructions=[
                "Pesquise dados relevantes para o agente financeiro", 
                "Gere a resposta no idioma Português do Brasil"
            ],
            session_id=session_id,
            user_id=user_id
        )
        super().__init__(config)