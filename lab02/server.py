import os
import time

def main():
    while True:
        lockfile = "lockfile.lock"
        if not os.path.exists(lockfile):
            clientf = ""
            with open("input.txt", "r") as f:
                clientf = f.readline().strip()
            if not clientf:
                continue
            with open("input.txt", "r") as serf:
                print("Client text:")
                for line in input:
                    print(line, end="")
                with open("clientf.txt", "w") as clientf:
                    while True:
                        line = input("Enter line: ")
                        if line == "":
                            break
                        clientf.write(line + "\n")
            os.remove("input.txt")
        else:
            time.sleep(1)
            continue


if __name__ == "__main__":
    main()
