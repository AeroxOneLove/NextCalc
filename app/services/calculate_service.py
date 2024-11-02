from sympy import SympifyError, nan, sympify

from app.exceptions.calculate_exceptions import BadRequestError


class CalculateService:
    def calculate(self, expression: str) -> float:
        try:
            if expression.count("=") >= 1:
                raise BadRequestError(f"Некоректный ввод ({expression})")
            result = sympify(expression)
            if result == nan:
                raise BadRequestError(f"Деление на ноль не возможно ({expression})")
            result_to_float = float(result)
        except (SympifyError, ValueError, SyntaxError, UnboundLocalError):
            raise BadRequestError(f"Некоректный ввод ({expression})")
        except TypeError:
            try:
                if str(result) == "zoo":
                    raise BadRequestError(f"Деление на ноль не возможно ({expression})")
            except UnboundLocalError:
                raise BadRequestError(f"Некоректный ввод ({expression})")
            raise BadRequestError(f"Некоректный ввод ({expression})")
        else:
            return result_to_float
