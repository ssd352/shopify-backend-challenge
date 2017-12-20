import requests
import json


class Reader:
    pass


class MenuReader(Reader):
    """
    This class sends HTTP request and encloses it in a json object
    """
    page = 1
    URL = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id={id}&page={page}"

    def __init__(self, challenge_id):
        self.page = 1
        self.challenge_id = challenge_id
        output = MenuReader.read_url(MenuReader.URL.format(id=self.challenge_id, page=1))
        self.total = output["pagination"]["total"]
        # print(output, self.total)

    def has_next(self):
        return self.page <= self.total

    def get_next(self):
        next_page = MenuReader.read_url(MenuReader.URL.format(id=self.challenge_id, page=self.page))
        self.page += 1
        return next_page

    @staticmethod
    def read_url(url):
        """

        :param url:str
        :return: json
        """
        r = requests.get(url)
        if r.status_code != 200:
            raise ConnectionError()
        output = json.loads(r.content)
        return output


# Unit Test
if __name__ == "__main__":
    mr = MenuReader()
    while mr.has_next():
        print(mr.get_next())
    # output = mr.read_url()
    # print(output)
