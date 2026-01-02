def range_abc(start=0, end=None, step=1):
    if end is None:
        raise ValueError("end cannot be None")

    while start < end:
        yield start
        start += step



for num in range_abc(start=5, end=15, step=2):
    print(num)