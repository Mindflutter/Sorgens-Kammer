"""
Написать программу на Python, которая делает следующие действия:

1. Создает 50 zip-архивов, в каждом 100 xml файлов со случайными данными следующей структуры:

 <root>
<var name=’id’ value=’<случайное уникальное строковое значение>’/>
<var name=’level’ value=’<случайное число от 1 до 100>’/>
<objects>
<object name=’<случайное строковое значение>’/>
<object name=’<случайное строковое значение>’/>
…
</objects>
</root>

В тэге objects случайное число (от 1 до 10) вложенных тэгов object.

2. Обрабатывает директорию с полученными zip архивами, разбирает вложенные xml файлы и формирует 2 csv файла:

Первый: id, level - по одной строке на каждый xml файл
Второй: id, object_name - по отдельной строке для каждого тэга object (получится от 1 до 10 строк на каждый xml файл)

Очень желательно сделать так, чтобы задание 2 эффективно использовало ресурсы многоядерного процессора.
Также желательно чтобы программа работала быстро.
"""
import multiprocessing
import os
import os.path as op
import random
import string
import time
import uuid
from zipfile import ZipFile

from lxml import etree as ET

ZIP_COUNT = 50
XML_COUNT = 100
CPU_COUNT = multiprocessing.cpu_count()

BASE_DIR = "work"
if not op.exists(BASE_DIR):
    os.mkdir(BASE_DIR)


def generate_xml():
    """ Generate a single XML according to task specification. """
    root = ET.Element("root")
    ET.SubElement(root, "var", attrib={"name": "id", "value": str(uuid.uuid4())})
    level_num = random.randint(1, 100)
    ET.SubElement(root, "var", attrib={"name": "level", "value": str(level_num)})
    objects = ET.SubElement(root, "objects")

    objects_num = random.randint(1, 10)
    for _ in range(objects_num):
        object_name = "".join([random.choice(string.ascii_lowercase) for _ in range(10)])
        ET.SubElement(objects, "object", attrib={"name": object_name})
    # note: tostring returns binary string
    return ET.tostring(root, pretty_print=True)


def pack_archive(name):
    """ Create a single archive. """
    with ZipFile(f"{BASE_DIR}/{name}", "w") as zfile:
        for i in range(XML_COUNT):
            zfile.writestr(f"{i}.xml", generate_xml())


def create_archives():
    """ Create N archives via multiprocessing. """
    with multiprocessing.Pool(CPU_COUNT) as pool:
        pool.map(pack_archive, [f"{i}.zip" for i in range(ZIP_COUNT)])


def init_csv():
    """ Create resulting csv"s with appropriate headers. """
    with open(f"{BASE_DIR}/first.csv", "w") as first, \
            open(f"{BASE_DIR}/second.csv", "w") as second:
        first.write("id,level\n")
        second.write("id,object_name\n")


def delete_csv():
    """ Cleanup csv"s from filesystem. """
    os.unlink(f"{BASE_DIR}/first.csv")
    os.unlink(f"{BASE_DIR}/second.csv")


def parse_xml(xml):
    """ Parse a single XML according to task specification. """
    doc = ET.fromstring(xml)

    # get values for the first csv
    vars_ = doc.findall("var")
    id_ = vars_[0].get("value")
    level = vars_[1].get("value")
    first_row = f"{id_},{level}"

    # get values for the second csv
    objects = doc.find("objects")
    second_rows = [f"{id_},{obj.get('name')}" for obj in objects.getchildren()]
    return first_row, second_rows


def process_all_archives():
    """ Process all archives sequentially. """
    with open(f"{BASE_DIR}/first.csv", "a") as first, \
            open(f"{BASE_DIR}/second.csv", "a") as second:
        for i in range(ZIP_COUNT):
            first_bunch, second_bunch = process_archive(f"{i}.zip")
            data_first = "\n".join(first_bunch) + "\n"
            first.write(data_first)
            data_second = "\n".join(second_bunch) + "\n"
            second.write(data_second)


def process_archive(name):
    """ Process a single archive, retrieving rows from packed XML"s. """
    with ZipFile(f"{BASE_DIR}/{name}") as zfile:
        first_bunch = []
        second_bunch = []
        for j in range(XML_COUNT):
            f = zfile.open(f"{j}.xml")
            xml = f.read()
            first_row, second_rows = parse_xml(xml)
            first_bunch.append(first_row)
            second_bunch.extend(second_rows)
        return first_bunch, second_bunch


def main():
    """ Entry point with main logic. """
    start = time.time()
    create_archives()
    print("Creating archives took", time.time() - start)

    # single process
    init_csv()
    start = time.time()
    process_all_archives()
    print("Single process took", time.time() - start)
    delete_csv()

    # multiprocessing
    init_csv()
    start = time.time()
    with multiprocessing.Pool(CPU_COUNT) as pool:
        with open(f"{BASE_DIR}/first.csv", "a") as first, \
                open(f"{BASE_DIR}/second.csv", "a") as second:
            for result in pool.imap_unordered(process_archive, [f"{i}.zip" for i in range(50)]):
                # combine retrieved data and write it to result files
                first_bunch, second_bunch = result
                data_first = "\n".join(first_bunch) + "\n"
                first.write(data_first)
                data_second = "\n".join(second_bunch) + "\n"
                second.write(data_second)
    print("Multiprocessing took", time.time() - start)


if __name__ == "__main__":
    main()
