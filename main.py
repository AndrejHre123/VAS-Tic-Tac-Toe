import argparse
import asyncio
from SudacAgent import SudacAgent
from IgracAgent import IgracAgent

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-X', choices=['random', 'minmax'], required=True)
    parser.add_argument('-O', choices=['random', 'minmax'], required=True)
    args = parser.parse_args()

    referee = SudacAgent("agent3@localhost", "password3")
    player_x = IgracAgent("agent1@localhost", "password1")
    player_x.strategy = args.X
    player_o = IgracAgent("agent2@localhost", "password2")
    player_o.strategy = args.O

    await referee.start()
    await player_x.start()
    await player_o.start()

    print(f"Agent1 (X) ima strategiju: {args.X}")
    print(f"Agent2 (O) ima strategiju: {args.O}")
    print("Ctrl+C za zaustavljanje.")
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Zaustavljanje agenata...")