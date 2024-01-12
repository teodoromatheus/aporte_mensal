from pydantic import BaseModel, PositiveFloat
from datetime import date

class CotationSchema(BaseModel):
    Date : date
    Close : PositiveFloat
    Adj_Close : PositiveFloat
    Asset : str