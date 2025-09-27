import pytest

from lesson24.logging_config import logger


class TestGetCars:
    @pytest.mark.parametrize("get_cars", [None], indirect=True)
    def test_response_not_empty(self, get_cars, request):
        logger.info(f"\t### PERFORMING {request.node.name} ###")

        response = get_cars
        assert response.status_code == 200, logger.error(f"Error: {response.status_code}, {response.text}")

        assert len(response.json()) > 0, logger.error("There is no data in Database")

    @pytest.mark.parametrize("get_cars", [None], indirect=True)
    def test_response_has_required_features(self, get_cars, request):
        logger.info(f"\t### PERFORMING {request.node.name} ###")

        response = get_cars
        car_features = ['brand', 'year', 'engine_volume', 'price']
        for f in car_features:
            assert f in response.json()[0], logger.error(f"There is no info about feature '{f}'")

    @pytest.mark.parametrize("get_cars", [None], indirect=True)
    def test_car_has_the_correct_info(self, get_cars, request):
        logger.info(f"\t### PERFORMING {request.node.name} ###")

        response = get_cars
        assert response.status_code == 200, f"Error: {response.status_code}, {response.text}"

        expected_info = {
            "brand": "Land Rover",
            "year": 2020,
            "engine_volume": 2.0,
            "price": 55000
        }

        actual_info = None
        brand = "Land Rover"
        for item in response.json():
            if item.get("brand") == brand:
                actual_info = item
                break
        assert actual_info is not None, logger.error(f"Car with brand '{brand}' was not found in the response")
        assert actual_info == expected_info, logger.error(
            f"The requested car brand '{brand}' info differs from the expected")

    # TEST GET CARS WITH EXTRA PARAMETERS IN HEADER

    params = {'sort_by': 'price'}

    @pytest.mark.parametrize("get_cars", [[k, v] for k, v in params.items()], indirect=True)
    def test_get_cars_with_sort_by_params(self, get_cars, request):
        logger.info(f"\t### PERFORMING {request.node.name} ###")
        ## RETRIEVING CARS ##
        response = get_cars  # unpacking from the gotten tuple (passed from yield)
        assert response.status_code == 200, logger.error(f"Error: {response.status_code}, {response.text}")
        assert len(response.json()) > 1, logger.error("Response has less than 2 cars to check sorting.")

        price_first_sorted = response.json()[0].get('price')
        price_last_sorted = response.json()[-1].get('price')

        assert price_first_sorted <= price_last_sorted, \
            logger.error(f" {price_first_sorted} >= {price_last_sorted}")

    params = {'limit': 5}

    @pytest.mark.parametrize("get_cars", [[k, v] for k, v in params.items()], indirect=True)
    def test_get_cars_with_limit_params(self, get_cars, request):
        logger.info(f"\t### PERFORMING {request.node.name} ###")
        ## RETRIEVING CARS ##
        logger.info(f"\t### PERFORMING {request.node.name} ###")
        response = get_cars  # unpacking from the gotten tuple (passed from yield)
        assert response.status_code == 200, logger.error(f"Error: {response.status_code}, {response.text}")

        response_length = len(response.json())
        assert response_length <= 5, logger.error(f"The output length is more than 5: {response_length}")

    invalid_params = {'sort_by': 'invalid_field'}

    @pytest.mark.parametrize("get_cars", [[k, v] for k, v in invalid_params.items()], indirect=True)
    def test_get_cars_with_invalid_params(self, get_cars):
        response = get_cars
        assert response.status_code == 400, logger.error(f"Expected error code 400, got {response.status_code}")
