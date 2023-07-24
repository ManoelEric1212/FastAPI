from fastapi import FastAPI
import uvicorn
from contas_a_pagar_e_receber.routes import contas_a_pagar_e_receber


app = FastAPI()
app.include_router(contas_a_pagar_e_receber.router)

