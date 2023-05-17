import os

from dotenv import load_dotenv


def loadenv():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(os.path.join(base_dir, ".env"))
