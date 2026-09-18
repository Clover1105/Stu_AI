from pydantic import BaseModel,Field

class QueryEmployeeSchema(BaseModel):
    sql: str = Field(...,description="sql语句")