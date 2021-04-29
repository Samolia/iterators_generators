from application.preservers import dir_create, links_saver, hash_saver


def main():
    links_saver(f'{dir_create("output")}/{"links_to_wiki.txt"}')
    hash_saver(f'{dir_create("output")}/{"md5_hash.txt"}', "output/links_to_wiki.txt")


if __name__ == '__main__':
    main()
