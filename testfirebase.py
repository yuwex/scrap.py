import aiofirebase
import asyncio



async def main():
    firebase = aiofirebase.FirebaseHTTP("https://scrapyard-49049-default-rtdb.firebaseio.com/")
    await firebase.put(path='newavlue', value='epic!?')
    await firebase.close()



asyncio.run(main())
