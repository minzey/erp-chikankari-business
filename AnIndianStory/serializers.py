from django.core import serializers

from AnIndianStory.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['challanid', 'process', 'product', 'karigar', 'size', 'qty', 'assignmentdate']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['product'] = instance.product.prodid
        rep['karigar'] = instance.karigar.name
        return rep