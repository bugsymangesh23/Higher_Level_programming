class Interpreter:
    def __init__(self):
        self.stack = []

    def LOAD_VALUE(self, number):
        """Load a value onto the stack."""
        self.stack.append(number)

    def PRINT_ANSWER(self):
        """Print the top value from the stack."""
        if self.stack:
            answer = self.stack.pop()
            print(answer)
        else:
            print("Stack is empty, nothing to print.")

    def ADD_TWO_VALUES(self):
        """Pop two values from the stack, add them, and push the result back on the stack."""
        if len(self.stack) < 2:
            print("Not enough values on the stack to perform addition.")
            return
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)

    def execute_code(self, what_to_execute):
        """Execute a series of instructions based on provided input."""
        instructions = what_to_execute["instructions"]
        numbers = what_to_execute["numbers"]
        
        for each_step in instructions:
            instruction = each_step[0]
            argument = each_step[1] if len(each_step) > 1 else None
            
            if instruction == "LOAD_VALUE":
                number = numbers[argument]
                self.LOAD_VALUE(number)
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()
            else:
                print(f"Unknown instruction: {instruction}")

# Example usage
if __name__ == "__main__":
    interpreter = Interpreter()
    
    # Define instructions and numbers
    what_to_execute = {
        "instructions": [
            ("LOAD_VALUE", 0),  # Load the first number (3)
            ("LOAD_VALUE", 1),  # Load the second number (5)
            ("ADD_TWO_VALUES",), # Add the two values
            ("PRINT_ANSWER",)   # Print the result
        ],
        "numbers": [3, 5]  # The numbers to load
    }
    
    interpreter.execute_code(what_to_execute)



