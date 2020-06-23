from server import Server

def main():
    servidor = Server()
    if servidor.get_cpu_percent() >= 95.0:
        processes = servidor.get_processes()
        processes_found = [servidor.get_process(ps['pid']) for ps in processes if ps['name'] == 'python3']
        for ps in processes_found:
            servidor.kill_process(ps)


if __name__ == '__main__':
    print("""
   ____                       _______                     
  / __/__ _____  _____ ____  / ___/ /__ ___ ____  ___ ____
 _\ \/ -_) __/ |/ / -_) __/ / /__/ / -_) _ `/ _ \/ -_) __/
/___/\__/_/  |___/\__/_/    \___/_/\__/\_,_/_//_/\__/_/   
                
                - NEXGEN SOLUTIONS -
    """)
    main()