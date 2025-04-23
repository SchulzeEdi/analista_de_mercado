from phi.agent import Agent
from phi.model.openai import OpenAIChat
# from agents.agent_financeiro import AgentFinanceiro
from agents.agent_pesquisa import AgentPesquisa
from agents.agent_valuation import AgentValuation
from uuid import uuid4

class PhidataTeam:
    def __init__(self):
        session_id = str(uuid4())
        user_id = str(uuid4())
        
        self.agent_pesquisa = AgentPesquisa(session_id=session_id, user_id=user_id)
        # self.agent_financeiro = AgentFinanceiro(session_id=session_id, user_id=user_id)
        self.agent_valuation = AgentValuation(session_id=session_id, user_id=user_id)
        
        self.multi_agent = Agent(
            name="Time de Análise Financeira",
            role="Analisar empresas e recomendar investimentos",
            description="""
                Faça uma análise completa e objetiva considerando:
                1. Visão Geral:
                   - Preço atual e variação
                   - Principais indicadores
                   - Resumo da empresa
                
                2. Análise Fundamentalista:
                   - Indicadores chave
                   - Saúde financeira
                   - Dividendos
                
                3. Valuation:
                   - Preço justo estimado
                   - Margem de segurança
                   - Potencial de valorização/desvalorização
                
                4. Recomendação Final:
                   - Comprar/Vender/Manter
                   - Horizonte recomendado
                   - Principais riscos
            """,
            team=[
                self.agent_pesquisa.agent,
                self.agent_valuation.agent
            ],
            model=OpenAIChat(id="gpt-4-0125-preview"),
            show_tool_calls=True,
            markdown=True,
            verbose=True,
            show_reasoning=True,
            num_history_responses=15,
            session_id=session_id,
            user_id=user_id,
            instructions=[
                'Responda SEMPRE em português do Brasil'
            ],
        )
    
    def execute_query(self, user_question: str):
        """
        Executa a consulta do usuário utilizando o time de agentes.
        Retorna uma análise completa da empresa/ação.
        """
        try:
            response = self.multi_agent.print_response(
                user_question
            )
            return response.content
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
            raise e