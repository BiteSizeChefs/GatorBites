# from django.db.models.signals import post_save, pre_delete
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile, Relationship

# @receiver(post_save, sender=User)
# def post_save_create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=Relationship)
# def post_save_add_to_friends(sender, instance, created, **kwargs):
#     if instance.status == 'accepted':
#         instance.sender.friends.add(instance.receiver.user)
#         instance.receiver.friends.add(instance.sender.user)
#         instance.sender.save()
#         instance.receiver.save()

# @receiver(pre_delete, sender=Relationship)
# def pre_delete_remove_from_friends(sender, instance, **kwargs):
#     sender = instance.sender
#     receiver = instance.receiver
#     instance.sender.friends.remove(instance.receiver.user)
#     instance.receiver.friends.remove(instance.sender.user)
#     instance.sender.save()
#     instance.receiver.save()