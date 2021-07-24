from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'publish_articles': True,
        'write_articles': True,
        'update_articles_of_another': True,
        'change_template': True,
        'add_formatting_rules': True,
    }



class Writer(AbstractUserRole):
    available_permissions = {
        'write_articles': True,
        'read_articles': True,
    }



class Reader(AbstractUserRole):
    available_permissions = {
        'read_articles': True,
    }