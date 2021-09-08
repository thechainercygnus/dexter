from modules import cointracker
from modules import spotify_client
from dotenv import load_dotenv
import datetime
import logging
import discord
import os

load_dotenv()

if not os.path.exists('logs'):
    os.mkdir('logs')

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File handler for logging
handler = logging.FileHandler(
    ('./logs/' + str(datetime.date.today()) + "-dexter-core.log"))
handler.setLevel(logging.INFO)

# Logging format definition
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

client = discord.Client()

my_name = "Dexter"


@client.event
async def on_ready():
    logger.info('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith(my_name):
        logger.info('Dexter was mentioned')
        acknowledgement = f"I'm listening, what can I help you with {message.author.display_name}?"
        await message.channel.send(acknowledgement)

    if msg.startswith('$topsongs'):
        search_term = msg.replace('$topsongs ', '')
        logger.info('Retrieveing top songs for: {0}'.format(search_term))
        topsongs = spotify_client.find_tracks_by_artist(search_term)
        await message.channel.send('I found some songs.')
        for track in enumerate(topsongs['tracks']['items']):
            await message.channel.send(track['name'])

    if msg.startswith('$similarto'):
        search_term = msg.replace('$similarto ', '')
        related_artists = spotify_client.find_similar_artists(search_term)
        i = 0
        while i < 1:
            img = related_artists['artists'][i]['images'][0]['url']
            logger.info(img)
            embed = discord.Embed(title=related_artists['artists'][i]['name'],
                                  url=related_artists['artists'][i]['external_urls']['spotify'],
                                  description='Tracks')
            embed.set_thumbnail(url=img)
            topsongs = spotify_client.find_tracks_by_artist(
                related_artists['artists'][i]['name'])
            j = 1
            for track in enumerate(topsongs['tracks']['items']):
                title = track[1]['name']
                embed.add_field(name=j, value=title, inline=False)
                j += 1
            embed.set_footer(text="Information requested by: {}".format(
                message.author.display_name))
            await message.channel.send(embed=embed)
            i += 1

    if msg.startswith('$cryptotest'):
        await message.channel.send(cointracker.test_connection())

    if msg.startswith('$balance'):
        query_data = msg.split()
        balance = cointracker.wallet_value(query_data[1], query_data[2])
        await message.channel.send(balance)

    if msg.startswith('$pricecheck'):
        query_data = msg.replace('$pricecheck ', '')
        current_price = cointracker.price_check(query_data)
        await message.channel.send(current_price)


client.run(os.getenv('DISCORD_TOKEN'))
