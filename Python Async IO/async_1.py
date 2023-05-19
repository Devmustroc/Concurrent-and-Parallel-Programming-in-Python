import time

start_code_time = time.time()
def waiter(customer_request, duration):
    print(f"waiter start: {customer_request} received")
    time.sleep(duration)
    print(f"waiter end: {customer_request} served")

def main():
    waiter("pizza", 3)
    waiter("sallad", 2)
    waiter("lasagna", 5)
    print(f"total time: {round(time.time() - start_code_time), 1}")

if __name__ == "__main__":
    main()
    print(f"total time: {round(time.time() - start_code_time), 1}")
