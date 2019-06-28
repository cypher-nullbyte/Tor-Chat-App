import io
import pycurl
import urllib.parse


class TorQuery:
    def __init__(self, domain, socks_port):
        """
        :param domain: the domain you will want to query
        :param socks_port: the port where tor controller is listening
        """
        self.domain = domain
        self.socks_port = int(socks_port)

    def query(self, route=''):
        """
        Uses pycurl to fetch a site using the proxy on the socks_port
        :param url: the string url
        :param route: the route in the website
        :return: the website string
        """
        if route:
            if route[0] == '/':
                domain = self.domain + route
            else:
                domain = self.domain + '/' + route
        else:
            domain = self.domain

        domain = urllib.parse.quote(domain)

        output = io.BytesIO()

        query = pycurl.Curl()
        query.setopt(pycurl.URL, domain)
        query.setopt(pycurl.PROXY, 'localhost')
        query.setopt(pycurl.PROXYPORT, self.socks_port)
        query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
        query.setopt(pycurl.WRITEFUNCTION, output.write)

        try:
            query.perform()
            return str(output.getvalue())[2:-1]
        except pycurl.error as exc:
            return "Unable to reach %s (%s)" % (domain, exc)
