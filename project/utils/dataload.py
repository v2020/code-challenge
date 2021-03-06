import json
import logging
from typing import Any, Dict, List, Optional, Union


class VulnerabilityDataBase:
    """Load vulnerability data"""

    def get_list(self):
        raise NotImplementedError()

    def get_item(self):
        raise NotImplementedError()


logger = logging.getLogger(__name__)


class VulnerabilityDataJson(VulnerabilityDataBase):
    """Load CSV data from a file"""

    def __init__(self, file_name: str):
        self._file_name = file_name
        self._load()

    def _check_data(self):
        # Not implemented
        return False

    def _load(self):
        """Load Json data"""
        self._data = []
        with open(self._file_name, "r") as f:
            self._data = json.load(f)

        if not self._data:
            raise Exception("The data validation has failed")

        if self._check_data():
            raise Exception("The data file is empty")

        logger.info(
            "The Json data file is successfully loaded",
        )

    def get_list(self):
        return self._data["items"]

    def get_item(self, id) -> Union[Dict[str, Any], None]:
        return next((i for i in self._data["items"] if i["_id"] == id), None)


class VulnerabilityDataXml(VulnerabilityDataBase):
    """Load XML data from a file (not implemented)"""

    pass
