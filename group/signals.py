from group.models import Group
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

@receiver(pre_save, sender=Group)
def my_handler(sender, **kwargs):
    print('group changed...')
