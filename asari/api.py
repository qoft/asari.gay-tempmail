import httpx
import time


class Api:
    def __init__(self, email: str = None, timeout: int = 15) -> None:
        if email is None:
            raise ValueError("Email is required")
        self.client = httpx.Client(
            timeout=timeout,
            headers={"User-Agent": "noratelimit"},
            base_url="https://asari.gay/api/v1/"
        )
        self.email = email if "@" in email else email + "@guilded.lol"

    def get_emails(self):

        if self.email is None:
            raise ValueError("Email is required")

        try:
            req = self.client.get(f"emails/{self.email}")
        except Exception as e:
            raise ValueError("Could not connect to the API") from None

        if req.json()["error"]:
            raise ValueError(req.json()["message"]) from None

        return req.json()["emails"]

    def delete_email(self):
        try:
            req = self.client.delete(f"emails/{self.email}/reset")
        except Exception as e:
            raise ValueError("Could not connect to the API") from None

        if req.json()["error"]:
            raise ValueError(req.json()["message"]) from None
        return True

    def test_email(self):
        try:
            req = self.client.post(f"emails/{self.email}/test")
        except Exception as e:
            raise ValueError("Could not connect to the API") from None

        if req.json()["error"]:
            raise ValueError(req.json()["message"]) from None
        return req.json()

    def wait_for_email(self, _from: str, timeout=5, tries=30):
        if _from is None:
            raise ValueError("_from is required")
        ct = 0
        while True:
            if ct >= tries:
                raise ValueError("Could not find email")
            e = self.get_emails()
            for _ in e:
                if _["from"] == _from:
                    return _
            ct += 1
            time.sleep(timeout)
