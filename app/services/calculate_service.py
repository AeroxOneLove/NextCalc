from sympy import SympifyError, sympify

from app.exceptions.calculate_exceptions import BadRequestError


class CalculateService:
    def calculate(self, expression: str) -> float:
        try:
            result = sympify(expression)
            result_to_float = float(result)
        except (SympifyError, TypeError):
            if str(result) == "zoo":
                raise BadRequestError(f"Деление на ноль не возможно ({expression})")
            raise BadRequestError(f"Некоректный ввод ({expression})")
        else:
            return result_to_float
