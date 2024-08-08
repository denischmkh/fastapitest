from ..database.crud import get_all_dbase_items

def get_items():
    result = get_all_dbase_items()
    return result