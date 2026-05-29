from aiohttp import web
import asyncio

async def keep_alive():
    app = web.Application()
    app.router.add_get('/', lambda r: web.Response(text="Bot is alive"))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
