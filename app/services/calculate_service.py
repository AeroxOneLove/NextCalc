from sympy import SympifyError, nan, sympify, zoo

from app.exceptions.calculate_exceptions import BadRequestError


class CalculateService:
    def calculate(self, expression: str) -> float:
        try:
            if "=" in expression:
                raise BadRequestError(f"Некорректный ввод ({expression})")
            result = sympify(expression)
            if result in [nan, zoo]:
                raise BadRequestError(f"Деление на ноль невозможно ({expression})")
            return float(result)
        except (SympifyError, ValueError, TypeError, SyntaxError):
            raise BadRequestError(f"Некорректный ввод ({expression})")
