from uuid import uuid4
import os


def path_and_rename(instance, filename):
    upload_to = 'post'+str(instance.pk)+'/thumbs'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format('post_thumb'+str(instance.pk), ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_rename_intro(instance, filename):
    upload_to = 'post'+str(instance.pk)+'/intro'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format('post_intro'+str(instance.pk), ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_rename_main(instance, filename):
    upload_to = 'post'+str(instance.pk)+'/main'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format('post_main'+str(instance.pk), ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_rename_add(instance, filename):
    upload_to = 'post'+str(instance.pk)+'/add'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format('post_add'+str(instance.pk), ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
