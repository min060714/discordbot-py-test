
import re
import traceback

import discord

EMOJI_REGEX = r"^<(a)?:(.+?):([0-9]{15,21})>$"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    print(f"{client.user} Online!")


@client.event
async def on_message(message: discord.Message) -> None:
    if not message.guild or message.author.bot:
        return

    if (m := re.match(EMOJI_REGEX, message.content)):
        try:
            color = message.author.color if message.author.color != discord.Colour.default() else 0xffffff
            ext = "gif" if m.group(1) else "png"

            embed = discord.Embed(color=color)
            embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar)
            embed.set_image(url=f"https://cdn.discordapp.com/emojis/{m.group(3)}.{ext}")
            #embed.set_footer(text=m.group(2))

            await message.delete()
            await message.channel.send(embed=embed, reference=message.reference, mention_author=False)
        except:
            #traceback.print_exc()
            pass




client.run('MTA3NTMyNzU0NDkzNDUzNTIzOQ.G1LTQW.qp6ekij3VWIO2imGBNRavaq7VuFJwmCUtIQm5Y')
