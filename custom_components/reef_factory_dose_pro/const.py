"""Constants for Reef Factory Dosing Pump Pro integration."""

from datetime import timedelta

DOMAIN = "reef_factory_dose_pro"

WS_URL = "wss://api.reeffactory.com:443/controler"
WS_PROTOCOL = "reeffactory"

CONF_EMAIL = "email"
CONF_PASSWORD = "password"
CONF_SERIAL = "serial"

UPDATE_INTERVAL = timedelta(minutes=30)
WS_TIMEOUT = 45
WS_RECEIVE_TIMEOUT = 15
WS_MAX_MESSAGES = 30

SCALE = 1 / 100

# Updated for single-channel Dosing Pump Pro
CHANNELS = (1,)
CHANNEL_NAMES = {1: "A"}

# History entry types that represent automated Reef Factory actions
ACTION_TYPES = frozenset(range(5, 11))  # 5,6,7,8,9,10