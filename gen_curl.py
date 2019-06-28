import io
import pycurl
from stem.util import term


def make_query(url):
    """
    Uses pycurl to fetch a site using the proxy on the socks_port
    :param url: the string url
    :return: the website string
    """

    output = io.BytesIO()

    query = pycurl.Curl()
    query.setopt(pycurl.URL, url)
    query.setopt(pycurl.PROXY, 'localhost')
    query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
    query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
    query.setopt(pycurl.WRITEFUNCTION, output.write)

    try:
        query.perform()
        return output.getvalue()
    except pycurl.error as exc:
        return "Unable to reach %s (%s)" % (url, exc)


SOCKS_PORT = int(input("What is the tor SOCKS_PORT? "))
website = input("What is the website? ")

print(term.format(make_query(website), term.Color.BLUE))
