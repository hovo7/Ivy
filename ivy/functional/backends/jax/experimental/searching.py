# global
from typing import Optional, Tuple

import jax.numpy as jnp

# local
from ivy.functional.backends.jax import JaxArray


def unravel_index(
    indices: JaxArray,
    shape: Tuple[int],
    /,
    *,
    out: Optional[JaxArray] = None,
) -> Tuple[JaxArray]:
    return jnp.unravel_index(indices.astype(jnp.int32), shape)
