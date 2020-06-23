import socket
import psutil

class Server:
    """Return data about your server"""

    def __init__(self):
        host = socket.gethostname()
        host_ip = socket.gethostbyname(host)        
        print(f'Hostname: {host} \nIP: {host_ip}')

    def get_cpu_percent(self):
        """Return CPU percent

        Returns:
            float: Return a number between 0.00 and 100.0
        """
        return psutil.cpu_percent()

    def get_processes(self):
        """Retrurn all process

        Returns:
            [type]: [description]
        """ 
        processes = []
        for process in psutil.process_iter():
            process_info = process.as_dict(attrs=['pid', 'name', 'cpu_percent']) 
            processes.append(process_info)

        return processes

    def get_process(self, pid):
        """[summary]

        Args:
            pid (int): [description]

        Returns:
            [type]: [description]
        """
        return psutil.Process(pid)

    def kill_process(self, process):
        """[summary]

        Args:
            process ([type]): [description]
        """
        process.kill()
