# Generated by Django 5.0.6 on 2024-06-30 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0005_rename_user_perfil_usuario_remove_perfil_apellido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='usuario',
            new_name='user',
        ),
    ]