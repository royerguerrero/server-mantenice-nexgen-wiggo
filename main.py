from server import Server

def main():
    servidor = Server()
    while True:    
        if servidor.get_cpu_percent() >= 95.0:
            processes = servidor.get_processes()
            processes_found = [servidor.get_process(ps['pid']) for ps in processes if ps['name'] == 'python3']
            for ps in processes_found:
                servidor.kill_process(ps)
    
    
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