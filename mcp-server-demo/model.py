from pydantic import BaseModel
from typing import Literal



class Context(BaseModel):
    value = Literal['love', 'confusion', 'cool', 'celebration', 'funny', 'angry', 'sad',
       'support', 'happy', 'surprise']
    