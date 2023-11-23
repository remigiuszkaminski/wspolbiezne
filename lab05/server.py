import sysv_ipc
import os
import time

def translate(word):
    dictionary = {"ogórek": "cucumber", "pomidor": "tomato", "jabłko": "apple", "gruszka": "pear" }
    return dictionary.get(word, "Brak tłumaczenia")

def main():
    input_queue_key=2002
    output_queue_key=2023

    input_queue = sysv_ipc.MessageQueue(input_queue_key, sysv_ipc.IPC_CREAT)
    output_queue = sysv_ipc.MessageQueue(output_queue_key, sysv_ipc.IPC_CREAT)

    while True:
        message, t = input_queue.receive()
        time.sleep(2)
        word = message.decode("utf-8")
        translation = translate(word)

        response = f"{os.getpid()}: {word} - {translation}"
        output_queue.send(response.encode("utf-8"), type=t)

if __name__ == "__main__":
    main()