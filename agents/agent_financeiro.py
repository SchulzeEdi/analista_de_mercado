# from phi.agent import Agent
# from phi.tools.yfinance import YFinanceTools
# from phi.model.openai import OpenAIChat
# from prompts.prompt_agent_financeiro import prompt_agente_financeiro

# class AgentFinanceiro:
#     def __init__(self, session_id: str, user_id: str):
#         self.agent = Agent(
#             name="Agente Financeiro",
#             role="Coletar Dados de Ativos Financeiros",
#             description=prompt_agente_financeiro,
#             tools=[
#                 YFinanceTools(
#                     stock_price=True,
#                     analyst_recommendations=True,
#                     company_info=True,
#                     company_news=True
#                 )
#             ],
#             instructions=[
#                 "Sempre use tabelas para exibir dados",
#                 "Gere a resposta no idioma Português do Brasil"
#             ],
#             model=OpenAIChat(id='gpt-4o-mini'),
#             session_id=session_id,
#             user_id=user_id,
#             reasoning=True,
#         )