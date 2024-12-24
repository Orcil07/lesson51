import inspect

def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта:
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта:
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль, к которому принадлежит объект, если есть такая возможность:
    obj_module = getattr(obj, '__module__', 'built-in' if isinstance(obj, (int, str, float, bool, list, dict, set,
                                                                           tuple)) else None)

    # Сбор информации в словарь:
    info = {'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module}

    return info

# Пример работы:
number_info = introspection_info(42)
print(number_info)