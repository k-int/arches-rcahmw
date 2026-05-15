# Imports
from django.core.management.base import BaseCommand, CommandError
from arches.app.models.models import Concept


class Command(BaseCommand):

    def handle(self, *arg, **options):

        concepts_to_delete = [
            "d68f53fb-5ba1-484d-b02f-4a6f56b2bf68",
            "ac8a2420-5eef-4a5d-9eb1-48278fbd3fb1",
            "9129cecc-064e-4a41-a0a2-5f7d37dac4ea",
            "a2569404-5739-4f84-8a58-a143606fcb22",
            "eab5bce8-60e0-4ea9-a13b-869a649e2d27",
            "4c494161-d939-4a9a-8ab6-b8e63c5b3945",
            "f917eb4a-4c25-402e-a28c-4df30569c666",
            "b23a570b-e1df-45aa-ab2f-2a82c5a9708b",
            "d8f7e061-cbc0-40a6-bb6c-0cfb9fd33719",
            "60699993-4896-47ee-a6ee-53d5bc3f44d4",
            "86afcc48-2716-4570-b396-76fee46eb5a3",
            "38b0b67b-098b-4025-869b-a9bcee16abe6",
            "71f964af-aae8-475c-a8d3-dde3dcb4ab5d",
            "adf4098c-86d0-4a1c-8ce7-1721654829c9",
            "8b933160-3c80-444f-93d0-70d263d4d139",
            "d8942f77-9ae8-484c-9ff0-7989659acb0a",
            "1b2112c2-9e32-44f1-beb3-33f8f1b9e6e9",
            "5055bd23-452d-40b0-8707-b168af363703",
            "c773950e-8f8f-4fe4-8588-686d4f4d4dc6",
            "724db863-69a3-4a19-8980-fb51eac3a91b",
            "d26382f1-f390-4bd0-a1b4-747a3009a6c2",
            "013faeb6-d829-4742-b10c-061a81ef4e66",
            "6b72d0b4-d76c-4ad8-8ffb-f852278062ca",
            "d9ec99a7-8eb4-4285-a804-6addddf3aace",
            "6c1566fb-2174-4575-bb43-97787e20b037",
            "8ff9ebdd-bab3-4463-970d-5621f97de495",
            "4883918f-9de0-48ab-b740-63ce1f926d23",
            "a945afdd-3299-4ed2-814c-4a0e9613e9f5",
            "285b1396-634f-4b67-9791-c12765c9668b",
            "e3395f77-0ff5-4f62-99f5-40cdadbabb30",
            "96716049-3b30-4651-a2c4-23c9534a3c7e",
            "c7ffb9d1-bced-44c3-b388-7a4b14f3c70a",
            "14890506-c22d-4cc1-b076-78e963588669",
            "bb2d5c8f-827a-42c2-bf13-ca8b476d7229",
            "38c86975-9f11-413a-922f-3bfe610c160e",
            "d2b10382-f7c6-468e-ac40-e8b265b8da1d",
            "fe324f50-b450-42ef-bcef-42856c80d913",
            "550087b5-2362-438c-987c-ea0103bab9a2",
            "4c9675dd-a4cc-4e2f-9570-790f1d78a614",
            "ec9fae97-a149-4c6d-8d8c-e1c2cafa7c7f",
            "e752c7aa-9d41-48a0-9cc7-18e3c0b4f1f9",
            "a9c93d35-2faa-4c38-a6aa-e43dfe5a41b9",
            "7eed94fa-47c1-45d5-9925-390939ff7362",
            "9d0f3609-eee5-495c-9278-0dfea28c505c",
            "a7f5f5d5-c230-468d-b9e3-385d51da9fca",
            "80aabaf1-1a8e-49b4-ac6f-b6592966a90c",
            "a804ae60-dfbf-4296-93a4-068a2254ac5e",
            "ae38febb-20ee-493c-bb25-db5f93796632",
            "356252cc-c7bb-44ce-b335-58495d55df5f",
            "b99e9ba8-589b-43cd-8c91-0885edfb8e8d",
            "6757004c-b107-44a0-bca5-3320d1336a2e",
            "c741c68b-779e-4cfb-8a50-70c2c45f81aa",
            "f4ea3e4c-44c0-4107-994f-1461f7a64d33",
        ]

        Concept.objects.filter(conceptid__in=concepts_to_delete).delete()
