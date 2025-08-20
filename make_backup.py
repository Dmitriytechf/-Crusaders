import json
from django.core import serializers
from django.core.management import call_command
import sys
import os
import django


# Добавляем путь к проекту
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

try:
    django.setup()
    
    def make_backup():
        # Создаем дамп с указанием кодировки
        with open('backup.json', 'w', encoding='utf-8') as f:
            call_command('dumpdata', stdout=f, indent=4)
        print("Backup создан успешно!")
    
    if __name__ == '__main__':
        make_backup()

except Exception as e:
    print(f"Ошибка: {e}")