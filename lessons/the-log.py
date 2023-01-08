import logging


def write_log():
    logging.basicConfig(format='%(levelname)s:%(message)s',
                        filemode='a',
                        filename='../supplemental/logging/example.log',
                        level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')


def test():
    logging.basicConfig(format='%(levelname)s:%(message)s',
                        level=logging.DEBUG)
    logging.warning("Your %s was executed successfully, but the %s is wrong!", "script", "output")


def write_better_log():
    # STEP 1
    # create a logger object instance
    logger = logging.getLogger()

    # STEP 2
    # specify the lowest boundary for logging
    logger.setLevel(logging.DEBUG)

    # STEP 3
    # set a destination for your logs or a handler
    # here, we choose to print on console (a console handler)
    # ---change from StreamHandler to FileHandler---
    # console_handler = logging.StreamHandler()
    console_handler = logging.FileHandler('../supplemental/logging/better-example.log')
    console_handler.mode = 'a'

    # STEP 4
    # set the logging format for your handler
    log_format = '%(asctime)s | %(levelname)s: %(message)s'
    console_handler.setFormatter(logging.Formatter(log_format))

    # finally, add the handler to the logger
    logger.addHandler(console_handler)

    # start the logging and show the messages
    logger.debug('Here you have some information for debugging.')
    logger.info('Everything is OK. Keep going!')
    logger.warning("Something strange has happened, but it's not critical.")
    logger.error('Something unexpected and critical has happened.')
    logger.critical('A critical error! The code cannot run!')


if __name__ == '__main__':
    # write_log()
    test()
    # write_better_log()
