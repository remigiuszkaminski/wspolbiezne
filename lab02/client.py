import os
import time


def main():
    lockfile = "lockfile.lock"
    clientf = input("Enter file name: ")
    while True:
        if not os.path.exists(clientf):
            with open("clientf", "w") as file:
                pass
        with open("clientf", "r") as clientI:
            if os.stat(clientf).st_size == 0:
                pass
            else:
                print("Reponse ")
                for line in clientI:
                    print(line, end="")
                break
        if os.path.exists(lockfile):
            print("Server is busy")
            time.sleep(2)
            continue
        with open(lockfile, "w") as lock:
            lock.write("lock")

        with open("serverI.txt", "w") as file:
            file.write(clientf + "\n")
            while True:
                line = input("Enter line: ")
                if line == "":
                    break
                file.write(line + "\n")



if __name__ == "__main__":
    main()


