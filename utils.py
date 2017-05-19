from wit import Wit

ACCESS_TOKEN = '5KDHBPFZJFD7NHL2KDTXDBYTMOSHEODV'

client = Wit(access_token=ACCESS_TOKEN)

txt = "I want sports news"

respond = client.message(message=txt)

print(respond)
