class DotDict(dict):
    def __init__(self, data=None):
        if data is not None:
            for key, value in data.items():
                self[key] = value

    def __setitem__(self, key, value):
        return super().__setitem__(key, _convert(value))

    # Redirect attribute operations to dictionary methods
    __delattr__ = dict.__delitem__
    __getattr__ = dict.__getitem__
    __setattr__ = __setitem__


class DotList(list):
    def __init__(self, items=None):
        if items is not None:
            for item in items:
                self.append(item)

    def append(self, items):
        return super().append(_convert(items))

    def insert(self, index, items):
        return super().insert(index, _convert(items))


def _convert(obj):
    """Recursively converts dicts/lists to DotDict/DotList if not already converted."""
    if isinstance(obj, dict) and not isinstance(obj, DotDict):
        return DotDict(obj)
    if isinstance(obj, list) and not isinstance(obj, DotList):
        return DotList(obj)
    return obj
