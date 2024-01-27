from pydantic import BaseModel
from enum import Enum

class StatusEnum(str, Enum):
    carteira = "CARTEIRA"
    monitoramento = "MONITORAMENTO"

class ExcelSchema(BaseModel):
    ASSET : str
    STATUS : StatusEnum