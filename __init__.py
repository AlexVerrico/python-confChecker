# Copyright (C) 2021 Alex Verrico (https://alexverrico.com/). All Rights Reserved.

from typing import List
from dotenv import load_dotenv
import os


def check_for_conf_key(level_list: List, current_level):
    try:
        x = current_level[level_list.pop(0)]
        if level_list:
            check_for_conf_key(level_list, x)
    except TypeError:
        raise KeyError
    return True


def check_env(required_vars: List):
    load_dotenv()
    for i in required_vars:
        if os.getenv(i) is None:
            raise Exception(f'Fatal Error: Environment Variable {i} not defined')
    return True


def check_yaml(conf, required_vars: List[List]):
    for var_list in required_vars:
        x = var_list[0:]
        try:
            check_for_conf_key(x, conf)
        except KeyError:
            raise Exception(f'Fatal Error: conf key \"{"->".join(var_list)}\" is non-existent')
        finally:
            del x
    return True
