import timeit
def benchmark_rsa(func, *args, repeat: int = 5) -> float:
    """
    Benchmark RSA encryption/decryption time in milliseconds.
    """
    times = timeit.repeat(lambda: func(*args), repeat=repeat, number=1)
    return (sum(times)/len(times)) * 1000  # ms