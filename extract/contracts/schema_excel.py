from pydantic import BaseModel

class ExcelSchema(BaseModel):
    Asset : str
    Status : enumerate("CARTEIRA","MONITORAMENTO")