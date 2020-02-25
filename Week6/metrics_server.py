import asyncio

SUCCESS_ANSWER = "ok\n\n"
WRONG_COMMAND_ANSWER = "error\nwrong command\n\n"
ALLOWED_COMMANDS = ["get", "put"]
DATA_MAP = {}

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
    def get_handler(self, body):
        if len(body) == 1:
            answer = "ok\n"
            for key, value in DATA_MAP.items():
                for pair in value:
                    if key == body[0] or body[0] == '*':
                        print(value)
                        answer += f"{key} {pair[1]} {pair[0]}\n"
            answer += '\n'
            return answer
        else:
            return WRONG_COMMAND_ANSWER

    def put_handler(self, body):
        if len(body) == 3:
            try:
                timestamp = int(body[2])
                value = float(body[1])
            except:
                return WRONG_COMMAND_ANSWER
            
            key = body[0]
            if key not in DATA_MAP:
                DATA_MAP[key] = []
            upd_flag = False
            for elem in DATA_MAP[key]:
                if elem[0] == timestamp:
                    elem[1] = value
                    upd_flag = True
            if not upd_flag:
                DATA_MAP[key].append([timestamp, value])

            return SUCCESS_ANSWER
        else:
            return WRONG_COMMAND_ANSWER

    def parse_data(self, raw_data):
        try:
            cmd, body = raw_data.split(" ", 1)
            if cmd not in ALLOWED_COMMANDS:
                return WRONG_COMMAND_ANSWER

            if body == '':
                return WRONG_COMMAND_ANSWER

            body = body.split()
        except:
            return WRONG_COMMAND_ANSWER

        if cmd == ALLOWED_COMMANDS[0]:
            return self.get_handler(body)
        elif cmd == ALLOWED_COMMANDS[1]:
            return self.put_handler(body)
        else:
            return WRONG_COMMAND_ANSWER

    def data_received(self, data):
        #print(f"Server recieved \"{data.decode()}\"")
        resp = self.parse_data(data.decode())
        #print(f"Server send \"{resp}\"")
        self.transport.write(resp.encode())
    

def _main():
        run_server('127.0.0.1', 8888)

if __name__ == '__main__':
    _main()