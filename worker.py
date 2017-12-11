    import discord
    import asyncio

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        if message.content == "Hello":
            await client.send_message(message.channel, "World")

    client.run(Mzg5Njk3NjYxODQzODAwMDY0.DQ_Vww.d-7ay5mm6Y_aVW_wXy9MobH77sU)