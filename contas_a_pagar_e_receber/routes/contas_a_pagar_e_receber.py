from fastapi import APIRouter


router = APIRouter(prefix="/contas-a-pagar-e-receber")
@router.get("/")
def listar_contas():
    return [
        {
            "contas1": "contas1",
            "contas2": "contas2",
            "contas3": "contas3",
            "contas4": "contas4",
         }
    ]