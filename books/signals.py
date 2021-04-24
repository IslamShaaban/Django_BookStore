from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from .models import Book, ISBN


@receiver(post_save,sender=Book)
def after_book_creation(sender, instance, created, *args, **kwargs):
    if created:
        isbn_instance = ISBN.objects.create(book = instance)
        isbn_instance.save()
        instance.isbn = isbn_instance
        instance.save()

    else:
        print("Book not Created")