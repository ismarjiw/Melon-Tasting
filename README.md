For the backend, I chose to use Flask at the Python web framework since it's easy / quick to get started and PSQL as my database management system since it has a long history of community development and stores data in data tables which I prefer to work with.
For the frontend I used HTML/CSS/Tailwind/Flowbite.

My database is named "Melons" and I created 3 tables in PSQL/SQLalchemy: Users, Reservations and Appointments. Users has a many-many relationship with Reservations and Appointments.

Users stores user_id and username. Reservation stores reservation_id, length, date, start time, and end time; it has foreign keys user_id and appointment_id. Appointment stores appointment_id, length, date, start time and end time; it has foreign keys user_id and reservation_id.

The most difficult challenge I came across was formating the datetime.date() object to be comparable to HTML input type date on the "make reservation" form. In addition, when trying to add start time/ end time/ date in search, the search result did not match => could not figure out why as when checking in interactive mode, it yielded the correct return response. As well, when trying to save a reservation, the server was not recognizing that a saved appointment had an associated appointment_id; it would appear as None although checking on psql melons => each appointment had an appointment_id...
Due to these blocks in this webapp, the user cannot properly search for an appointment and view what reservations they would've been able to make.