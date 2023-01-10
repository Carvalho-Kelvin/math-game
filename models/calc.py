from random import choice, randint


class Calculate():

    def __init__(self, difficulty: int) -> None:
        self.__difficulty: int = difficulty
        self.__num1: int = self._generate_value
        self.__num2: int = self._generate_value
        self.__operator: str = choice(('+', '-', '*'))
        self.__result: int = self._generate_result

    @property
    def difficulty(self) -> int:
        return self.__difficulty

    @property
    def num1(self) -> int:
        return self.__num1

    @property
    def num2(self) -> int:
        return self.__num2

    @property
    def operator(self) -> str:
        return self.__operator

    @property
    def result(self) -> int:
        return self.__result

    def __str__(self) -> str:
        op: str = ''
        if self.operator == '+':
            op = 'Sum'
        elif self.operator == '-':
            op = 'Minus'
        elif self.operator == '*':
            op = 'Multiply'
        else:
            op = 'Invalid operator!'
        return f'Number 1: {self.num1} \nNumber 2: {self.num2} \nDifficulty: {self.difficulty} \nOperator: {op}'

    @property
    def _generate_value(self) -> int:
        if self.difficulty == 1:
            return randint(0, 10)
        elif self.difficulty == 2:
            return randint(11, 100)
        elif self.difficulty == 3:
            return randint(101, 1000)

    @property
    def _generate_result(self) -> int:
        if self.operator == '+':
            return self.num1 + self.num2
        elif self.operator == '-':
            return self.num1 - self.num2
        elif self.operator == '*':
            return self.num1 * self.num2

    def check_result(self, answer: int) -> bool:
        right: bool = False

        if answer == self.result:
            right = True
        print(f'{self.num1} {self.operator} {self.num2} = {self.__result}')
        return right

    def show_operation(self) -> None:
        print(f'{self.num1} {self.operator} {self.num2} = ?')
