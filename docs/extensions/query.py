# If you are wondering why this is done, it enables metaclass attributes to be picked up as class attributes/properties
# AFAIK there is no good way to do this apart from just recreating the class.
# TODO remove when updating for classmethod properties
import inspect

import steam
from steam.game_server import Query, QueryMeta


def setup(_):
    namespace = Query.__dict__.copy()
    attrs = dict(inspect.getmembers(QueryMeta, predicate=lambda attr: isinstance(attr, property)))
    del namespace["__slots__"]
    for name, value in attrs.items():
        namespace[name] = classmethod(value)  # make it show up as a class property

    steam.Query = steam.game_server.Query = type(
        "Query",
        (),
        namespace,
    )
