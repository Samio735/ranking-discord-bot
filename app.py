import discord
import dotenv
import os
import requests
import json
dotenv.load_dotenv()
url = os.getenv('URL')
class MyClient(discord.Client):
    async def on_ready(self):
            resp = requests.get(url)
            print(resp.status_code)
            data = resp.json()
            print(data["members"][0])
            i = 1
            for member in data["members"]:
                print("Rank {}  {}  {}p".format(i,member["name"],member["points"]))
                i = i + 1
            json_data = json.dumps(data)
            truncated_data = json_data[:400]

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        # if message.name != "samyrahim07":
        #     return
        
        if True:
            resp = requests.get(url)
            print(resp.status_code)
            if resp.status_code != 200:
                # This means something went wrong.
                await message.channel.send('Something went wrong')
            else:
                data = resp.json()
                i = 1
                j = 0
                msg = [""]
                for member in data["members"]:
                    msg[j] = msg[j] +  "Rank {}  {}  {}p \n".format(i,member["name"],member["points"])
                    i = i + 1
                    print(msg[j])
                    if i % 61 == 0:
                        j = j + 1
                        msg.append("")
                for m in msg:
                    await message.channel.send(m)

                
                
                        
            

intents = discord.Intents(messages=True)
client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))


