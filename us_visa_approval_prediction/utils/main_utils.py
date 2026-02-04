import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from us_visa_approval_prediction.exception import USvisaException
from us_visa_approval_prediction.logger import logging


def read_yaml_file(file_path: str) -> dict:
    """
    Read and parse a YAML configuration file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Parsed content of the YAML file.

    Raises:
        USvisaException: If the file cannot be read or parsed.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise USvisaException(e, sys) from e
    


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Write data to a YAML file, creating directories as needed.

    Args:
        file_path (str): Destination file path.
        content (object): Data to serialize and write.
        replace (bool): If True, replaces an existing file.

    Raises:
        USvisaException: If writing to the file fails.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise USvisaException(e, sys) from e
    



def load_object(file_path: str) -> object:
    """
    Load a serialized Python object from a file using dill.

    Args:
        file_path (str): File path of the serialized object.

    Returns:
        object: Deserialized Python object.

    Raises:
        USvisaException: If loading fails.
    """
    logging.info("Entered the load_object method of utils")

    try:

        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)

        logging.info("Exited the load_object method of utils")

        return obj

    except Exception as e:
        raise USvisaException(e, sys) from e
    


def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save a NumPy array to disk as a binary .npy file.

    Args:
        file_path (str): Destination path for the .npy file.
        array (np.array): NumPy array to save.

    Raises:
        USvisaException: If saving fails.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise USvisaException(e, sys) from e
    



def load_numpy_array_data(file_path: str) -> np.array:
    """
    Load a NumPy array from a binary .npy file.

    Args:
        file_path (str): Path to the saved .npy file.

    Returns:
        np.array: Loaded NumPy array.

    Raises:
        USvisaException: If loading fails.
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise USvisaException(e, sys) from e




def save_object(file_path: str, obj: object) -> None:
    """
    Serialize and save a Python object to disk using dill.

    Args:
        file_path (str): Destination file path.
        obj (object): Python object to serialize and save.

    Raises:
        USvisaException: If serialization fails.
    """
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise USvisaException(e, sys) from e



def drop_columns(df: DataFrame, cols: list)-> DataFrame:
    """
    Drop specified columns from a Pandas DataFrame.

    Args:
        df (DataFrame): Input DataFrame.
        cols (list): List of column names to remove.

    Returns:
        DataFrame: DataFrame after removing specified columns.

    Raises:
        USvisaException: If the operation fails.
    """
    
    logging.info("Entered drop_columns methon of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")
        
        return df
    except Exception as e:
        raise USvisaException(e, sys) from e
    