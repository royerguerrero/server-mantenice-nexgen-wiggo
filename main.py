from server import Server

def main():
    servidor = Server()
    processes = servidor.get_processes()
    process_to_kill = 'php'
    processes_found = [servidor.get_process(ps['pid']) for ps in processes if ps['name'] == process_to_kill]
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