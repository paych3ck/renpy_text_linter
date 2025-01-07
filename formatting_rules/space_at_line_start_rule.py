import re
import constants
from formatting_rules.base_rule import FormattingRule
from typing import List
from models import Error


class SpaceAtLineStartRule(FormattingRule):
    def check_line(self, line: str, row_index: int) -> List[Error]:
        errors = []

        match = re.match(r"^[ \t]+", line)
        if match:
            start_col = match.start()
            end_col = match.end()
            length = end_col - start_col

            errors.append(Error(
                row=row_index,
                word=" ",
                col=start_col,
                length=length,
                suggestions=[],
                message="Лишние пробелы или табы в начале строки",
                checker=constants.FORMATTING_CHECKER
            ))

        return errors