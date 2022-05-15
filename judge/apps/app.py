"""
The app module. Defines template parent class for all apps.
"""

from functools import reduce


class App():
    """
    The parent class for all apps. All apps should have a methods method
    decorated by @subscribe_methods, and add other app methods with
    decorator @methods.add_method.
    """
    def __init__(self, _raw_img):
        self._raw_img = _raw_img

    def __call__(self):
        """
        Run the app.

        @return True if passed
        """
        return reduce(lambda res, mtd: res and mtd(self,
                                    type(self)._ELEMENT_IMAGE(self._raw_img)),
                      [ True ] + self.methods)

