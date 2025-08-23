from django.apps import AppConfig


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        """
        This method runs after Django has loaded all apps,
        so it's safe to import models and create groups/permissions here.
        """
        from django.contrib.auth.models import Group, Permission
        from django.db.utils import OperationalError, ProgrammingError

        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        try:
            for group_name, perms in groups_permissions.items():
                group, _ = Group.objects.get_or_create(name=group_name)
                for perm_codename in perms:
                    try:
                        permission = Permission.objects.get(codename=perm_codename)
                        group.permissions.add(permission)
                    except Permission.DoesNotExist:
                        # Permissions may not exist on the very first migrate
                        pass
        except (OperationalError, ProgrammingError):
            # Database not ready yet (during first migrate) → skip silently
            pass

