# interpreter.py

class Interpreter:
    def __init__(self, program):
        self.program = program

    def run(self):
        for command in self.program:
            if command[0] == 'SAY':
                self.execute_say(command[1])
            elif command[0] == 'CALCULATE':
                self.execute_calculate(command[1], command[2])

    def execute_say(self, text):
        print(text)

    def execute_calculate(self, left, right):
        result = left + right
        print(result)
