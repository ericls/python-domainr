# -*- coding: utf-8 -*-

"""
domainr.py is a simple tool to check domain availability

NOTE:
    1. this tool uses Domainr's free API
    2. the accuracy of availavbility is pretty low for some TLDs
    3. In September 2014, you'll need an API key to use Domainr's API. 


Usage:
    

    >>> import domainr
    >>> a = domainr.domain('foo.com')
    >>> a.available
    >>> False


... or search available domain names with same TLD:

    
    >>> name_list = ['foo', 'bar', 'presume-this-is-available']
    >>> domainr.search_name(name_list, 'com')
    >>> presume-this-is-available.com # printed
    >>> ['presume-this-is-available.com'] # returned


... or search available domain names through a domain name list:


    >>> domain_list = ['an-available-domain.com', 'taken-domain.cc']
    >>> domainr.bulk_available(domain_list)
    >>> an-available-domain.com # printed
    >>> ['an-available-domain.com'] # returned


... or same name with diffrent TlDs


    >>> name = 'foo'
    >>> domainr.search_tld(name)
    >>> ...(omitted)

    or specify a TLD list:

    >>> name = 'foo'
    >>> tlds = ['com', 'net', 'gift', 'club']
    >>> domainr.search_tld(name, tlds)
    >>> ...(omitted)
"""

import requests

COMMON_TLD = ['com', 'net', 'org']


class domain(object):

    def __init__(self, name):
        self.name = name
        self.d_info = None
        self.d_available = None

    def _info(self):
        if not self.d_info:
            d = requests.get('https://domai.nr/api/json/info?q=%s' % self.name)
            self.d_info = d.json()
        return self.d_info

    def _available(self):
        if not self.d_available:
            try:
                a = self.info['availability'] == 'available'
            except:
                raise Exception('can\'t  retrieve information for domain %s' % self.name)
            self.d_available = a
        return self.d_available

    def __repr__(self):
        return '<domain: %s>' % self.name

    info = property(_info)
    available = property(_available)


def formalize(tld):
    if tld.startswith('.'):
        return tld
    else:
        return '.%s' % tld


def is_available(name):
    d = domain(name)
    try:
        return d.available
    except:
        return False


def bulk_available(domain_list):
    available_domain = []
    for d in domain_list:
        if is_available(d):
            print d
            available_domain.append(d)
    return available_domain


def search_name(name_list, tld):
    tld = formalize(tld)
    domain_list = ['%s%s' % (n,tld) for n in name_list]
    return bulk_available(domain_list)


def search_tld(name, tlds=COMMON_TLD):
    tlds = [formalize(t) for t in tlds]
    domain_list = ['%s%s' % (name,tld) for tld in tlds]
    return bulk_available(domain_list)
