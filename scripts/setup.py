import os
import shutil
import traceback
from contextlib import suppress

import PyInstaller.__main__

application_name = 'HASD'

dist_path = os.path.join('dist')

copy_files = [
    ('icon.ico', dist_path),
]

copy_folders = [
    ('res', os.path.join(dist_path, 'res')),
]

try:
    PyInstaller.__main__.run([
        'main.py',
        '--name=%s' % application_name,
        '--icon=icon.ico',
        '--onefile',
        '--windowed',
    ])

    for source, destination in copy_files:
        shutil.copy(source, destination)

    for source, destination in copy_folders:
        with suppress(FileNotFoundError):
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
except:
    traceback.print_exc()
finally:
    with suppress(FileNotFoundError):
        shutil.rmtree('build')

    with suppress(FileNotFoundError):
        os.remove(f'{application_name}.spec')
