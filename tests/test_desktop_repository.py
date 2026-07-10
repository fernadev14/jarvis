from jarvis.platforms.discovery.factory import DiscoveryFactory


repo = DiscoveryFactory.create()

print()

print(len(repo.applications))

print()

for app in repo.applications[:30]:

    print(app)
