from graphene import (
    InputObjectType,
    ID,
)


class BaseInput(InputObjectType):
    """
    Base abstract Input wih id
    (so we don`t need to implement "id" field every time we creating input)
    """
    id = ID()
