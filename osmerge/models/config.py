import yorm
from yorm.types import Float, List, Object, AttributeDictionary


@yorm.attr(minimum=Float)
@yorm.attr(maximum=Float)
class CoordinateRange(AttributeDictionary):
    """Specifies a floating-point range."""

    def __init__(self, minimum, maximum):
        super().__init__()
        self.minimum = minimum
        self.maximum = maximum


@yorm.attr(latitude=CoordinateRange)
@yorm.attr(longitude=CoordinateRange)
class BoundingBox(AttributeDictionary):
    """A GPS bounding box."""

    def __init__(self, latitude, longitude):
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude


@yorm.attr(tags=List.of_type(Object))
class FilterOptions(AttributeDictionary):
    """Collection of rules to include matching polygons."""

    def __init__(self, tags=None):
        super().__init__()
        self.tags = tags or []


@yorm.attr(boundaries=List.of_type(BoundingBox))
@yorm.attr(filters=FilterOptions)
@yorm.sync("osmerge.yml")
class Config:
    """Specifies how to limited the location and types of polygons."""

    def __init__(self):
        self.boundaries = []
        self.filters = FilterOptions()

    @classmethod
    def generate_example(cls):
        """Create an example configuration to be manually edited."""
        config = cls()

        config.boundaries = [
            BoundingBox(
                CoordinateRange(42.882669706849875, 43.03002974711799),
                CoordinateRange(-85.75284790217363, -85.5676630879733),
            ),
        ]
        config.filters.tags = [
            dict(leasure='park'),
        ]

        return config
