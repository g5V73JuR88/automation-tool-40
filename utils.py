from typing import List, Dict, Any


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """Flatten a nested list.

    Args:
        nested_list (List[List[Any]]): A list of lists to be flattened.

    Returns:
        List[Any]: A single flattened list.
    """
    return [item for sublist in nested_list for item in sublist]


def merge_dicts(dict_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Merge a list of dictionaries into a single dictionary.

    Args:
        dict_list (List[Dict[str, Any]]): A list of dictionaries to merge.

    Returns:
        Dict[str, Any]: A dictionary containing all key-value pairs from the input dictionaries. If the same key appears in multiple dictionaries, the last value will be retained.
    """
    merged_dict = {}
    for d in dict_list:
        merged_dict.update(d)
    return merged_dict


def chunk_list(data: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks of a specified size.

    Args:
        data (List[Any]): The list to be split into chunks.
        chunk_size (int): The size of each chunk.

    Returns:
        List[List[Any]]: A list containing the chunks.
    """
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]