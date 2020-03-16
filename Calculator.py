class Calculator:
    @staticmethod
    def Add(input: str) -> int:
        if input == "":
            return 0
        elif len(input) >= 3:
            num_list = input.split(",")
            sum = 0 
            for number_str in num_list:
                if "\n" in number_str:
                    num1, num2 = number_str.split("\n")
                    sum += int(num1) + int(num2)
                else:
                    sum += int(number_str)

            return sum
        else:
            return int(input)
