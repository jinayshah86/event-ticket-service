# Event ticketing service

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
- [x] Reservation API
- [x] Reservation update API
- [x] Cancel reservation API
- [x] Make sure constraints are satisfied

### Additional checklist
- [x] Event create API
- [x] Event fetch API
- [x] Event update API
- [x] Event delete API
- [x] Docker
- [x] PostgreSQL

### Local setup
- Copy the `.env.template` to `.env` file and update the env vars accordingly
- Start docker containers
  - ```shell
    docker-compose up web
    ```
- Stop docker containers
  - ```shell
    docker-compose down
    ```
- Check application logs
  - ```shell
    docker-compose logs web
    ```

### Create a migration
- Create a python file in `models` folder and create a model there.
- Make sure that model is used somewhere in the application
- Generate migration file by replacing the `{migrtion-title}` with some meaningful migration title.
  - ```shell
    docker-compose run web flask db revision --autogenerate -m "{migration-title}"
    ```

### Load initial events
Make sure curl is installed and docker containers are running
  ```shell
  sh ./inital_data.sh
  ```

### APIs
- Events
  - Create event
    - Successful request:
      ```shell
        curl --request POST \
          --url http://localhost:5000/events/ \
          --header 'Content-Type: application/json' \
          --data '{
            "name": "Rocket to Mars",
            "description": "I'\''m nobody'\''s taxi service; I'\''m not gonna be there to catch you every time you feel like jumping out of a spaceship. I'\''m the Doctor, I'\''m worse than everyone'\''s aunt. *catches himself* And that is not how I'\''m introducing myself.",
            "date": "2047-10-21T09:00:00Z",
            "availability": 0
        }'
      ```
      - Response (`201`)
        ```json
        {
            "availability": 0,
            "created_at": "2023-05-17T16:02:57.040846",
            "updated_at": "2023-05-17T16:02:57.040846",
            "description": "I'm nobody's taxi service; I'm not gonna be there to catch you every time you feel like jumping out of a spaceship. I'm the Doctor, I'm worse than everyone's aunt. *catches himself* And that is not how I'm introducing myself.",
            "name": "Rocket to Mars",
            "date": "2047-10-21T09:00:00+00:00",
            "id": "4b029817-f723-4695-9281-ec126747cba2"
        }
        ```
    - Malformed request:
      ```shell
      curl --request POST \
        --url http://localhost:5000/events/ \
        --header 'Content-Type: application/json' \
        --data '{
          "name": "Rocket to Mars",
          "description": "I'\''m nobody'\''s taxi service; I'\''m not gonna be there to catch you every time you feel like jumping out of a spaceship. I'\''m the Doctor, I'\''m worse than everyone'\''s aunt. *catches himself* And that is not how I'\''m introducing myself.",
          "date": "2047-10-21T09:00:00Z"
      }'
      ```
      - Response (`422`)
      ```json
      {
          "availability": [
              "Missing data for required field."
          ]
      }
      ```
  - Get event
    - Successful request:
      ```shell
        curl --request GET \
        --url http://localhost:5000/events/4b029817-f723-4695-9281-ec126747cba2
      ```
      - Response (`200`)
        ```json
        {
	        "description": "I'm nobody's taxi service; I'm not gonna be there to catch you every time you feel like jumping out of a spaceship. I'm the Doctor, I'm worse than everyone's aunt. *catches himself* And that is not how I'm introducing myself.",
	        "name": "Rocket to Mars",
	        "availability": 0,
            "date": "2047-10-21T09:00:00+00:00",
            "id": "4b029817-f723-4695-9281-ec126747cba2",
	        "created_at": "2023-05-17T16:02:57.040846",
	        "updated_at": "2023-05-17T16:02:57.040846"
        }
        ```
    - Event does not exist:
      ```shell
      curl --request GET \
      --url http://localhost:5000/events/4b029817-f723-4695-9281-ec126747cba1
      ```
      - Response (`422`)
      ```json
      {
        "message": "Event with event id: 4b029817-f723-4695-9281-ec126747cba1 doesn't exist."
      }
      ```
  - Get all events
    - Successful request:
      ```shell
      curl --request GET \
      --url http://localhost:5000/events/
      ```
      - Response (`200`):
      ```json
      [
          {
              "description": "I'm nobody's taxi service; I'm not gonna be there to catch you every time you feel like jumping out of a spaceship. I'm the Doctor, I'm worse than everyone's aunt. *catches himself* And that is not how I'm introducing myself.",
              "name": "Rocket to Mars",
              "availability": 0,
              "date": "2047-10-21T09:00:00+00:00",
              "id": "4b029817-f723-4695-9281-ec126747cba2",
              "created_at": "2023-05-17T16:02:57.040846",
              "updated_at": "2023-05-17T16:02:57.040846"
          }
      ]
      ```
  - Update event
    - Successful request:
      ```shell
      curl --request PATCH \
      --url http://localhost:5000/events/4b029817-f723-4695-9281-ec126747cba2 \
      --header 'Content-Type: application/json' \
      --data '{
      "name": "Rocket to Mars!"
      }'
      ```
      - Response (`200`):
      ```json
      {
        "description": "I'm nobody's taxi service; I'm not gonna be there to catch you every time you feel like jumping out of a spaceship. I'm the Doctor, I'm worse than everyone's aunt. *catches himself* And that is not how I'm introducing myself.",
        "name": "Rocket to Mars!",
        "availability": 0,
        "date": "2047-10-21T09:00:00+00:00",
        "id": "4b029817-f723-4695-9281-ec126747cba2",
        "created_at": "2023-05-17T16:02:57.040846",
        "updated_at": "2023-05-17T16:02:57.040846"
      }
      ```
    - Invalid request:
      ```shell
      curl --request PATCH \
        --url http://localhost:5000/events/4b029817-f723-4695-9281-ec126747cba2 \
        --header 'Content-Type: application/json' \
        --data '{
          "availability": 10
      }'
      ```
      - Response (`422`):
      ```json
      {
          "availability": [
              "Unknown field."
          ]
      }
      ```
  - Delete event
    - Successful request:
      ```shell
      curl --request DELETE \
      --url http://localhost:5000/events/7eb194b4-1574-4ec4-9627-38d20748bd30
      ```
      - Response (`204`)
    - Event does not exist
      - Same as the one in get event
- Reservations
  - Create reservation
    - Successful request:
      ```shell
      curl --request POST \
      --url http://localhost:5000/reservations/ \
      --header 'Content-Type: application/json' \
      --data '{
    	"event_id": "6c00a5d6-0ed3-4a23-b6e6-d1eb056cfbd1",
    	"no_of_tickets": 1
      }'
      ```
      - Response (`201`):
        ```json
         {
             "event_id": "6c00a5d6-0ed3-4a23-b6e6-d1eb056cfbd1",
             "updated_at": "2023-05-17T16:36:32.544453",
             "cancelled": false,
             "id": "2c526fa4-897d-4fbc-80e9-974bc12c29b0",
             "no_of_tickets": 1,
             "created_at": "2023-05-17T16:36:32.544453"
         }
        ```
    - Reservation does not exist:
      ```shell
      curl --request POST \
      --url http://localhost:5000/reservations/ \
      --header 'Content-Type: application/json' \
      --data '{
        "event_id": "7eb194b4-1574-4ec4-9627-38d20748bd30",
        "no_of_tickets": 1
      }'
      ```
      - Response (`404`)
        ```json
        {
          "message": "Event with event id: 7eb194b4-1574-4ec4-9627-38d20748bd30 doesn't exist."
        }
        ```
    - Insufficient tickets request:
      ```shell
      curl --request POST \
        --url http://localhost:5000/reservations/ \
        --header 'Content-Type: application/json' \
        --data '{
          "event_id": "cbcaf3e2-4872-4b29-a4c9-4ffbe43c0e47",
          "no_of_tickets": 1
      }'
      ```
      - Response (`400`):
        ```json
        {
	        "error": "Requested number of tickets are not available."
        }
        ```
  - Get reservation
    - Successful request:
      ```shell
      curl --request GET \
      --url http://localhost:5000/reservations/
      ```
      - Response (`200`)
        ```json
        {
            "event_id": "6c00a5d6-0ed3-4a23-b6e6-d1eb056cfbd1",
            "updated_at": "2023-05-17T16:36:32.544453",
            "cancelled": false,
            "id": "2c526fa4-897d-4fbc-80e9-974bc12c29b0",
            "no_of_tickets": 1,
            "created_at": "2023-05-17T16:36:32.544453"
        }
        ```
    - Reservation does not exist
      ```shell
      curl --request GET \
      --url http://localhost:5000/reservations/6c00a5d6-0ed3-4a23-b6e6-d1eb056cfbd1
      ```
      - Response (`404`)
        ```json
          {
              "message": "Reservation with reservation id: 6c00a5d6-0ed3-4a23-b6e6-d1eb056cfbd1 doesn't exist."
          }
        ```
  - Get all reservations
    - Successful request:
      ```shell
      curl --request GET \
      --url http://localhost:5000/reservations/
      ```
      - Response (`200`):
        ```json
        [
	        {
        		"created_at": "2023-05-17T16:36:32.544453",
		        "no_of_tickets": 1,
		        "id": "2c526fa4-897d-4fbc-80e9-974bc12c29b0",
		        "event_id": "6c00a5d6-0ed3-4a23-b6e6-d1eb056cfbd1",
		        "cancelled": false,
		        "updated_at": "2023-05-17T16:36:32.544453"
	        },
	        {
        		"created_at": "2023-05-17T16:40:35.280123",
		        "no_of_tickets": 1,
		        "id": "2b771ade-6e86-49e6-8603-c729c5c37709",
		        "event_id": "6c00a5d6-0ed3-4a23-b6e6-d1eb056cfbd1",
		        "cancelled": false,
		        "updated_at": "2023-05-17T16:40:35.280123"
	        }
        ]
        ```
  - Update reservation
    - Successful request:
      ```shell
      curl --request PATCH \
        --url http://localhost:5000/reservations/2b771ade-6e86-49e6-8603-c729c5c37709 \
        --header 'Content-Type: application/json' \
        --data '{
	      "no_of_tickets": 198
      }'
      ```
      - Response (`200`)
        ```json
         {
      	   "created_at": "2023-05-17T16:40:35.280123",
	       "no_of_tickets": 198,
	       "id": "2b771ade-6e86-49e6-8603-c729c5c37709",
	       "event_id": "6c00a5d6-0ed3-4a23-b6e6-d1eb056cfbd1",
	       "cancelled": false,
	       "updated_at": "2023-05-17T16:40:35.280123"
         }
         ```
    - Insufficient tickets request
      ```shell
      curl --request PATCH \
        --url http://localhost:5000/reservations/2b771ade-6e86-49e6-8603-c729c5c37709 \
        --header 'Content-Type: application/json' \
        --data '{
      	"no_of_tickets": 202
      }'
      ```
      - Response (`400`):
        ```json
        {
      	  "error": "Requested number of tickets are not available."
        }
        ```
    - Invalid request
      ```shell
       curl --request PATCH \
         --url http://localhost:5000/reservations/2b771ade-6e86-49e6-8603-c729c5c37709 \
         --header 'Content-Type: application/json' \
         --data '{
       	"cancelled": false
       }'
       ```
       - Response (`422`):
         ```json
         {
         	"cancelled": [
         		"Unknown field."
         	]
         }
         ```
    - Reservation does not exist
      ```shell
      curl --request PATCH \
        --url http://localhost:5000/reservations/7eb194b4-1574-4ec4-9627-38d20748bd30 \
        --header 'Content-Type: application/json' \
        --data '{
	      "no_of_tickets": 1
      }'
      ```
      - Response (`404`):
        ```json
        {
           "message": "Event with event id: 7eb194b4-1574-4ec4-9627-38d20748bd30 doesn't exist."
        }
        ```
  - Cancel reservation
    - Successful request
      ```shell
      curl --request DELETE \
        --url http://localhost:5000/reservations/2b771ade-6e86-49e6-8603-c729c5c37709
      ```
      - Response (`204`)
    - Reservation does not exist
      ```shell
      curl --request DELETE \
      --url http://localhost:5000/reservations/20f15f85-2b3a-415d-b7c8-fde8faacb7d4
      ```
      - Response (`404`):
        ```json
        {
            "message": "Reservation with reservation id: 20f15f85-2b3a-415d-b7c8-fde8faacb7d4 doesn't exist."
        }
        ```
