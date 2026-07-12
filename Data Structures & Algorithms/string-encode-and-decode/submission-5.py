class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "<EMPTY-STRING>"
        return "??".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "<EMPTY-STRING>":
            return []
        return s.split("??")
