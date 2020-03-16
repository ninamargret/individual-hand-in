

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
                    num1 = check_number_str(int(num1))
                    num2 = check_number_str(int(num2))
                    sum += num1 + num2
                else:
                    number_str = check_number_str(int(number_str))
                    sum += number_str

            return sum
        
        else:
            return int(input)


def check_number_str(number_str: int)-> int:
        if number_str > 1000:
            return 0
        else:
            return number_str