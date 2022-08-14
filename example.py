import asari.api as asari


def main():
    client = asari.Api(email="qoft", timeout=5)
    while True:
        emails = client.get_emails()
        for _ in emails:
            print(_)


if __name__ == '__main__':
    main()
