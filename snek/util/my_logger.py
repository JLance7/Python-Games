import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    format=f'%(asctime)s - %(levelname)s - %(filename)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger.setLevel(logging.INFO)