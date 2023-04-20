class DNS:
    def __init__(self, api_wall_service):
        self.api_wall_service = api_wall_service

    def get_data(self, command=None):
        data = self.api_wall_service.fetch_data_from_source("dns")
        if command:
            response = self.execute_api_command(command, data=data)
            return response
        return data

    def execute_api_command(self, command, data=None):
        response = self.api_wall_service.execute_api_function("dns", command, data)
        return response
