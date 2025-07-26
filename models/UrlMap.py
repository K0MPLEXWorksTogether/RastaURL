from utils.hash_url import urlHasher


class UrlMap:
    def __init__(self) -> None:
        self.map = dict()
        self.currentUrls = 0

    def addUrl(self, url: str, urlHash: str) -> None:
        self.map[urlHash] = url
        self.currentUrls += 1

    def getMap(self) -> dict:
        return self.map

    def removeUrl(self, urlHash: str) -> None:
        self.map.pop(urlHash, None)
        self.currentUrls -= 1

    def updateUrl(self, url: str, urlHash: str) -> None:
        self.removeUrl(urlHash)
        self.addUrl(url, urlHasher(url))

    def getUrl(self, urlHash: str) -> str:
        return self.map[urlHash]

    def getActiveURLS() -> int:
        return self.currentUrls


def main():
    sampleMap = UrlMap()

    # Creation
    sampleMap.addUrl(
        "https://www.example.com/", urlHash=urlHasher("https://www.example.com/")
    )

    # Reading
    print(sampleMap.getMap())

    # Updating
    sampleMap.updateUrl(
        "https://www.example.com/", urlHash=urlHasher("https://www.example.com/")
    )
    print(sampleMap.getMap())

    # Removal
    sampleMap.removeUrl(urlHasher("https://www.example.com/"))
    print(sampleMap.getMap())
