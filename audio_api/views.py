from django.http import HttpResponse
from django.http.response import JsonResponse
from .serializer import SongSerializer, PodcastSerializer, AudiobookSerializer
from .models import Song, Podcast, Audiobook
import json
from django.http import QueryDict


def create_audio(request):    
    if request.method == 'POST':
        try:
            audioFileType = request.POST.get('audioFileType')
            data = request.POST.get('audioFileMetadata')
            audioFileMetadata = {}
            try:
                audioFileMetadata = json.loads(data)
            except:
                response = JsonResponse({"message": "Please Provide valid song file metadata."}, status=400)
                return response
            if audioFileType == 'Song':
                serializer = SongSerializer(data=audioFileMetadata)
                if serializer.is_valid():
                    serializer.save()
                    response = JsonResponse({"message": "Data Created"}, status=201)
                    return response
                else:
                    response = JsonResponse({"message": "Please Provide valid song file metadata."}, status=400)
                    return response
            elif audioFileType == 'Podcast':
                if 'paticipant' in audioFileMetadata:
                    if audioFileMetadata['paticipant'] != '':
                        audioFileMetadata['paticipant'] = json.dumps(audioFileMetadata['paticipant'])
                serializer = PodcastSerializer(data=audioFileMetadata)
                if serializer.is_valid():
                    serializer.save()
                    response = JsonResponse({"message": "Data Created"}, status=201)
                    return response
                else:
                    response = JsonResponse({"message": "Please Provide valid song file metadata."}, status=400)
                    return response
            elif audioFileType == 'Audiobook':
                serializer = AudiobookSerializer(data=audioFileMetadata)
                if serializer.is_valid():
                    serializer.save()
                    response = JsonResponse({"message": "Data Created"}, status=201)
                    return response
                else:
                    response = JsonResponse({"message": "Please Provide valid song file metadata."}, status=400)
                    return response
        except Exception as e:
            print(e)
            response = JsonResponse({"message": "Internal Server Error"}, status=500)
            return response
    else:
        response = JsonResponse({"message": "Method Not Allowed"}, status=405)
        return response



def customize_audio(request, audioFileType, audioFileID):    
    if request.method == 'POST':
        try:
            data = request.POST.get('audioFileMetadata')
            audioFileMetadata = {}
            try:
                audioFileMetadata = json.loads(data)
            except:
                response = JsonResponse({"message": "Please Provide valid song file metadata."}, status=400)
                return response
            if audioFileType == 'Song':
                if Song.objects.filter(pk=audioFileID).exists():
                    serializer = SongSerializer(instance=Song.objects.get(pk=audioFileID), data=audioFileMetadata, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        response = JsonResponse({"message": "Data Updated"}, status=204)
                        return response
                    else:
                        response = JsonResponse({"message": "Please Provide valid song file metadata."}, status=400)
                        return response
                else:
                    response = JsonResponse({"message": "file ID does not exists."}, status=404)
                    return response
            elif audioFileType == 'Podcast':
                if Podcast.objects.filter(pk=audioFileID).exists():
                    if 'paticipant' in audioFileMetadata:
                        if audioFileMetadata['paticipant'] != '':
                            audioFileMetadata['paticipant'] = json.dumps(audioFileMetadata['paticipant'])
                    serializer = PodcastSerializer(instance=Podcast.objects.get(pk=audioFileID), data=audioFileMetadata, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        response = JsonResponse({"message": "Data Updated"}, status=204)
                        return response
                    else:
                        response = JsonResponse({"message": "Please Provide valid song file metadata."}, status=400)
                        return response
                else:
                    response = JsonResponse({"message": "file ID does not exists."}, status=404)
                    return response
            elif audioFileType == 'Audiobook':
                if Audiobook.objects.filter(pk=audioFileID).exists():
                    serializer = AudiobookSerializer(instance=Audiobook.objects.get(pk=audioFileID), data=audioFileMetadata, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        response = JsonResponse({"message": "Data Updated"}, status=204)
                        return response
                    else:
                        response = JsonResponse({"message": "Please Provide valid song file metadata."}, status=400)
                        return response
                else:
                    response = JsonResponse({"message": "file ID does not exists."}, status=404)
                    return response
        except Exception as e:
            print(e)
            response = JsonResponse({"message": "Internal Server Error"}, status=500)
            return response
    elif request.method == 'GET':
        try:
            if audioFileType == 'Song':
                if Song.objects.filter(pk=audioFileID).exists():
                    serializer = SongSerializer(Song.objects.get(pk=audioFileID))
                    response = JsonResponse(serializer.data, status=200)
                    return response
                else:
                    response = JsonResponse({"message": "file ID does not exists."}, status=404)
                    return response
            elif audioFileType == 'Podcast':
                if Podcast.objects.filter(pk=audioFileID).exists():
                    serializer = PodcastSerializer(Podcast.objects.get(pk=audioFileID))
                    response = JsonResponse(serializer.data, status=200)
                    return response
                else:
                    response = JsonResponse({"message": "file ID does not exists."}, status=404)
                    return response
            elif audioFileType == 'Audiobook':
                if Audiobook.objects.filter(pk=audioFileID).exists():
                    serializer = AudiobookSerializer(Audiobook.objects.get(pk=audioFileID))
                    response = JsonResponse(serializer.data, status=200)
                    return response
                else:
                    response = JsonResponse({"message": "file ID does not exists."}, status=404)
                    return response
        except Exception as e:
            print(e)
            response = JsonResponse({"message": "Internal Server Error"}, status=500)
            return response
    
    elif request.method == 'DELETE':
        try:
            if audioFileType == 'Song':
                if Song.objects.filter(pk=audioFileID).exists():
                    Song.objects.get(pk=audioFileID).delete()
                    response = JsonResponse({"message": "Audio Deleted"}, status=204)
                    return response
                else:
                    response = JsonResponse({"message": "file ID does not exists."}, status=404)
                    return response
            elif audioFileType == 'Podcast':
                if Podcast.objects.filter(pk=audioFileID).exists():
                    Podcast.objects.get(pk=audioFileID).delete()
                    response = JsonResponse({"message": "Audio Deleted"}, status=204)
                    return response
                else:
                    response = JsonResponse({"message": "file ID does not exists."}, status=404)
                    return response
            elif audioFileType == 'Audiobook':
                if Audiobook.objects.filter(pk=audioFileID).exists():
                    Audiobook.objects.get(pk=audioFileID).delete()
                    response = JsonResponse({"message": "Audio Deleted"}, status=204)
                    return response
                else:
                    response = JsonResponse({"message": "file ID does not exists."}, status=404)
                    return response
        except Exception as e:
            print(e)
            response = JsonResponse({"message": "Internal Server Error"}, status=500)
            return response
    else:
        response = JsonResponse({"message": "Method Not Allowed"}, status=405)
        return response


def get_audio(request, audioFileType):
    if request.method == 'GET':
        try:
            if audioFileType == 'Song':
                song = Song.objects.all()
                serializer = SongSerializer(song, many=True)
                response = JsonResponse(serializer.data, status=200, safe=False)
                return response
            elif audioFileType == 'Podcast':
                podcast = Podcast.objects.all()
                serializer = PodcastSerializer(podcast, many=True)
                response = JsonResponse(serializer.data, status=200, safe=False)
                return response
            elif audioFileType == 'Audiobook':
                audiobook = Audiobook.objects.filter()
                serializer = AudiobookSerializer(audiobook, many=True)
                response = JsonResponse(serializer.data, status=200, safe=False)
                return response
        except Exception as e:
            print(e)
            response = JsonResponse({"message": "Internal Server Error"}, status=500)
            return response
    else:
        response = JsonResponse({"message": "Method Not Allowed"}, status=405)
        return response