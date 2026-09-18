from pydantic import BaseModel,Field

class MysqlSchema(BaseModel):
    sql: str = Field(...,description="sql语句")