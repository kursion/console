HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def _print(color, message):
    print(color+message+ENDC)


def success(message):
    _print(OKGREEN, message)


def log(message):
    _print(OKBLUE, message)


def header(message):
    _print(HEADER, message)


def title(message):
    _print(HEADER+BOLD, message)


def error(message):
    _print(FAIL, message)


def warning(message):
    _print(WARNING, message)


# ALIAS error
def fail(message):
    error(message)


def warn(message):
    warning(message)


def ok(message):
    success(message)
