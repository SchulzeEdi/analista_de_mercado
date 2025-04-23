from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.model.openai import OpenAIChat

class AgentValuation:
    def __init__(self, session_id: str, user_id: str):
        self.agent = Agent(
            name="Analista de Valuation",
            role="Avaliar o valor justo das empresas",
            description="""
            Especialista em valuation que determina o valor justo das empresas usando:
            - Fluxo de Caixa Descontado (DCF)
            - Análise de Múltiplos
            - Modelos de Crescimento de Dividendos
            - Análise de Valor Patrimonial
            """,
            tools=[
                YFinanceTools(
                    analyst_recommendations=True,
                    stock_fundamentals=True,
                    stock_price=True,
                    company_news=True,
                    company_info=True,
                    income_statements=True,
                    key_financial_ratios=True,
                    historical_prices=True,
                    technical_indicators=True,
                )
            ],
            instructions=[
                "SEMPRE responda em português do Brasil",
                "Justifique suas premissas de valuation",
                "Compare diferentes métodos de avaliação",
                "Considere cenários otimistas e pessimistas",
                "Apresente margem de segurança no preço-alvo",
                "Seja objetivo e direto nas análises"
            ],
            model=OpenAIChat(
                id='gpt-4-0125-preview',
            ),
            session_id=session_id,
            user_id=user_id,
            show_tool_calls=True,
            markdown=True,
            verbose=True,
            show_reasoning=True,
        )