class Calculator:
    @staticmethod
    def Add(input: str) -> int:
        if input == "":
            return 0
        else:
            return int(input)