from __future__ import print_function

from google.oauth2 import service_account
from googleapiclient.discovery import build


class Spreadsheet:
    # If modifying these scopes, delete the file token.json.

    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    CREDENTIALS_FILE = "google-credentials.json"

    # The ID and range of a sample spreadsheet.
    SPREADSHEET_ID = "1zbszu3Ar5XOzZQ5UP_0nFzMaum9cbQmVLjm4IwPs2cY"
    WRITE_RANGE = "user_posts"
    READ_RANGE = "user_posts"
    SHEET_NAME = "user_posts"

    def __init__(self):
        self.sheet = self.get_sheet()

    def get_sheet(self):
        """
        get the spreadsheet
        """
        creds = None
        creds = service_account.Credentials.from_service_account_file(
            self.CREDENTIALS_FILE
        )

        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()

        return sheet

    def read(self) -> list:
        """read the spreadsheet

        Returns:
            list: [description]
        """
        result = (
            self.sheet.values()
            .get(spreadsheetId=self.SPREADSHEET_ID, range=self.READ_RANGE)
            .execute()
        )
        return result.get("values", [])

    def write(self, values_to_write) -> list:
        """read the spreadsheet

        Args:
            values_to_write ([list]): [nested list to enter the value in rows of spreadsheet]

        Returns:
            list: [description]
        """
        # clear the sheet before wiriting the new data
        self.clear()

        request = self.sheet.values().update(
            spreadsheetId=self.SPREADSHEET_ID,
            range=self.WRITE_RANGE,
            valueInputOption="USER_ENTERED",
            body={"values": values_to_write},
        )
        return request.execute()

    def clear(self) -> list:
        return (
            self.sheet.values()
            .clear(spreadsheetId=self.SPREADSHEET_ID, range=self.SHEET_NAME)
            .execute()
        )
