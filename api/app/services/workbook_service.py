from sqlalchemy.orm import Session
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet


class WorkbookService:
    """
    Handles workbook data operations.
    """

    def __init__(self,
                 session: Session
                 ):
        """
        Initializes the WorkbookService class.
        """
        self._wb: Workbook = None  # TODO: Manage workbook object.
        self._ws = self.wb.active

    @property
    def wb(self) -> Workbook:
        pass

    @property
    def ws(self) -> Worksheet:
        pass

    def _create_wb(self):
        pass

    def add_schedule(self,
                     schedule_dict: dict
                     ) -> None:
        pass

    def _add_schedule_data(self):
        pass

    def _style_ws(self):
        pass




