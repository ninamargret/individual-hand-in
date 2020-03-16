class Calculator:
    
    @staticmethod
    def Add(input: str) -> int:
        if input == "":
            return 0
        
        elif len(input) >= 3:
            
            negative_numbers = ""
            num_list = input.split(",")
            sum = 0 
            
            for number_str in num_list:
                if "-" in number_str:
                    negative_numbers += number_str + ","
                
                elif "\n" in number_str:
                    num1, num2 = number_str.split("\n")
                    num1 = check_number_str(num1)
                    num2 = check_number_str(num2)
                    sum += num1 + num2
    
                else:
                    if int(number_str) > 1000:
                        sum += 0
                    else:
                        sum += int(number_str)
            
            if negative_numbers != "":
                return f"Negatives not allowed: {negative_numbers[:-1]}"
            else:
                return sum
        
        else:
            return int(input)


def check_number_str(number_str: str)-> int:
    new_num = 0
    for element in number_str:

        if element.isdigit() and int(element) > 1000:
            new_num += 0
        elif element.isdigit():
            new_num += int(element)
        else:
            new_num += 0
    return new_num