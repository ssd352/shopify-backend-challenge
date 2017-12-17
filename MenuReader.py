import requests
import json


class Reader:
    pass


class MenuReader(Reader):
    """
    This class sends HTTP request and encloses it in a json object
    """
    FIRST_PAGE = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1"

    @classmethod
    def read_url(cls, url=FIRST_PAGE):
        """

        :param url:str
        :return: json
        """
        r = requests.get(url)
        if r.status_code != 200:
            raise ConnectionError()
        output = json.loads(r.content)
        return output


if __name__ == "__main__":
    output = MenuReader.read_url()
    print(output)
