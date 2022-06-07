from __future__ import annotations

from app import app
from app.calculate import calculate_quadratic_equation_roots

from flask import request


@app.route('/', methods=['POST'])
def main_route() -> dict:
    """Main and only route, that calculates the roots of a
    quadratic equation from values: 'a', 'b' and  'c'
    """

    data = request.json
    if not data:
        return {'success': False, 'detail': 'Request must content json data'}

    a, b, c = data.get('a'), data.get('b'), data.get('c')
    if not (a is not None and b is not None and c is not None):  # Because values can be zero
        return {'success': False, 'detail': 'Request must content attrs: "a", "b" and "c"'}

    try:
        a, b, c = map(float, (a, b, c))
    except TypeError:
        return {'success': False, 'detail': 'Attrs "a", "b" and "c" must be float'}

    result = calculate_quadratic_equation_roots(a, b, c)

    return {'success': True, 'result': result}
