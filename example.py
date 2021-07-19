from scraper import Opggtrack

tracker = Opggtrack("Guamss", "euw")
print(f"rank : {tracker.get_ranksolo()} | Classé Solo/Duo")
print(f"rank : {tracker.get_rankflex()} | Flex 5:5")
print(f"winrate : {tracker.get_winratio()}")
print(f"kda ratio : {tracker.get_kdaratio()}")
