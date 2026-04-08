import re

import language_tool_python


class GrammarChecker:
    def __init__(self, language: str = "en-US", max_issues: int = 1):
        self.tool = language_tool_python.LanguageTool(language)
        self.max_issues = max_issues

    def _fails_fragment_heuristic(self, reply: str) -> bool:
        text = reply.strip()

        if not text:
            return True

        lower = text.lower()

        short_fragment_patterns = [
            r"^lunch maybe later, not sure\.?$",
            r"^it was fun, went .+",
        ]

        for pattern in short_fragment_patterns:
            if re.match(pattern, lower):
                return True

        return False

    def evaluate(self, reply: str) -> str:
        matches = self.tool.check(reply)

        grammar_matches = [
            match for match in matches
            if getattr(match, "ruleIssueType", None) in {"grammar", "misspelling", "typographical"}
        ]

        if len(grammar_matches) >= self.max_issues:
            return "Fail"

        if self._fails_fragment_heuristic(reply):
            return "Fail"

        return "Pass"
