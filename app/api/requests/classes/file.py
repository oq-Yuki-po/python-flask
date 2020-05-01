from typing import List
from dataclasses import field
from dataclasses_json import dataclass_json
from marshmallow_dataclass import dataclass
import marshmallow.validate

from .file_detail import FileDetail


@dataclass_json
@dataclass
class File:
    name: str = field(metadata=dict(
        validate=marshmallow.validate.Length(min=1, max=255)))
    user_name: str = field(metadata=dict(
        validate=marshmallow.validate.Length(min=1, max=255)))
    details: List[FileDetail]
