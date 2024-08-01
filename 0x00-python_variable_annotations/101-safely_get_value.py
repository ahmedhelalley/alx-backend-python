#!/usr/bin/env python3
"""Defines safely_get_value function.."""

from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')
ret_t = Union[Any, T]
def_t = Optional[T]


def safely_get_value(dct: Mapping, key: Any, default: def_t = None) -> ret_t:
    """Return value that coresponds to a specific key or None"""
    if key in dct:
        return dct[key]
    else:
        return default
