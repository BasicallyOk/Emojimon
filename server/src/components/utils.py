import copy
import json


class Utils:
    def __init__(self):
        pass

    def json_encoder(self, obj):
        """
        Handles encoding and loading the state of the emojimon into a JSON file
        """
        # Shallow copy.
        data = copy.copy(self.__dict__)
        data = self.dict_attr_traversal(data)
        with open(f"{obj.return_id()}.json") as f:
            json.dump(data, f)

    def dict_attr_traversal(self, data: dict):
        """
        Recursively extract the data of the emojimon along with any objects belonging to the emojimon object
        Parameters:
                data (dict): the __dict__ attribute of the object, specifically the Emojimon or the objects related to
                it.
        """
        for key in data.keys():
            val = data[key]
            if hasattr(val, '__dict__'):
                data[key] = self.dict_attr_traversal(val.__dict__)
            elif isinstance(val, list):
                # valid since both val and data[key] points to the list, and we change the elements in the list that
                # those two variables point to.
                data[key] = self.__arbitrary_list_depth_traversal(val)
            # If we need to check for the possibility of an attribute referring to a dictionary then a
            # a conditional check like for the list should be sufficient.
        # The climbing_up part.
        return data

    def __arbitrary_list_depth_traversal(self, lst: list):
        """
            Recursively traverse lists of arbitrary depth, and extract any __dict__ attribute of objects inside that
            have it. This is a helper method for the __dict_attr_traversal method.
            Parameters:
                lst (list): a list of arbitrary depth.
        """
        for i in range(len(lst)):
            if isinstance(lst[i], list):
                lst[i] = self.__arbitrary_list_depth_traversal(lst[i])
            elif hasattr(lst[i], '__dict__'):
                # Extract and encode the attributes of the object having __dict__ as usual.
                lst[i] = self.dict_attr_traversal(lst[i].__dict__)
        return lst