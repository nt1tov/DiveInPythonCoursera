import os
import time
import socket

class Client:
    def __init__(self, host, port,  timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        try:
            self.sock = socket.create_connection((self.host, self.port), self.timeout)
        except:
            raise ClientError()


    def get(self, metric_name):

        request_get = "get" + " " + metric_name + "\n"
        try:
            self.sock.sendall(request_get.encode("utf-8"))
        except socket.timeout:
            raise ClientError()
        except socket.error:
            raise ClientError()
        

        try: 
            answer_get = None
            while True:
                answer_get = self.sock.recv(1024) 
                if answer_get:
                    answer_get = answer_get.decode("utf-8").splitlines()
                    if answer_get[0] != "ok":
                        raise ClientError
                    break
        except socket.timeout: 
            raise ClientError()
        except socket.error:
            raise ClientError()

        metrics_map = {}
        
        answer_get = answer_get[1:len(answer_get)-1]

        answer_get = [x for line in answer_get for x in line.split()]
        if len(answer_get) % 3 != 0:
            raise ClientError()
        answer_get = zip(answer_get[::3], answer_get[1::3], answer_get[2::3])

        for key, value, timestamp in answer_get:
            try: 
                val = float(value)
                tstamp = int(timestamp)
            except ValueError:
                raise ClientError()

            if not key in metrics_map:
                metrics_map[key] = [(tstamp, val)]
            else:
                metrics_map[key].append((tstamp, val))
            for key in metrics_map:
                metrics_map[key].sort(key=lambda tup: tup[0])
        return metrics_map

    def put(self, metric_name, metric_value, metric_timestamp = None):
        
        if metric_timestamp is None:
            metric_timestamp = int(time.time())

        put_msg = "put" + ' ' + metric_name + " " + str(metric_value) \
                    + " " + str(metric_timestamp) + "\n"

        try:
            self.sock.sendall(put_msg.encode("utf-8"))
        except socket.timeout:
            raise ClientError()
        except socket.error as ex:
             raise ClientError()

        try: 
            answer_get = None
            while True:
                answer_get = self.sock.recv(1024)
                if answer_get:
                    break
        except socket.timeout: 
            raise ClientError()
        except socket.error: 
            raise ClientError()
        result = answer_get.decode("utf-8").splitlines()
        if result[0] != "ok":
            raise ClientError()



    def close(self):
        self.sock.close()


class ClientError(Exception):
    pass