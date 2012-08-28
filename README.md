ticketmaster
============

Ticketmaster is a [flickr-style ticket server](http://code.flickr.com/blog/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-the-cheap/) implemented with Flask and Redis.

Requirements
------------
* Redis

Usage
-----

### / GET

Returns a list of ticket tapes and their latest ticket id.

```
{
  "ticket_tapes": [
    {
      "Tickets32": 4
    },
    {
      "Tickets64": 16
    }
  ]
}
```

### /:ticket_tape/ POST

Generates a new ticket for `:ticket_tape`.

```
>>> r = requests.post(url)
>>> r.json
{u'ticket_tape': u'Tickets64', u'id': 19}
>>> r = requests.post(url)
>>> r.json
{u'ticket_tape': u'Tickets64', u'id': 20}
```
