from server import Server

def main():
    servidor = Server()
    print(servidor.get_cpu_percent())
    print(servidor.get_processes())
    print(servidor.get_process(1))

if __name__ == '__main__':
    print("""   
  _________                                   _________                                  __   
 /   _____/ ______________  __ ___________   /   _____/__ ________ ______   ____________/  |_ 
 \_____  \_/ __ \_  __ \  \/ // __ \_  __ \  \_____  \|  |  \____  |____ \ /  _ \_  __ \   __/
 /        \  ___/|  | \/\   /\  ___/|  | \/  /        \  |  /  |_> >  |_> >  <_> )  | \/|  |  
/_______  /\___  >__|    \_/  \___  >__|    /_______  /____/|   __/|   __/ \____/|__|   |__|  
        \/     \/                 \/                \/      |__|   |__|                       
                                    - NEXGEN SOLUTIONS -
    """)
    main()