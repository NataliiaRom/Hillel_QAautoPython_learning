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

    number_found = False
    for child in root:
        for subchild in child:
            if subchild.tag == 'number' and subchild.text == str(number):
                number_found = True
                timing_found = False
                for timex in child:
                    if timex.tag == 'timingExbytes':
                        timing_found = True
                        found_incoming = False
                        for inc in timex:
                            if inc.tag == 'incoming':
                                found_incoming = True
                                if inc.text:
                                    logger.info(f"{log_msg} {inc.text}")
                                else:
                                    logger.warning(f"There is no text for tag 'incoming' found.")
                        if not found_incoming:
                            logger.warning(f"There is no tag 'incoming' found.")
                if not timing_found:
                    logger.warning(f"There is no tag 'timingExbytes' found.")
                return
    if not number_found:
        logger.warning(f"There is no child with number {number} found.")
group_number_search(groups_xml_path, 2)


