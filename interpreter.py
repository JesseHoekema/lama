# interpreter.py

class Interpreter:
    def __init__(self, program):
        self.program = program
        self.ask_count = 0  # To keep track of ASK numbers
        self.variables = {}  # To store ASK results

    def run(self):
        for command in self.program:
            if command[0] == 'SAY':
                self.execute_say(command[1])
            elif command[0] == 'CALCULATE':
                self.execute_calculate(command[1], command[2])
            elif command[0] == 'ASK':
                self.execute_ask(command[1])
            elif command[0] == 'IF':
                self.execute_if(command[1], command[2], command[3], command[4])

    def execute_say(self, text):
        print(text)

    def execute_calculate(self, left, right):
        result = left + right
        print(result)

    def execute_ask(self, prompt):
        self.ask_count += 1
        result = input(prompt)
        self.variables[f'ASK{self.ask_count}'] = result
        return result

    def execute_if(self, left, right, then_command, else_command):
        # Check if left starts with ASK, if so get the stored value
        if isinstance(left, str) and left.startswith('ASK'):
            left = self.variables.get(left, '')
        # Check if right starts with ASK, if so get the stored value
        if isinstance(right, str) and right.startswith('ASK'):
            right = self.variables.get(right, '')
            
        if left == right:
            if then_command and then_command[0] == 'SAY':
                self.execute_say(then_command[1])
            elif then_command and then_command[0] == 'CALCULATE':
                self.execute_calculate(then_command[1], then_command[2])
        else:
            if else_command and else_command[0] == 'SAY':
                self.execute_say(else_command[1])
            elif else_command and else_command[0] == 'CALCULATE':
                self.execute_calculate(else_command[1], else_command[2])
