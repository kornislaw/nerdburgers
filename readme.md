# NerdBurger

A simple JSON-based API for collecting lunch orders in the office.

```json
{
    "404": "The API call you tried to make was not defined. Here's a definition of the API to help you get going :)",
    "documentation": {
        "overview": " A simple API for collecting lunch orders.\n    The person who makes jokes causing chaos on the list will be the delivery boy.\n",
        "handlers": {
            "/order": {
                "GET": {
                    "usage": " If you want to place an order, use /order?who=[your name]&what=[your pick]",
                    "examples": [
                        "http://localhost:8000/order?who=Big Dummy&what=MegaBurger"
                    ],
                    "outputs": {
                        "format": "JSON (Javascript Serialized Object Notation)",
                        "content_type": "application/json"
                    },
                    "inputs": {
                        "who": {
                            "type": "Basic text / string value"
                        },
                        "what": {
                            "type": "Basic text / string value"
                        }
                    }
                }
            },
            "/orders": {
                "GET": {
                    "usage": " Returns the current list of orders ",
                    "examples": [
                        "http://localhost:8000/orders"
                    ],
                    "outputs": {
                        "format": "JSON (Javascript Serialized Object Notation)",
                        "content_type": "application/json"
                    }
                }
            },
            "/remove": {
                "GET": {
                    "outputs": {
                        "format": "JSON (Javascript Serialized Object Notation)",
                        "content_type": "application/json"
                    },
                    "inputs": {
                        "id": {
                            "type": "Basic text / string value"
                        }
                    }
                }
            }
        }
    }
}
```


## Sample output

```json
{
    "data": [
        [
            {
                "id": 1,
                "who": "Big Dummy",
                "what": "MegaBurger",
                "actions": {
                    "remove": "http://localhost:8000/remove?id=1"
                }
            },
            {
                "id": 3,
                "who": "Small Dummy",
                "what": "Small cheese burger and fries",
                "actions": {
                    "remove": "http://localhost:8000/remove?id=3"
                }
            }
        ]
    ],
    "actions": {
        "go back": "http://localhost:8000"
    }
}
```
