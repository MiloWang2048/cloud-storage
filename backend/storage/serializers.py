from rest_framework import serializers
from storage.models import Identifier, Storage


class CatalogueSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='pk')
    is_file = serializers.ReadOnlyField()
    is_shared = serializers.ReadOnlyField()
    date_modified = serializers.ReadOnlyField()

    name = serializers.CharField(required=False, default='新建文件夹')
    extension = serializers.CharField(required=False)
    size = serializers.ReadOnlyField(source="my_file.size")
    owner = serializers.PrimaryKeyRelatedField(source='owner.nickname', read_only=True)

    class Meta:
        model = Identifier
        fields = (
            'id', 'name', 'is_file', 'is_shared',
            'date_modified', 'extension', 'size', 'owner'
        )


class BreadcrumbsSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='pk')
    name = serializers.ReadOnlyField()

    class Meta:
        model = Identifier
        fields = ('id', 'name')


class StorageSerializer(serializers.ModelSerializer):
    storage_id = serializers.IntegerField(source='id')
    root_folder_id = serializers.PrimaryKeyRelatedField(source='root_identifier', read_only=True)

    class Meta:
        model = Storage
        fields = ('storage_id', 'root_folder_id', 'created_time')
