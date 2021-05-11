from django.db.models.signals import post_save

from banquet.models import User, Customer


def create_customer(sender, **kwargs):
    if kwargs['created']:
        Customer.objects.create(user=kwargs['instance'])


post_save.connect(create_customer, sender=User)
