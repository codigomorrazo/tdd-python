class Sum:
    def execute(self, valueA: int, valueB: int) -> int:
        self.__areValidParamsOrFail(valueA, valueB)
        return valueA + valueB

    def __areValidParamsOrFail(self, valueA: int, valueB: int) -> None:
        if not isinstance(valueA, int) or not isinstance(valueB, int):
            raise TypeError('Invalid types')
