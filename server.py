import socket
import psutil

class Server:
    """Return data about your server"""

    def __init__(self):
        host = socket.gethostname()
        host_ip = socket.gethostbyname(host)        
        print('Hostname: {} \nIP: {}'.format(host, host_ip))

    def get_cpu_percent(self):
        """Return CPU percent

        Returns:
            float: Return a number between 0.00 and 100.0
        """
        return psutil.cpu_percent()

    def get_processes(self):
        """Retrurn all process

        Returns:
            list: list of all processes
        """ 
        processes = []
        for process in psutil.process_iter():
            process_info = process.as_dict(attrs=['pid', 'name', 'cpu_percent']) 
            processes.append(process_info)

        return processes

    def get_process(self, pid):
        """Return a process using the id

        Args:
            pid (int): process id

        Returns:
            psutil.Process: Objetct psutil Process
        """
        return psutil.Process(pid)

    def kill_process(self, process):
        """Kill a process using an instance psutil.Process

        Args:
            process (instance psutil.Process): instance psutil.Process
        """
        process.kill()
