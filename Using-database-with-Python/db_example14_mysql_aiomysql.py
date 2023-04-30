#!/usr/bin/env python3

# Install the following before running the code.
# pip install asyncio
# pip install aiomysql

import asyncio
import aiomysql

loop = asyncio.get_event_loop()

async def connect_db():
    connection = await aiomysql.connect(
        host = "<fill>",
        user = "<fill>",
        password = "<fill>",
        db = "<fill>"
        loop = loop
    )

    cursor = await connection.cursor()
    await cursor.execute("select @@version")
    version = await cursor.fetchone()

    if version:
        print('Running version: ', version)
    else:
        print('Not connected.')

    await cursor.close()

    cursor = await connection.cursor()
    await cursor.execute("select * from country limit 10")

    row = await cursor.fetchone()

    while row:
        print(str(row[1]) + '  ' + str(row[3]))
        row = await cursor.fetchone()

    await cursor.close()

    connection.close()

loop.run_until_complete(connect_db())
