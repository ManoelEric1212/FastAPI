from fastapi import FastAPI
import uvicorn
from contas_a_pagar_e_receber.routes import contas_a_pagar_e_receber


app = FastAPI(
    title="Contas API",
    version="1.0.0",
    description="API desenvolvida para aprender melhor o framework FastAPI",
)
app.include_router(contas_a_pagar_e_receber.router)

