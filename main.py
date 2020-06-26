from server import Server
from datetime import datetime

def log_generator(processs_to_kill, processes_found, processes_killed):
    date = datetime.now()
    date = date.strftime('%B %dth, %Y at %X')
    PATH_LOG = '/var/log/server_cleaner_log.txt'
    
    with open(PATH_LOG, 'a') as f:
        f.write('**SERVER CLEANER** Start on {}\n'.format(date))
        f.write('Process to kill: {}* \n'.format(processs_to_kill))
        
        f.write('Processes found to kill: \n')
        if len(processes_found) == 0:
            f.write('\t* No process was found\n')

        for ps in processes_found:
            f.write('\t* {}\n'.format(ps))
        
        f.write('Processes killed: \n')
        if len(processes_found) == 0:
            f.write('\t* No process was found to kill\n')

        for ps in processes_killed:
            f.write('\t* {}\n'.format(ps))

        if processes_found == processes_killed:
            f.write('-- Server cleaner executed successfully.\n')
        else:
            f.write('-- Server cleaner executed unsuccessfully.\n')

        f.write('{}\n\n'.format('*** ' * 10))

    print('Logs saved in {}'.format(PATH_LOG))
        

def main():
    processes = SERVIDOR.get_processes()
    process_to_kill = 'php'
    processes_found = [SERVIDOR.get_process(ps['pid']) for ps in processes if ps['name'] == process_to_kill]
    processes_killed = []
    for ps in processes_found:
        SERVIDOR.kill_process(ps)
        processes_killed.append(ps)

    log_generator(process_to_kill, processes_found, processes_killed)
    

if __name__ == '__main__':
    print("""
   ____                       _______                     
  / __/__ _____  _____ ____  / ___/ /__ ___ ____  ___ ____
 _\ \/ -_) __/ |/ / -_) __/ / /__/ / -_) _ `/ _ \/ -_) __/
/___/\__/_/  |___/\__/_/    \___/_/\__/\_,_/_//_/\__/_/   
                
                - NEXGEN SOLUTIONS -
    """)    
    SERVIDOR = Server()
    main()