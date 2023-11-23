import sysv_ipc
import os
import random


def main():
    input_queue_key=2002
    output_queue_key=2023

    input_queue = sysv_ipc.MessageQueue(input_queue_key, sysv_ipc.IPC_CREAT)
    output_queue = sysv_ipc.MessageQueue(output_queue_key, sysv_ipc.IPC_CREAT)

    word = input("Podaj słowo do przetłumaczenia: ")

    input_queue.send(word.encode('utf-8'), type=os.getpid())

    response, _ = output_queue.receive(type=os.getpid())
    print(f"Odpowiedź serwera:{response.decode('utf-8')}")

if __name__ == "__main__":
    main()