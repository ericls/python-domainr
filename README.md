python-domainr
==============

python wrapper for domainr

###NOTE:

1. this tool uses Domainr's free API
2. the accuracy of availavbility is pretty low for some TLDs
3. In September 2014, you'll need an API key to use Domainr's API. 


###Usage:
    

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

... ...or specify a TLD list:

    >>> name = 'foo'
    >>> tlds = ['com', 'net', 'gift', 'club']
    >>> domainr.search_tld(name, tlds)
    >>> ...(omitted)
