import requests
import math

# Clips a number to the specified minimum and maximum values.
def clip(n, minValue, maxValue):
    return min(max(n, minValue), maxValue)

# Calculates width and height of the map in pixels at a specific zoom level from -180 degrees to 180 degrees.
def getMapSize(zoom, tileSize):
    return math.ceil(tileSize * pow(2, zoom))

# Converts a point from latitude/longitude WGS-84 coordinates (in degrees) into pixel XY coordinates at a specified level of detail.
def positionToGlobalPixel(position, zoom, tileSize):
    MinLatitude = -85.05112878
    MaxLatitude = 85.05112878
    MinLongitude = -180
    MaxLongitude = 180
    latitude = clip(position[1], MinLatitude, MaxLatitude)
    longitude = clip(position[0], MinLongitude, MaxLongitude)

    x = (longitude + 180) / 360;
    sinLatitude = math.sin(latitude * math.pi / 180);
    y = 0.5 - math.log((1 + sinLatitude) / (1 - sinLatitude)) / (4 * math.pi)

    mapSize = getMapSize(zoom, tileSize);

    return [clip(x * mapSize + 0.5, 0, mapSize - 1),clip(y * mapSize + 0.5, 0, mapSize - 1)]

# Converts pixel XY coordinates into tile XY coordinates of the tile containing the specified pixel.
def globalPixelToTileXY(pixel, tileSize):
    tileX = (int)(pixel[0] / tileSize)
    tileY = (int)(pixel[1] / tileSize)
    return [tileX, tileY]
    
def generateTileUrl(longitude,latitude, zoom_level=15, tileSize=256, historical_date=None):
    # Azure Maps API endpoint for satellite imagery
    _endpoint="https://atlas.microsoft.com/map/imagery/png"

    # Azure Maps API key
    _api_key = "sUmIKKtgz-lVkZI6P5paolNRhvP6yqRY0weju-g3am0"

    # Zoom level for satellite imagery
    # zoom_level = 15
    # tileSize = 256
    # Coordinates of the region of interest (latitude, longitude)
    # latitude = 3.4653
    # longitude = -62.2159
    position=[longitude, latitude]

    # Date and time of the historical imagery (YYYY-MM-DDTHH:mm:ss format)
    # historical_date = "2022-01-01T00:00:00"

    # # Image size
    # image_width = 1024
    # image_height = 1024

    # Make the GET request to Azure Maps API

    # Construct the request URL
    if type(zoom_level)==int:
        # Tile System math for the Spherical Mercator projection coordinate system (EPSG:3857)
        pixelXY=positionToGlobalPixel(position, zoom_level, tileSize)
        [tileX,tileY]=globalPixelToTileXY(pixelXY, tileSize)
        url = f"{_endpoint}?subscription-key={_api_key}&style=satellite&zoom={zoom_level}&x={tileX}&y={tileY}"
        # if historical_date is not None:
        #     url += f"&dateTime={historical_date}"
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"historical_satellite_image_{zoom_level}.png", "wb") as f:
                f.write(response.content)
            print(f"Historical satellite image retrieved successfully. Zoom level={zoom_level}")
        else:
            print("Error:", response.text)

    else:
        for curr_zoom_level in range(zoom_level[0], zoom_level[1]+1):
            # Tile System math for the Spherical Mercator projection coordinate system (EPSG:3857)
            pixelXY=positionToGlobalPixel(position, curr_zoom_level, tileSize)
            [tileX,tileY]=globalPixelToTileXY(pixelXY, tileSize)
            url = f"{_endpoint}?subscription-key={_api_key}&style=satellite&zoom={curr_zoom_level}&x={tileX}&y={tileY}"
            # if historical_date is not None:
            #     url += f"&dateTime={historical_date}"
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"historical_satellite_image_{curr_zoom_level}.png", "wb") as f:
                    f.write(response.content)
                print(f"Historical satellite image retrieved successfully. Zoom level={curr_zoom_level}")
            else:
                print("Error:", response.text)
