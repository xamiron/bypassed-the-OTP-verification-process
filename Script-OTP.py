def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5000,
                           requestsPerConnection=10000,
                           pipeline=False
                           )

    for number in range(327129,338129):
        engine.queue(target.req, number)


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status != 404:
        table.add(req)