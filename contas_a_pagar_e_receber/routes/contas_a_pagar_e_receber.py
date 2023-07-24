from decimal import Decimal
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/contas-a-pagar-e-receber")

class ContasPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str
class ContasPagarReceberRequest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: str

@router.get("/", response_model=List[ContasPagarReceberResponse])
def listar_contas():
    return [
        ContasPagarReceberResponse(
        id=1,
        descricao="aluguel",
        valor=1000.50,
        tipo="PAGAR"
        ),
        ContasPagarReceberResponse(
        id=1,
        descricao="Carro",
        valor=5000.50,
        tipo="PAGAR"
        ),
    ]
@router.post("/", response_model=ContasPagarReceberResponse, status_code=201)
def criar_conta(conta: ContasPagarReceberRequest):
    return ContasPagarReceberResponse(
        id=3,
        descricao= conta.descricao,
        valor=conta.valor,
        tipo=conta.tipo
    )
    