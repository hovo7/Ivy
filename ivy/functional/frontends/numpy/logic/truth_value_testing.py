# global
import numbers

import ivy
import ivy.functional.frontends.numpy as np_frontend
from ivy.functional.frontends.numpy.func_wrapper import (
    from_zero_dim_arrays_to_scalar,
    handle_numpy_out,
    to_ivy_arrays_and_back,
)


@handle_numpy_out
@to_ivy_arrays_and_back
@from_zero_dim_arrays_to_scalar
def all(
    a,
    axis=None,
    out=None,
    keepdims=False,
    *,
    where=None,
):
    axis = tuple(axis) if isinstance(axis, list) else axis
    if where is not None:
        a = ivy.where(where, a, True)
    ret = ivy.all(a, axis=axis, keepdims=keepdims, out=out)
    return ret


@handle_numpy_out
@to_ivy_arrays_and_back
@from_zero_dim_arrays_to_scalar
def any(
    a,
    axis=None,
    out=None,
    keepdims=False,
    *,
    where=None,
):
    axis = tuple(axis) if isinstance(axis, list) else axis
    if where is not None:
        a = ivy.where(where, a, False)
    ret = ivy.any(a, axis=axis, keepdims=keepdims, out=out)
    return ret


@to_ivy_arrays_and_back
def iscomplex(x):
    return ivy.bitwise_invert(ivy.isreal(x))


@to_ivy_arrays_and_back
def iscomplexobj(x):
    if x.ndim == 0:
        return ivy.is_complex_dtype(ivy.dtype(x))
    for ele in x:
        if ivy.is_complex_dtype(ivy.dtype(ele)):
            return True
        else:
            return False


@to_ivy_arrays_and_back
def isfortran(a):
    return a.flags.fnc


@to_ivy_arrays_and_back
def isreal(x):
    return ivy.isreal(x)


@to_ivy_arrays_and_back
def isrealobj(x: any):
    return not ivy.is_complex_dtype(ivy.dtype(x))


@to_ivy_arrays_and_back
def isscalar(element):
    return (
        isinstance(element, (int, float, complex, bool, bytes, str, memoryview))
        or isinstance(element, numbers.Number)
        or isinstance(element, np_frontend.generic)
    )
