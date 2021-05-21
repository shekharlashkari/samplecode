from .models import Song, Podcast, Audiobook
from rest_framework import serializers, fields
import json
import ast

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['id', 'name', 'duration', 'uploaded_time', 'host', 'paticipant']

    def validate_paticipant(self, paticipant):
        print(paticipant)
        if paticipant == '':
            return paticipant
        try:
            paticipant = json.loads(paticipant)
        except:
            raise serializers.ValidationError("this field must be list of string.")
        if isinstance(paticipant, list):
            for index, item in enumerate(paticipant):
                if isinstance(item, str):
                    if 0 < len(item) < 101:
                        pass
                    else:
                        raise serializers.ValidationError("Index {} item is length not valid.".format(index))
                else:
                    raise serializers.ValidationError("Index {} item must be string.".format(index))
            if len(paticipant) < 11:
                return paticipant
            else:
                raise serializers.ValidationError("list of string ength must be less than 11.")
        else:
            raise serializers.ValidationError("this field must be list of string.")

class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = '__all__'