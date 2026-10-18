import uuid
from typing import Optional, List
from pydantic import BaseModel, Field


class StatementBase(BaseModel):
    source: str = Field(..., description="Statement provider source, e.g. 'B3' or 'NOMAD'")
    reference_date: Optional[str] = Field(None, description="Statement period or reference date (e.g. '2026-07-27')")
    currency: str = Field(default="BRL", description="Base statement currency ('BRL' or 'USD')")
    total_net_worth: float = Field(default=0.0, ge=0.0, description="Total reported net worth")


class StatementCreate(StatementBase):
    id: Optional[str] = Field(default=None, description="Statement UUIDv4. Auto-generated if omitted.")

    def model_post_init(self, __context) -> None:
        if not self.id:
            self.id = str(uuid.uuid4())


class Statement(StatementBase):
    id: str
    created_at: str

    model_config = {"from_attributes": True}


class PositionBase(BaseModel):
    ticker: str = Field(..., description="Asset ticker symbol, e.g. 'PETR4', 'AAPL'")
    category: str = Field(..., description="Asset classification, e.g. 'Stocks', 'FII', 'ETF'")
    quantity: float = Field(default=0.0, description="Asset position quantity")
    price: Optional[float] = Field(default=None, ge=0.0, description="Unit acquisition or current price")
    currency: str = Field(default="BRL", description="Asset currency ('BRL' or 'USD')")


class PositionCreate(PositionBase):
    statement_id: str = Field(..., description="Foreign key to the parent statement")
    id: Optional[str] = Field(default=None, description="Position UUIDv4. Auto-generated if omitted.")

    def model_post_init(self, __context) -> None:
        if not self.id:
            self.id = str(uuid.uuid4())


class Position(PositionBase):
    id: str
    statement_id: str

    model_config = {"from_attributes": True}


class StatementWithPositions(Statement):
    positions: List[Position] = []
