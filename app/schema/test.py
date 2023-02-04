import random
from datetime import datetime

import numpy as np
from fastapi_plus.schema.base import InfoSchema, RespDetailSchema


class TestInfoSchema(InfoSchema):
    parent_name: str


class TestDetailSchema(TestInfoSchema):
    created_time: datetime
    updated_time: datetime


class TestRespDetailSchema(RespDetailSchema):
    detail: TestDetailSchema = None


if __name__ == '__main__':
    print("".join([str(random.randint(0, 10)) for i in range(20)]))
