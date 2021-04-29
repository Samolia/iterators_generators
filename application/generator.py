from hashlib import md5


def md5_hash_creator(file_path):
    with open(file_path, 'r', encoding='utf-8') as links:
        for line in links.readlines():
            yield md5(line.encode()).hexdigest()
