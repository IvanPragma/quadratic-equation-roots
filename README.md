# Quadratic equation roots
 Simple service written on `flask`, used to find the roots of a quadratic equation

# How does it work?
- Run local server `python3.9 run.py`
- Send `POST` request to `http://localhost:5000/` with data in json format
  > Example data: {"a": 2, "b": 4, "c": 6}
- Server will return json with keys: `success` and `result`
  > `result` is root(s) for equation, it's can be `None`, `float` or `list[float]`
