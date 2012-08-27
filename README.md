ticketmaster
============

Ticketmaster is a flickr-style ticket server implemented with Flask and Redis

Requirements
------------
* Redis

Usage
-----

### / GET

Returns a list of ticket tapes which are in use.

```
{
  "ticket_tapes": [
    "Tickets32",
    "Tickets64",
    "Photos",
    "Accounts",
    "Groups"
  ]
}
```

### /:ticket_tape/ POST

Generates a new ticket for `:ticket_tape`.

```
{
	"ticket_tape": "Tickets64",
	"id": "72157623227190423"
}
```
