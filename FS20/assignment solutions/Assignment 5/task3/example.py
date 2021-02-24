dictionary = {
    "count": 1,
    "result": {
        "2020-03-26": {
            "confirmed": 11811,
            "deaths": 191,
            "recovered": 131
        }
    }
}

print(list(dictionary['result'].items()))