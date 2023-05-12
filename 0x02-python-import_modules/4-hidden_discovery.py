#!/usr/bin/python3

if __name__ == "__main__":

    import importlib.util

    module_name = "hidden_4"
    module_spec = importlib.util.spec_from_file_location(module_name,
                                                         "hidden_4.pyc")
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    names = [name for name in dir(module) if not name.startswith("__")]
    names.sort()

    for name in names:
        print(name)
