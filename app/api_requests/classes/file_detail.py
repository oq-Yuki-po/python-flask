from dataclasses import field
from dataclasses_json import dataclass_json
from marshmallow_dataclass import dataclass
import marshmallow.validate


@dataclass_json
@dataclass
class FileDetail:
    row: int = field(metadata=dict(validate=marshmallow.validate.Range(min=1)))
    contents: str = field(metadata=dict(
        validate=marshmallow.validate.Length(min=0, max=255)))
