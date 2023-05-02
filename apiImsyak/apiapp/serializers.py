from rest_framework import serializers

class JadwalSerializer(serializers.Serializer):
    tanggal = serializers.CharField(max_length=50)
    imsak   = serializers.TimeField()
    subuh   = serializers.TimeField()
    terbit  = serializers.TimeField()
    duha    = serializers.TimeField()
    zuhur   = serializers.TimeField()
    ashar   = serializers.TimeField()
    magrib  = serializers.TimeField()
    isya    = serializers.TimeField()
