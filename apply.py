import json
import os
import shutil
import subprocess

def get_settings():
    with open('settings.json') as file:
        return json.load(file)

def apply_patch(path):
    cwd = os.getcwd()
    shutil.copy('mypatch.patch', path)
    os.chdir(path)
    subprocess.run(['git', 'apply', 'mypatch.patch'])
    os.chdir(cwd)

def copy_texts(path):
    shutil.copytree('texts', os.path.join(path, 'texts'), dirs_exist_ok=True)

def copy_audio(path):
    shutil.copytree('audio', os.path.join(path, 'dynos', 'audio'), dirs_exist_ok=True)

def main():
    settings = get_settings()
    path = settings['render96ex-path']
    apply_patch(path)
    copy_texts(path)
    copy_audio(path)

if __name__ == '__main__':
    main()