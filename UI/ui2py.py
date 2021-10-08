import os
import re

def generate_all_ui2py(path):
    files = os.listdir(path)
    pattern = re.compile(r'.*\.ui')
    ui_list = [i for i in files if pattern.match(i)]

    for i in ui_list:
        file_path = os.path.join(path, i)
        file_name_without_extension = file_path.split(os.sep)[-1].removesuffix('.ui')
        cmd = f'pyside6-uic {file_path} > {path}{os.sep}{file_name_without_extension}.py'
        os.popen(cmd)

if __name__ == '__main__':
    generate_all_ui2py(os.path.dirname(os.path.abspath(__file__)))
