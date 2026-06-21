"""
Tests = the source of truth for completion. A milestone is done when its tests pass.
Run with: python -m pytest -q   (or ask your tutor to check your work)
"""
import math
import pytest
from engine import Value


# ---- Milestone 1: the Value container ----
def test_m1_holds_data_and_grad():
    a = Value(3.0)
    assert a.data == 3.0
    assert a.grad == 0.0


# ---- Milestone 2: forward add / mul ----
def test_m2_add_and_mul_forward():
    a, b = Value(2.0), Value(-3.0)
    assert (a + b).data == -1.0
    assert (a * b).data == -6.0


# ---- Milestone 4: backward through + and * ----
def test_m4_backward_simple():
    a, b = Value(2.0), Value(-3.0)
    d = a * b + a          # d = a*b + a
    d.backward()
    # dd/da = b + 1 = -2 ; dd/db = a = 2
    assert math.isclose(a.grad, -2.0, abs_tol=1e-6)
    assert math.isclose(b.grad, 2.0, abs_tol=1e-6)


# ---- Milestone 5: tanh + a single neuron ----
def test_m5_tanh_neuron():
    x, w, b = Value(1.0), Value(0.5), Value(0.0)
    n = (x * w + b).tanh()
    n.backward()
    # dn/dw = (1 - tanh(0.5)^2) * x
    expected = (1 - math.tanh(0.5) ** 2) * 1.0
    assert math.isclose(w.grad, expected, abs_tol=1e-6)


if __name__ == "__main__":
    raise SystemExit(pytest.main(["-q", __file__]))
