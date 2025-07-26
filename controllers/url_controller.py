from models.UrlMap import UrlMap
from utils.hash_url import urlHasher

urlMap = UrlMap()


def createShortening(url: str) -> str:
    try:
        urlHash = urlHasher(url)
        urlMap.addUrl(url, urlHash)
        return urlHash
    except Exception as Error:
        print("Could Not Create Shortening:", Error)


def updateShortening(url: str, urlHash: str) -> None:
    try:
        urlMap.updateUrl(url, urlHash)
    except Exception as Error:
        print("Could Not Update Shortening:", Error)


def deleteShortening(urlHash: str) -> None:
    try:
        urlMap.removeUrl(urlHash)
    except Exception as Error:
        print("Could Not Delete Shortening:", Error)


def getUrlMap() -> dict:
    try:
        return urlMap.getMap()
    except Exception as Error:
        print("Could Not Get Shortening Map:", Error)


def getUrl(urlHash: str) -> str:
    try:
        return urlMap.getUrl(urlHash)
    except Exception as Error:
        print("Could Not Get Shortened URL With Hash:", Error)


def getCurrentUrls() -> int:
    try:
        return urlMap.getActiveURLS()
    except Exception as Error:
        print("Could Not Get Count Of Active URLS:", Error)
