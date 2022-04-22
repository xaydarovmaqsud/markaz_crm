from permissions.init.register import PERMISSIONS
from account.models import Permission


def permission_instalization():
    delete_permissions = [p.name for p in Permission.objects.all()]
    for permission in PERMISSIONS:
        for member in permission._member_names_:
            name = str(permission._member_map_[member])
            model = permission.__name__
            description = permission._member_map_[member].value
            if name in delete_permissions:
                delete_permissions.remove(name)
            permission_objects = Permission.objects.filter(name=name)
            if permission_objects:
                permission_object = permission_objects.first()
                permission_object.description = description
                permission_object.save()
            else:
                Permission.objects.create(
                    name=name,
                    model=model,
                    description=description
                )
    for name in delete_permissions:
        Permission.objects.get(name=name).delete()

