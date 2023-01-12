import json


class BusCompany:
    def __init__(self):
        self.bus_data = ''
        self.json_bus_data = {}
        self.results_summary = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}

    def load_bus_data_from_input(self):
        data = input()
        self.bus_data = data
        if not self.bus_data:
            print('No data')
        else:
            json_data = json.loads(self.bus_data)
            if json_data:
                self.json_bus_data = json_data
                self.validate_bus_data()

    def validate_bus_data(self):
        for bus_entry in self.json_bus_data:
            self.validate_bus_ids(bus_entry)
            self.validate_stop_ids(bus_entry)
            self.validate_stop_names(bus_entry)
            self.validate_next_stops(bus_entry)
            self.validate_stop_types(bus_entry)
            self.validate_a_times(bus_entry)
        self.print_results_summary()

    def validate_bus_ids(self, bus_entry):
        bus_id = bus_entry['bus_id']
        # print(f"bus_id: {bus_id}")
        if bus_id == '' or type(bus_id) != int:
            self.results_summary['bus_id'] += 1

    def validate_stop_ids(self, bus_entry):
        stop_id = bus_entry['stop_id']
        # print(f"stop_id: {stop_id}")
        if stop_id == '' or type(stop_id) != int:
            self.results_summary['stop_id'] += 1

    def validate_stop_names(self, bus_entry):
        stop_name = bus_entry['stop_name']
        # print(f"stop_name: {stop_name}")
        if stop_name == '' or type(stop_name) != str:
            self.results_summary['stop_name'] += 1

    def validate_next_stops(self, bus_entry):
        next_stop = bus_entry['next_stop']
        # print(f"next_stop: {next_stop}")
        if next_stop == '' or type(next_stop) != int:
            self.results_summary['next_stop'] += 1

    def validate_stop_types(self, bus_entry):
        stop_type = bus_entry['stop_type']
        # print(f"stop_type: {stop_type}")
        if type(stop_type) != str or len(stop_type) > 1:
            self.results_summary['stop_type'] += 1

    def validate_a_times(self, bus_entry):
        a_time = bus_entry['a_time']
        # print(f"a_time: {a_time}")
        if type(a_time) != str or ':' not in a_time:
            self.results_summary['a_time'] += 1

    def print_results_summary(self):
        # print(self.json_bus_data)
        print(f"Type and required field validation: {sum(self.results_summary.values())} errors")
        print(f"bus_id: {self.results_summary['bus_id']}")
        print(f"stop_id: {self.results_summary['stop_id']}")
        print(f"stop_name: {self.results_summary['stop_name']}")
        print(f"next_stop: {self.results_summary['next_stop']}")
        print(f"stop_type: {self.results_summary['stop_type']}")
        print(f"a_time: {self.results_summary['a_time']}")


if __name__ == '__main__':
    bus_company = BusCompany()
    bus_company.load_bus_data_from_input()

