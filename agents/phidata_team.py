from agent_base import AgentBase
from agent_financeiro import AgentFinanceiro
from agent_pesquisa import AgentPesquisa
class PhidataTeam:
    def __init__(self):
        pass
    
    def execute_query(self, user_question: str):
        """
            Executa a consulta do usuário utilizando os agentes de pesquisa e financeiro.
        """
        try:
            multi_agente = AgentBase(
                team = [AgentPesquisa.get_agent, AgentFinanceiro.get_agent],
                show_tool_calls = True,
                markdown = True,
                num_history_responses = 15,
            )

            try:
                multi_agente.execute_query(
                    query = user_question,
                    stream = True
                )
            except Exception as e:
                print(f"Erro ao executar a pesquisa: {e}")

        except Exception as e:
            print(f"Erro ao inicializar os agentes: {e}")