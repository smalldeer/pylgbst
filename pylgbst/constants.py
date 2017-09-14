# GENERAL
LEGO_MOVE_HUB = "LEGO Move Hub"
DEVICE_NAME = 0x07
MOVE_HUB_HARDWARE_HANDLE = 0x0E
MOVE_HUB_HARDWARE_UUID = '00001624-1212-efde-1623-785feabcd123'

ENABLE_NOTIFICATIONS_HANDLE = 0x000f
ENABLE_NOTIFICATIONS_VALUE = b'\x01\x00'

PACKET_VER = 0x01

# COLORS
COLOR_BLACK = 0x00
COLOR_PINK = 0x01
COLOR_PURPLE = 0x02
COLOR_BLUE = 0x03
COLOR_LIGHTBLUE = 0x04
COLOR_CYAN = 0x05
COLOR_GREEN = 0x06
COLOR_YELLOW = 0x07
COLOR_ORANGE = 0x09
COLOR_RED = 0x09
COLOR_WHITE = 0x0a
COLORS = {
    COLOR_BLACK: "BLACK",
    COLOR_PINK: "PINK",
    COLOR_PURPLE: "PURPLE",
    COLOR_BLUE: "BLUE",
    COLOR_LIGHTBLUE: "LIGHTBLUE",
    COLOR_CYAN: "CYAN",
    COLOR_GREEN: "GREEN",
    COLOR_YELLOW: "YELLOW",
    COLOR_ORANGE: "ORANGE",
    COLOR_RED: "RED",
    COLOR_WHITE: "WHITE"
}

# PORTS
PORT_C = 0x01
PORT_D = 0x02
PORT_LED = 0x32
PORT_A = 0x37
PORT_B = 0x38
PORT_AB = 0x39
PORT_TILT_SENSOR = 0x3a
PORT_SOMETHING1 = 0x3B
PORT_SOMETHING2 = 0x3C

PORTS = {
    PORT_A: "A",
    PORT_B: "B",
    PORT_AB: "AB",
    PORT_C: "C",
    PORT_D: "D",
    PORT_LED: "LED",
    PORT_TILT_SENSOR: "TILT_SENSOR",
    PORT_SOMETHING1: "UNK1",
    PORT_SOMETHING2: "UNK2",
}

# PACKET TYPES
MSG_DEVICE_INFO = 0x01
MSG_PING_RESPONSE = 0x03
MSG_PORT_INFO = 0x04
MSG_PORT_CMD_ERROR = 0x05
MSG_SET_PORT_VAL = 0x81
MSG_PORT_STATUS = 0x82
MSG_SENSOR_SUBSCRIBE = 0x41
MSG_SENSOR_SOMETHING = 0x42
MSG_SENSOR_DATA = 0x45
MSG_SENSOR_SUBSCRIBE_ACK = 0x47

# NOTIFICATIONS
TYPE_DISTANCE_COLOR_SENSOR = 0x25
TYPE_IMOTOR = 0x26
TYPE_MOTOR = 0x27
TYPE_TILT_SENSOR = 0x28
TYPE_LED = 0x17
# one of them is button? another is battery?
TYPE_SOMETHING1 = 0x15
TYPE_SOMETHING2 = 0x14

DEVICE_TYPES = {
    TYPE_DISTANCE_COLOR_SENSOR: "DISTANCE_COLOR_SENSOR",
    TYPE_IMOTOR: "IMOTOR",
    TYPE_MOTOR: "MOTOR",
    TYPE_TILT_SENSOR: "TILT_SENSOR",
    TYPE_LED: "LED",
    TYPE_SOMETHING1: "UNK1",
    TYPE_SOMETHING2: "UNK2",
}

STATUS_STARTED = 0x01
STATUS_CONFLICT = 0x05
STATUS_FINISHED = 0x0a

# TILT
TILT_SENSOR_MODE_2AXIS_FULL = 0x00
TILT_SENSOR_MODE_2AXIS_SIMPLE = 0x01
TILT_SENSOR_MODE_BASIC = 0x02
TILT_SENSOR_MODE_BUMP = 0x03
TILT_SENSOR_MODE_FULL = 0x04

TILT_HORIZONTAL = 0x00
TILT_UP = 0x01
TILT_DOWN = 0x02
TILT_RIGHT = 0x03
TILT_LEFT = 0x04
TILT_FRONT = 0x05
TILT_SOME1 = 0x07
TILT_SOME2 = 0x09

TILT_STATES = {
    TILT_HORIZONTAL: "HORIZONTAL",
    TILT_UP: "UP",
    TILT_DOWN: "DOWN",
    TILT_RIGHT: "RIGHT",
    TILT_LEFT: "LEFT",
    TILT_FRONT: "FRONT",
    TILT_SOME1: "LEFT1",
    TILT_SOME2: "SOME2",
}

# COLOR & DISTANCE SENSOR
CLR_DIST_MODE_COLOR_ONLY = 0x00
CLR_DIST_MODE_DISTANCE_INCHES = 0x01
CLR_DIST_MODE_COUNT_2INCH = 0x02
CLR_DIST_MODE_DISTANCE_HOW_CLOSE = 0x03
CLR_DIST_MODE_DISTANCE_SUBINCH_HOW_CLOSE = 0x04
CLR_DIST_MODE_OFF1 = 0x05
CLR_DIST_MODE_STREAM_3_VALUES = 0x06
CLR_DIST_MODE_OFF2 = 0x07
CLR_DIST_MODE_COLOR_DISTANCE_INCHES_SUBINCHES = 0x08
CLR_DIST_MODE_LUMINOSITY = 0x09
CLR_DIST_MODE_SOME_14BYTES = 0x0a
