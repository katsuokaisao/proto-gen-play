from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class pinPonRequest(_message.Message):
    __slots__ = ["words"]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    words: str
    def __init__(self, words: _Optional[str] = ...) -> None: ...

class pinPonResponse(_message.Message):
    __slots__ = ["words"]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    words: str
    def __init__(self, words: _Optional[str] = ...) -> None: ...