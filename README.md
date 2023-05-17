### Requirements specification for the Event ticketing service

We want to build a new service which can handle the viewing, booking and reservation
management of tickets for a number of events. The events will be listed at the end of this
document, each event has a limited number of tickets available. An event is defined by a name,
a description and a date and time.

We want users of this API to be able to perform the following operations:
- View a list of all events, and associated event information such as name, date, and
number of tickets available
- Make a reservation for a number of tickets for a given event
- Manage an existing ticket reservation; possible actions are change amount of tickets or  cancel the reservation

A reservation for an amount of tickets for an event cannot exceed the amount of tickets
available, in such cases a helpful error message and code should be returned.

Same as the above, a modification for an existing reservation to increase the amount of tickets
reserved cannot be performed if the amount of tickets available are less than the additional
amount requested. In this case a helpful error message and code should be returned.

Any reservations made through the API should update the available stock of tickets to avoid
double bookings. For example: if an event has 100 tickets available from the start, and 100
reservations for single tickets are made, no more tickets should be available for this event.

Ticket cancellations should return the reserved tickets to the stock.
The API should handle general errors (such as missing input parameters, incorrect format etc)
and give helpful error codes to the API requester, for example in case of input errors or
incorrect/missing parameters.

### Mandatory checklist
- [x] Event list API
- [ ] Reservation API
- [ ] Reservation update API
- [ ] Cancel reservation API
- [ ] Make sure constraints are satisfied

### Additional checklist
- [x] Event create API
- [x] Event fetch API
- [x] Event update API
- [x] Event delete API
- [ ] Docker
- [x] PostgreSQL
- [ ] Tests

### Local setup
- Copy the `.env.template` to `.env` file and update the env vars accordingly


### Create a migration