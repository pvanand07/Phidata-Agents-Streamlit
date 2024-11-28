from phi.agent import Agent
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector
import dotenv
import os

dotenv.load_dotenv("D:/DEV/LIZMOTORS/PHIDATA/personalized/secrets.env")

db_url = f"postgresql+psycopg://{os.getenv('SUPABASE_USER')}:{os.getenv('SUPABASE_PASSWORD')}@aws-0-us-west-1.pooler.supabase.com:5432/postgres"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url),
)
#knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(knowledge_base=knowledge_base, use_tools=True, show_tool_calls=True)
agent.print_response("How to make thai omlette ?", markdown=True)
