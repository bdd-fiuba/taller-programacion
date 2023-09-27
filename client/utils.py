from os import getenv


def get_host():
    return (
        "localhost"
        if getenv("IS_CONTAINER", "false").lower() == "false"
        else "webserver"
    )


def get_port():
    return 9505
