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
        """
        Returns the class's workbook.

        Returns
        -------
        Workbook
            The workbook.
        """
        return self._wb

    @property
    def ws(self) -> Worksheet:
        """
        Returns the class's worksheet.

        Returns
        -------
        Worksheet
            The worksheet.
        """
        return self._ws

    def _set_ws(self,
                sheet_name: str,
                ) -> None:
        """
        Sets the class's worksheet.

        Parameters
        ----------
        sheet_name: str
            The name of the worksheet.

        Returns
        -------
        None
        """
        self._ws = self.wb.get_sheet_by_name(sheet_name)
        return

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
