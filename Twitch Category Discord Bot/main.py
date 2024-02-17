import discord
import discord.ext import commands
import requests

# Function to fetch active streams in the specified game category
def get_active_streams_in_category(game_id, client_id, oauth_token):
    url = "https://api.twitch.tv/helix/streams"
    headers = {
        "Client-ID": client_id,
        "Authorization": "Bearer " + oauth_token
    }
    params = {
        "game_id": game_id
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        print("Error:", response.status_code)
        return []

# Bot command to fetch and display active streams
@bot.command()
async def streams(ctx):
    game_id = "512990"  # This is for the Bleeding Edge category. change it to whatever category you want
    client_id = "CLIENTIDHERE" # Replace with your twitch client ID
    oauth_token = "OUATHTOKEN" # Replace with your OUATH token

    active_streams = get_active_streams_in_category(game_id, client_id, oauth_token)
    if active_streams:
        for stream in active_streams:
            stream_link = f"https://www.twitch.tv/{stream['user_login']}"
            await ctx.send(f"Title: {stream['title']}\nViewer Count: {stream['viewer_count']}\nStream Link: {stream_link}\n-------------")
    else:
        await ctx.send("No one is streaming Bleeding Edge right now.")

# Replace the TOKEN with your Discord bot token
bot.run('TOKEN')