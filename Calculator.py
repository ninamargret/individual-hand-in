class Calculator:
    @staticmethod
    def Add(input: str) -> int:
        if input == "":
            return 0
        elif len(input) >= 3:
            num_list = input.split(",")
            sum = 0 
            for number_str in num_list:
                sum += int(number_str)
            return sum
        else:
            return int(input)
