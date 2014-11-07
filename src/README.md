# High level: What to edit

Edit **receiver.py**

# Structure

All p2p communications should be sent as a POST request,
encoded in a JSON object, to the following URL:

    http://localhost:port/mailbox

If the request is not a POST request, and/or not a properly
formatted JSON object, server will return an error.

# Simulating requests

Recommend downloading "Postman" chrome app.

Simple test:

    curl -H "Content-Type: application/json" -d '{"somedata":"miles"}' http://localhost:8080/mailbox


# Architecture

Similar to peerster.

## Overview

**Groupthink**:
Global context object. Analagous to 'Peerster' object.

**Server**:
Bottle.py server

**main**:
Main loop

**receiver**:
Responsible for handling incoming messages.

## Events!! Cool, Miles!

Any object can **register** an **event** with the
Groupthink object, and any object can
register a **handler** with the Groupthink object.

For example, the server.py file registers an event
`/mailbox` and calls it when the mailbox URL receives
a POST request. Separately, the receiver.py file registers
a handler to event '/mailbox' which is called whenever the
event happens (and server calls groupthink.process_event('/mailbox', ...))

e.g.

    # In class that will create the event
    groupthink.register_event('/mailbox')

    # In class that wants to register a handler:
    def listener(somearg=None):
        print somearg

    groupthink.register_handler('/mailbox', listener)

    # When event happens:
    groupthink.process('/mailbox', somearg=someval)

Note that the callback function, if it requires argument `somearg`,
will cause an error if `groupthink.process_event()` does not include
it as an argument, e.g. `groupthink.process_event('event_name', somearg=someval)`
would work, but `groupthink.process_event('event_name')` would fail.

## Example of event chain

- Run the server (see readme in above directory).
- Run following command in separate terminal window:

    curl -H "Content-Type: application/json" -d '{"somedata":"miles"}' http://localhost:8080/mailbox

- In your terminal window serving the website, you should see the output of the message.

What happened here?

**At Bootup:**

1. Main loop created groupthink object, server object, receiver object

2. Objects attached to each other like SERVER <-> GROUPTHINK <-> RECEIVER

3. Server object registered event '/mailbox' with `groupthink.register_event('/mailbox')`

4. Receiver object registered handler for event '/mailbox' and callback `message_received`

**When user makes request:**

1. User requested /mailbox (POST request with proper JSON object in body)

2. Request went to bottle.py route handler in http_server.py

3. Route handler called `groupthink.process_event('/mailbox')`

4. Groupthink called all callbacks registered to event `/mailbox`, which was
simply the one that the receiver object registered.
