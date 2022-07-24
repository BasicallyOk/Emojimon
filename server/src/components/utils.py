import copy
import json


class Utils:
  """A class containing various utility methods along with some helper methods for those utility methods"""
  def json_encoder(obj):
    """
    Handles encoding and loading the state of the emojimon into a JSON file.
    Capable of handling objects with objects and lists of arbitrary depths that could contain
    objects inside it.
    Precondition: For now, the object must have the get_id() method.
    Parameters:
      obj: An object.
    """

    def __dict_traversal(data: dict):
      """
      Recursively extract the data from the object's __dict__ attribute (also its other dictionary attributes)
      along with any attributes that are objects.
      Work in tandem with the __arbitrary_list_depth_traversal method.
      Parameters:
        data (dict): the __dict__ attribute (or other dictionary attributes) of the object
      """
      for key in data.keys():
        val = data[key]
        if hasattr(val, '__dict__'):
          data[key] = __dict_traversal(val.__dict__)
        elif isinstance(val, list):
          # valid since both val and data[key] points to the list, and we change the elements in the list that
          # those two variables point to.
          data[key] = __arbitrary_list_depth_traversal(val)
        elif isinstance(val, dict):
          data[key] = __dict_traversal(val)
      # The climbing_up part recursion-wise.
      return data


    def __arbitrary_list_depth_traversal(lst: list):
      """
      Recursively traverse lists of arbitrary depth, and extract any __dict__ attribute of objects inside that
      have it. Work in tandem with the __dict_traversal method.
      Parameters:
        lst (list): a list of arbitrary depth.
      """
      for i in range(len(lst)):
        if isinstance(lst[i], list):
          lst[i] = __arbitrary_list_depth_traversal(lst[i])
        elif hasattr(lst[i], '__dict__'):
          # Extract and encode the attributes of the object having __dict__ as usual.
          lst[i] = __dict_traversal(lst[i].__dict__)
      return lst


    # Shallow copy.
    data = copy.copy(obj.__dict__)
    data = __dict_traversal(data)
    # TODO: Write to an object instead of a file
    with open(f"{obj.get_id()}.json", mode="w+", encoding="UTF-8") as f:
      json.dump(data, f, indent=2)


  def write_to_db(db_name, data):
    """
    Writes data to a database.
    Parameters:
      db_name (str): the name of the database.
      data (dict): the data to be written to the database.
    """
    pass