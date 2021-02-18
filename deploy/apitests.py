import importlib.util
import os
from flask import url_for


def has_no_empty_params(rule):
    """Check whether the route rules contain any empty parameters or not

    Arguments:
        input takes the route which we want to check 
        
    Returns:
        Bool: True if the route doesn't contain any empty parameters, otherwise false.
    """
    
    defaults = (rule.defaults if rule.defaults is not None else ())
    arguments = (rule.arguments if rule.arguments is not None else ())
    return len(defaults) >= len(arguments)


def get_routes():
    """Get all the list of routes with the functions initialised in the app.py file

    Arguments:
        None

    Returns:
        list: returns the list of routes defined in app.py
    """
    
    # Loading the app.py file as a module using library importlib

    spec = importlib.util.spec_from_file_location('app', 'app.py')
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)
    routes = []
    for rule in app.app.url_map.iter_rules():
        # Checking whether the rule has any empty params

        if has_no_empty_params(rule):
            # The list contains the tuple which comprises of route method,route path,route end point

            routes.append((rule.methods,str(rule),rule.endpoint))

    return routes


if __name__ == '__main__':
    get_routes()
