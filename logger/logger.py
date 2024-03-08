import datetime
import logging
import os


class log_manager:

    file_path = '/data/dashboard/app_log/'
    file_name = 'monitor_log'

    if not os.path.isdir(file_path):
        os.makedirs(file_path)

    date_info = datetime.datetime.now()

    log_format = '%(asctime)s - %(name)s- %(levelname)s - %(message)s'

    log_file = file_path + file_name

    try:
        logging.basicConfig(filename=log_file,
                            format=log_format,
                            level=logging.DEBUG)
    except:
        f = open(log_file)
        f.close()
        logging.basicConfig(filename=log_file,
                            format=log_format,
                            level=logging.DEBUG)

    logger = logging.getLogger(__name__)

    def write_error(self, s):
        self.logger.error(": " + s)

    def write_debug(self, s):
        self.logger.debug(": " + s)


lm = log_manager()
