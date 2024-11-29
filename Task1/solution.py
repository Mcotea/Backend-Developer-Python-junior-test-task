#solution.py
def strict(func):
    def wrapper(*args):
        annotations = func.__annotations__

        for (param_name, param_type), arg in zip(annotations.items(), args):
            if param_name == 'return':
                continue
            if not isinstance(arg, param_type):
                raise TypeError(
                    f"Argument '{param_name}' must be of type {param_type.__name__}, "
                    f"but got {type(arg).__name__}."
                )

        if len(args) != len(annotations) - ('return' in annotations):
            raise TypeError("Number of arguments does not match function annotations.")

        return func(*args)

    return wrapper
