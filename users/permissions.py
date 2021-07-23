from rolepermissions.permissions import register_object_checker
from Etech_Blog.roles import Admin, Writer, Readers

@register_object_checker()
def write_article(role):
    if role == Admin:
        return True

    if role == Writer:
        return True

    return False


@register_object_checker()
def read_article(role):
    if role == Admin:
        return True

    elif role == Writer:
        return True

    else:
        return True