from pprint import pprint

# Example input config
example_input = {
    "service_version": "2022.08.02",
    "logs_store": {
        "remote": {
            "url": "https://elk",
            "user": "some_user",
            "password": "some_password"
        },
        "local": "$HOME/service.log"
    },
    "message_broker":
        {
            "url": "https://rabbitmq",
            "user": "rmq",
            "password": "some_password"
        }
}

# Example output
expected = {
    "service_version": "2022.08.02",
    "logs_store.remote.url": "https://elk",
    "logs_store.remote.user": "some_user",
    "logs_store.remote.password": "some_password",
    "logs_store.local": "$HOME/service.log",
    "message_broker.url": "https://rabbitmq",
    "message_broker.user": "rmq",
    "message_broker.password": "some_password"
}


def flatten_config(input_dict: dict, prefix=None) -> dict:
    """ Flatten a given config using recursion. """
    result = {}
    for key, value in input_dict.items():
        key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, str):
            result[key] = value
        else:
            result.update(flatten_config(value, prefix=key))
    return result


pprint(flatten_config(example_input))
