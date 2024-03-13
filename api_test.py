from enum import Enum
import requests
import unittest


# Enum Definition
class HarryPotterHouses(Enum):
    GRYFFINDOR = ("0367baf3-1cb6-4baf-bede-48e17e1cd005", "Gryffindor")
    HUFFLEPUFF = ("85af6295-fd01-4170-a10b-963dd51dce14", "Hufflepuff")
    SLYTHERIN = ("a9704c47-f92e-40a4-8771-ed1899c9b9c1", "Slytherin")
    RAVENCLAW = ("805fd37a-65ae-4fe5-b336-d767b8b7c73a", "Ravenclaw")

    @property
    def id(self):
        return self.value[0]

    @property
    def house_name(self):
        return self.value[1]


# Test Case
class TestHarryPotterHouses(unittest.TestCase):
    def test_simple(self):
        # Making the API Request
        house = HarryPotterHouses.GRYFFINDOR
        response = requests.get(f"https://wizard-world-api.herokuapp.com/Houses/{house.id}")

        # Processing the Response
        data = response.json()

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], house.id)
        self.assertEqual(data['name'], house.house_name)


if __name__ == "__main__":
    unittest.main()

