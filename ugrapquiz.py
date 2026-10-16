import pandas as pd

df = pd.read_json('/home/sixten/Programmering/Dataset/UGdataset.json')

artist=df.sample().iloc[0]
answr=artist['stage_name']

ledtradar = [
    f"Hen är {artist['age']} år gammal",
    f"De kommer ifrån {artist['origin']}",
    f"De heter {artist['real_name']}",
    f"Deras största projekt är {artist['biggest_project']}"
]

print("hej, här är mitt gissningsspel\n")

vunnit=False

for i, ledtrad in enumerate(ledtradar, start=1):
    print(f"\n{ledtrad}")
    gissning=input("vem är det?: ")

    if gissning.strip().lower()==answr.lower():
        print("\nwow rätt")
        vunnit=True
        break
    elif i < len(ledtradar):
        print("fel, här får du en till ledtråd\n")

if not vunnit:
    print(f"lol du suger b, rätt svar var {answr}")
