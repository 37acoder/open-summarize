import re


class Text:
    def __init__(self, content: str) -> None:
        self.content = content

    def split_by_paragraph(self) -> list:
        return [Text(c) for c in self.content.split("\n") if c]

    def split_by_sentence(self) -> list:
        return [Text(c) for c in re.split(r"[.?!。！？]", self.content) if c]