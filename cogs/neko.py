import json

import requests
from discord.ext import commands

import utils


class NekoImage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="neko")
    async def neko(self, ctx: commands.Context):
        """Send a neko image."""
        url_neko_pic = requests.get("https://nekos.life/api/v2/img/neko").json()["url"]
        await ctx.send(f"{url_neko_pic}")
        utils.write_logs("Weeb", f"Sent neko pic ({url_neko_pic})")


def setup(bot: commands.Bot):
    bot.add_cog(NekoImage(bot))
