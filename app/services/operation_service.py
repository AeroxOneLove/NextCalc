from app.schemas.operation_schema import OperationElemSchema, OperationSchema


class OperationService:
    def get_all_operations(self) -> OperationSchema:
        operations = OperationSchema(
            elements=[
                OperationElemSchema(
                    name="Сложение", symbol="+", description="Складывает два числа"
                ),
                OperationElemSchema(
                    name="Вычитание",
                    symbol="-",
                    description="Вычитает одно число из другого",
                ),
                OperationElemSchema(
                    name="Умножение", symbol="*", description="Умножает два числа"
                ),
                OperationElemSchema(
                    name="Деление", symbol="/", description="Делит одно число на другое"
                ),
                OperationElemSchema(
                    name="Возведение в степень",
                    symbol="**",
                    description="Возводит число в степень",
                ),
                OperationElemSchema(
                    name="Корень",
                    symbol="sqrt",
                    description="Вычисляет квадратный корень числа",
                ),
                OperationElemSchema(
                    name="Синус", symbol="sin", description="Вычисляет синус угла"
                ),
                OperationElemSchema(
                    name="Косинус", symbol="cos", description="Вычисляет косинус угла"
                ),
                OperationElemSchema(
                    name="Тангенс", symbol="tan", description="Вычисляет тангенс угла"
                ),
                OperationElemSchema(
                    name="Котангенс",
                    symbol="cot",
                    description="Вычисляет котангенс угла",
                ),
                OperationElemSchema(
                    name="Секанс", symbol="sec", description="Вычисляет секанс угла"
                ),
                OperationElemSchema(
                    name="Косеканс", symbol="csc", description="Вычисляет косеканс угла"
                ),
                OperationElemSchema(
                    name="Гиперболический синус",
                    symbol="sinh",
                    description="Вычисляет гиперболический синус угла",
                ),
                OperationElemSchema(
                    name="Гиперболический косинус",
                    symbol="cosh",
                    description="Вычисляет гиперболический косинус угла",
                ),
                OperationElemSchema(
                    name="Гиперболический тангенс",
                    symbol="tanh",
                    description="Вычисляет гиперболический тангенс угла",
                ),
                OperationElemSchema(
                    name="Логарифм",
                    symbol="log",
                    description="Вычисляет логарифм числа по основанию",
                ),
                OperationElemSchema(
                    name="Экспонента",
                    symbol="exp",
                    description="Вычисляет значение e^x",
                ),
                OperationElemSchema(
                    name="Абсолютное значение",
                    symbol="Abs",
                    description="Вычисляет абсолютное значение числа",
                ),
                OperationElemSchema(
                    name="Факториал",
                    symbol="`factorial`",
                    description="Вычисляет факториал числа",
                ),
                OperationElemSchema(
                    name="Гамма-функция",
                    symbol="gamma",
                    description="Вычисляет гамма-функцию",
                ),
                OperationElemSchema(
                    name="Бета-функция",
                    symbol="beta",
                    description="Вычисляет бета-функцию",
                ),
                OperationElemSchema(
                    name="Функция Хевисайда",
                    symbol="Heaviside",
                    description="Определяет функцию Хевисайда",
                ),
                OperationElemSchema(
                    name="Дельта-функция Дирака",
                    symbol="DiracDelta",
                    description="Определяет дельта-функцию Дирака",
                ),
                OperationElemSchema(
                    name="Расширение выражения",
                    symbol="expand",
                    description="Расширяет математическое выражение",
                ),
                OperationElemSchema(
                    name="Упрощение выражения",
                    symbol="simplify",
                    description="Упрощает математическое выражение",
                ),
                OperationElemSchema(
                    name="Факторизация",
                    symbol="factor",
                    description="Факторизует математическое выражение",
                ),
            ]
        )
        return operations
