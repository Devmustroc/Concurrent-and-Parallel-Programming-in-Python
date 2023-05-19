import time
import threading


def calculate_sum_square(n):
    sum_square = 0
    for i in range(n):
        sum_square += i ** 2
    print(sum_square)


def sleep_a_title(seconds):
    time.sleep(seconds)


def main():
    calc_start_time = time.time()
    for i in range(5):
        maximum_value = (i + 1) * 1000000
        t = threading.Thread(target=calculate_sum_square, args=(maximum_value,))
        # calculate_sum_square((i + 1) * 1000000)
    print('calculating sum of squares took: ', round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()

    for seconds in range(1, 6):
        t = threading.Thread(target=sleep_a_title, args=(seconds,))
        # sleep_a_title(i)

    print('sleeping took: ', round(time.time() - sleep_start_time, 1))

if __name__ == '__main__':
    main()
