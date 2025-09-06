import json


class Config:
    filePath = "./config.json"
    configs=json.load(open(filePath,"r"))

    @staticmethod
    def getCookies():
        cookies = {}
        for cookie in Config.configs["cookies"]:
            cookies[cookie["key"]] = cookie["value"]
        return cookies

    @staticmethod
    def addCookie(cookie):
        cookies=Config.configs["cookies"]
        for key,value in cookie.items():
            updated = False
            for _cookie in cookies:
                if _cookie["key"] == key:
                    _cookie["value"] = value
                    updated = True
            if not updated:
                cookies.append({"key": key, "value": value})

        try:
            with open(Config.filePath,"w",encoding="utf-8") as f:
                json.dump(Config.configs ,f,indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"写入失败:{e}")