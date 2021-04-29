import os
from application.iterator import LinksCreator
from application.generator import md5_hash_creator


def dir_create(dir_name):
    if os.path.exists(dir_name) is False:
        os.mkdir(dir_name)
    return dir_name


def links_saver(file_path):
    print(f'Ссылки сформированы. Проверьте файл - {file_path}')
    with open(file_path, 'w', encoding='utf-8') as links:
        for link_to_country in LinksCreator('data/countries.json'):
            links.write(f'{link_to_country}\n')


def hash_saver(md5_hash_file, file_path):
    print(f'Захешировал файл - {file_path}. Проверьте файл - {md5_hash_file}')
    with open(md5_hash_file, 'w') as md5_hash:
        for my_hash in md5_hash_creator(file_path):
            md5_hash.write(f'{my_hash}\n')
