import threading
from time import sleep,time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

time_start = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time()
print(f"Время выполнения записи в файлы: {round(time_end - time_start,2)} секунд")

time_start = time()
file_params = [(10, 'example5.txt'),(30, 'example6.txt'),(200, 'example7.txt'),(100, 'example8.txt'),]
threads = []

for params in file_params:
    thread = threading.Thread(target=write_words, args=params)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

time_end = time()
print(f"Время выполнения записи в файлы: {round(time_end - time_start,2)} секунд")