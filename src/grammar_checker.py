import language_tool_python


class GrammarChecker:
    def __init__(self, language: str = "en-US", max_issues: int = 1):
        self.tool = language_tool_python.LanguageTool(language)
        self.max_issues = max_issues

    def evaluate(self, reply: str) -> str:
        matches = self.tool.check(reply)

        grammar_matches = [
            match for match in matches
            if getattr(match, "ruleIssueType", None) in {"grammar", "misspelling", "typographical"}
        ]

        return "Fail" if len(grammar_matches) >= self.max_issues else "Pass"
