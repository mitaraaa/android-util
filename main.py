import re
import os
import sys

sys.stderr = open(os.devnull, "w")

try:
    import psutil
finally:
    sys.stderr = sys.__stderr__

from pyrogram import Client


bot_token = "5447852667:AAFL9hHSz5fgTqxZFmsPziA48Y_JtRcHYXo"
bot = Client(
    name="xdxdroid", api_id="19772261", api_hash="19772261", bot_token=bot_token
)


def get_data() -> tuple:
    temperature = str(
        re.findall(r"\w+=([^,)]+)", str(psutil.sensors_temperatures()["battery"][0]))[1]
    )
    battery = psutil.sensors_battery()
    plugged = str(battery.power_plugged)
    percent = str(battery.percent)

    return temperature, percent, plugged


@bot.on_message()
async def handler(client, message):
    data = get_data()
    text = f"""
    Poco X3 PRO
    Battery: {data[1]}% {"| Charging" if data[2] else ""}
    Temperature: {data[0]}"""
    async with bot:
        await bot.send_message(842767405, text)


bot.run()
