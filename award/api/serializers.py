from rest_framework import serializers
from award.models import AwardPost



class AwardPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = AwardPost
        fields = ['title','body','image','date_updated']