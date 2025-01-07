from typing import List
from models import Error


class FormattingRule:
    def check_line(self, line: str, row_index: int) -> List[Error]:
        raise NotImplementedError