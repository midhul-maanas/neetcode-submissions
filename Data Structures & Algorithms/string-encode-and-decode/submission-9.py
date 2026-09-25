class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "<EMPTY_STRING>"
        return "???".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "<EMPTY_STRING>":
            return []
        return s.split("???")