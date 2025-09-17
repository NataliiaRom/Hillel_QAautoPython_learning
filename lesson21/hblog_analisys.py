import logging
from datetime import datetime, timedelta

logger = logging.Logger('time analysis')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('hb_test.log')
formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


def heartbeat_analysis(file_name):
    stream_sample = "TSTFEED0300|7E3E|0400"

    with open(file_name, 'r') as file:
        # selecting unique heartbeat lines, based on a stream_sample
        unique_heartbeat_lines = []
        for line in file.readlines():
            line_list = line.split()
            if stream_sample in line and line not in unique_heartbeat_lines:
                unique_heartbeat_lines.append(line)

        # extracting timestamps from each line
        timestamps_list = []
        for line in unique_heartbeat_lines:
            initial_timestamp_index = line.find("Timestamp ") + 10
            line_part_with_timestamp = line[initial_timestamp_index:(initial_timestamp_index + 8)]
            timestamp_conversion = datetime.strptime(line_part_with_timestamp, '%H:%M:%S')
            timestamps_list.append(timestamp_conversion)

        # looking for the unnormal timebeat frequency
        timestamps_list.sort(reverse=True)

        for i in range(len(timestamps_list) - 1):
            time_first = timestamps_list[i]
            time_next = timestamps_list[i + 1]
            diff = time_first - time_next
            if timedelta(seconds=31) <= diff < timedelta(seconds=33):
                logger.warning(
                    f"The heartbeat frequency is between 31 and 32 sec between {time_first.time()} and {time_next.time()}")
            elif diff >= timedelta(seconds=33):
                logger.error(
                    f"The heartbeat frequency reached or exceeded 33 sec between {time_first.time()} and {time_next.time()}")


file = 'hblog.txt'

heartbeat_analysis(file)
