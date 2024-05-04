import asyncio
import argparse

from client import TorrentClient
from torrent import Torrent


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('f', type=argparse.FileType('r'), nargs='*')
        self.args = self.parser.parse_args()

    def files(self):

        return [file.name for file in self.args.f]


async def main(*args):
    trackers = []
    for f in args:
        client = TorrentClient(Torrent(f))
        task = loop.create_task(client.start())
        peers = await client.get_info()
        trackers.append(peers)
        await client.stop()
        task.cancel()
    print(trackers)


if __name__ == '__main__':
    parser = Parser()
    files = parser.files()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(*files))
    loop.close()




