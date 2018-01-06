# -*- coding: utf-8

import fire

def get_robots_url(base_url):
    from urllib.parse import urlparse, urlunparse

    parsed = urlparse(base_url)
    parts = (parsed.scheme, parsed.netloc, 'robots.txt', None, None, None)
    return urlunparse(parts)


def can_fetch(url, robots_url, useragent):
    from urllib.robotparser import RobotFileParser

    parser = RobotFileParser()
    parser.set_url(robots_url)
    parser.read()
    return parser.can_fetch(useragent, url)


def cli(url, robots_url=None, useragent='*'):
    if not robots_url:
        robots_url = get_robots_url(url)
    if can_fetch(url, robots_url, useragent):
        return 'allow'
    else:
        return 'disallow'


def main():
    fire.Fire(cli)

if __name__ == '__main__':
    main()
