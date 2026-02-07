class NumberOperation:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def is_power_of_10(self, num):
        power_of_10 = [10**i for i in range(101)]
        return num in power_of_10

    def perform_operation(self):
        if self.is_power_of_10(self.num1) and self.is_power_of_10(self.num2):
            if self.operator == '+':
                return self.num1 + self.num2
            elif self.operator == '*':
                return self.num1 * self.num2
        return None


num1 = int(input())
operator = input()
num2 = int(input())

operation = NumberOperation(num1, num2, operator)
result = operation.perform_operation()

if result is not None:
    print(result)
