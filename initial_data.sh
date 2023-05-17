curl --request POST \
  --url http://localhost:5000/events/ \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "National Awareness Day",
	"description": "You won'\''t have time for sleeping, soldier, not with all the bed making you'\''ll be doing. Guess again. No, I'\''m Santa Claus! Bender! Ship! Stop bickering or I'\''m going to come back there and change your opinions manually!",
	"date": "2027-03-05T13:00:00Z",
	"availability": 10
}'
curl --request POST \
  --url http://localhost:5000/events/ \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "Universal Entrepreneurship Expo",
	"description": "I suppose I could part with '\''one'\'' and still be feared... Enough about your promiscuous mother, Hermes! We have bigger problems. Ummm...to eBay?",
	"date": "2013-02-21T15:00:00Z",
	"availability": 5
}'
curl --request POST \
  --url http://localhost:5000/events/ \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "Wine festival",
	"description": "All I want is to be a monkey of moderate intelligence who wears a suit... that'\''s why I'\''m transferring to business school! Meh. We'\''ll go deliver this crate like professionals, and then we'\''ll go home.",
	"date": "2024-12-11T14:00:00Z",
	"availability": 1
}'
curl --request POST \
  --url http://localhost:5000/events/ \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "Annual Bicycle Appreciation Day",
	"description": "Yes, if you make it look like an electrical fire. When you do things right, people won'\''t be sure you'\''ve done anything at all. Oh dear! She'\''s stuck in an infinite loop, and he'\''s an idiot! Well, that'\''s love for you",
	"date": "2007-03-01T13:00:00Z",
	"availability": 200
}'
curl --request POST \
  --url http://localhost:5000/events/ \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "Rocket to Mars",
	"description": "I'\''m nobody'\''s taxi service; I'\''m not gonna be there to catch you every time you feel like jumping out of a spaceship. I'\''m the Doctor, I'\''m worse than everyone'\''s aunt. *catches himself* And that is not how I'\''m introducing myself.",
	"date": "2047-10-21T09:00:00Z",
	"availability": 0
}'
