import asari.asyncapi as asari
import asyncio


async def main():
    client = asari.AsyncApi(email="qoft", timeout=5)
    while True:
        emails = await client.get_emails()
        for _ in emails:
            print(_)


asyncio.run(main())
