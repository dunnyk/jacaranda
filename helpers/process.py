from models.computation import Computation
from models.database import db


def process_computation(data: dict) -> dict:
    """Process the computation

    Args:
        data (dict): data received from the client includes dividend and divisor

    Raise:
        Exception
    Returns:
        results (dict): computed result {"result": result}
    """
    if data.get("dividend") is None or data.get("divisor") is None:
        return "Both dividend and divisor MUST be given", 400
    try:
        dividend = int(data.get("dividend"))
        divisor = int(data.get("divisor"))
    except Exception:
        return {"error": "Both dividend and divisor must be integers"}, 400

    if divisor == 0:
        return {"error": "Division by zero is not allowed"}, 400

    return compute(dividend, divisor)


def compute(dividend: int, divisor: int) -> dict:
    """Division computation

    Args:
        dividend (int): dividend
        divisor (int): divisor

    Returns:
        results (dict): computed result {"result": result}
    """
    result = dividend / divisor
    result = round(result, 3)
    division_result = Computation(dividend=dividend, divisor=divisor, result=result)
    db.session.add(division_result)
    db.session.commit()
    return {"result": result}
