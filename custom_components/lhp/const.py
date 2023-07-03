"""Constants for the LHP integration."""
from logging import Logger, getLogger
from datetime import timedelta


LOGGER: Logger = getLogger(__package__)

NAME = "Hochwasserportal"
DOMAIN = "lhp"
VERSION = "0.0.2"
SCAN_INTERVAL = timedelta(minutes=30)
