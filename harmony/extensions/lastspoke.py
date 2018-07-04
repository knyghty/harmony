import datetime

import discord
from discord.ext import commands

import sqlalchemy as sa

from db.base import Base


class LatestUtterance(Base):
    __tablename__ = 'latestutterance'

    user_id = sa.Column(sa.String, primary_key=True)
    uttered_time = sa.Column(sa.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    utterance = sa.Column(sa.String)


class LastSpoke:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lastspoke(self, user: discord.Member):
        session = self.bot.Session()
        try:
            utterance = session.query(LatestUtterance).filter(LatestUtterance.user_id == user.id)[0]
        except IndexError:
            await self.bot.say('Nothing found.')
            return
        member = user.server.get_member(utterance.user_id)
        embed = discord.Embed(description=utterance.utterance, timestamp=utterance.uttered_time, color=member.color)
        embed.set_author(name=member.display_name, icon_url=member.avatar_url)
        await self.bot.say(embed=embed)

    async def update(self, message):
        session = self.bot.Session()
        try:
            utterance = session.query(LatestUtterance).filter(LatestUtterance.user_id == message.author.id)[0]
        except IndexError:
            utterance = LatestUtterance(user_id=message.author.id)

        utterance.utterance = message.content
        session.add(utterance)
        session.commit()


def setup(bot):
    bot.add_listener(LastSpoke(bot).update, 'on_message')
    bot.add_cog(LastSpoke(bot))
