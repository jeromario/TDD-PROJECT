from datetime import datetime
import uuid
from pydantic import BaseModel, UUID4, Field


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    upgrated_at: datetime = Field(default_factory=datetime.utcnow)
