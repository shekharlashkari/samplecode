# samplecode
# Setup:-
1. create virtualenv in Python 3.6
2. install requirements.txt
3. run "python manage.py migrate"
4. run "python manage.py runserver"

====================================================================================================================================

# Create API
Method: POST
URL : http://127.0.0.1:8000/create-audio

from-data : 

{
   "audioFileType" : "Song",
   "audioFileMetadata":{
	"name":"Libas",
	"duration":50
    }
}

OR

{
    "audioFileType":"Podcast",
    "audioFileMetadata":{
        "name":"Libas",
        "duration":50,
        "host":"pk",
        "paticipant":["shekhar", "techsolvo", "etc"]   # it's optional or can be blank or can be empty list.
    }
}

OR

{
    "audioFileType":"Audiobook",
    "audioFileMetadata":{
	"title":"Libas",
	"author_of_title":"jai shree mahakal",
	"narrator":"jai shree mahakal",
	"duration":50
    }
}

========================================================================================================================================

# Update API
Method: POST

URL : http://127.0.0.1:8000/Song/<int:audio_file_id>
from-data : 
{
   "audioFileMetadata":{
	"name":"Libas 2.0",
	"duration":500
    }
}

OR

URL : http://127.0.0.1:8000/Podcast/<int:audio_file_id>
from-data : 
{
   "audioFileMetadata":{
        "name":"Libas",
        "duration":50,
        "host":"shekhar",
        "paticipant":["shekhar", "computerbaba", "pk"]   # it's optional or can be blank or can be empty list.
    }
}

OR

URL : http://127.0.0.1:8000/Audiobook/<int:audio_file_id>
from-data : 
{
   "audioFileMetadata":{
	"title":"Libas",
	"author_of_title":"jai shree mahakal",
	"narrator":"django",
	"duration":50
    }
}

========================================================================================================================================

# Get API
Method: GET

URL : http://127.0.0.1:8000/Song/<int:audio_file_id>

OR

URL : http://127.0.0.1:8000/Podcast/<int:audio_file_id>

OR

URL : http://127.0.0.1:8000/Audiobook/<int:audio_file_id>

OR

URL : http://127.0.0.1:8000/Song

OR

URL : http://127.0.0.1:8000/Podcast

OR

URL : http://127.0.0.1:8000/Audiobook

===========================================================================================================================================

# Delete API
Method: DELETE

URL : http://127.0.0.1:8000/Song/<int:audio_file_id>

OR

URL : http://127.0.0.1:8000/Podcast/<int:audio_file_id>

OR

URL : http://127.0.0.1:8000/Audiobook/<int:audio_file_id>

============================================================================================================================================

