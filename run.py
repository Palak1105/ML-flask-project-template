
import logging
from app import app as application
from app import db

logger = logging.getLogger("app")

def main(port=5000, debug=True):
    logger.info("Staring App at Port: {} with Debug Option: {}".format(port, debug))
    application.run(port=port, debug=debug)


if __name__ == '__main__':
    main()
