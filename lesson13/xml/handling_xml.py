"""
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і
повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""
from pathlib import Path
import xml.etree.ElementTree as ET
import logging

# setting up access to the target file
base_path = Path().absolute()
xml_files_path = Path(base_path,'work_with_xml')
for x in xml_files_path.iterdir():
    if x.is_file() and x.name == 'groups.xml':
        groups_xml_path = x

#setting up logger
logger = logging.getLogger('search_in_xml')
log_msg = "The tag 'incoming' has a following value inside:"
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def group_number_search(xml_file,number: int):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall('group'):
        numb = group.find("number")
        if numb is not None and numb.text == str(number):
            timingExbytes = group.find("timingExbytes")
            if timingExbytes is not None:
                incoming = timingExbytes.find("incoming")
                if incoming is not None:
                    return logger.info(incoming.text)
                else:
                    return logger.warning(f"requested 'incoming' value is not found")
            else:
                return logger.warning(f"elt 'timingExbytes' is not found")

    return logger.warning(f"requested elt 'number' is not found")

print(group_number_search(groups_xml_path, 6))


