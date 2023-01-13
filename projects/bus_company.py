import json
import re


class BusCompany:
    def __init__(self):
        self.bus_data = ''
        self.json_bus_data = {}
        self.bus_line = {}
        self.error_summary = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}
        self.stop_summary = {}

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
            if self.all_data_validations(bus_entry):
                self.add_bus_line_entry(bus_entry)
        # self.print_error_summary()
        # self.print_stop_summary()
        if self.validate_bus_lines():
            self.print_bus_line_summary()

    def all_data_validations(self, bus_entry):
        return self.validate_bus_ids(bus_entry) and self.validate_stop_ids(bus_entry) and \
            self.validate_stop_names(bus_entry) and self.validate_next_stops(bus_entry) and \
            self.validate_stop_types(bus_entry) and self.validate_a_times(bus_entry)

    def validate_bus_ids(self, bus_entry):
        bus_id = bus_entry['bus_id']
        # print(f"bus_id: {bus_id}")
        if bus_id == '' or type(bus_id) != int:
            self.error_summary['bus_id'] += 1
            return False
        else:
            return True

    def validate_stop_ids(self, bus_entry):
        stop_id = bus_entry['stop_id']
        # print(f"stop_id: {stop_id}")
        if stop_id == '' or type(stop_id) != int:
            self.error_summary['stop_id'] += 1
            return False
        else:
            return True

    def validate_stop_names(self, bus_entry):
        stop_name = bus_entry['stop_name']
        # print(f"stop_name: {stop_name}")
        if stop_name == '' or type(stop_name) != str:
            self.error_summary['stop_name'] += 1
            return False
        else:
            template = r'(\A[A-Z]+[a-z]+(\s[A-Z]+[a-z]+)?)[\s](Road|Avenue|Boulevard|Street)\Z'
            if not re.match(template, stop_name):
                self.error_summary['stop_name'] += 1
                return False
            else:
                return True

    def validate_next_stops(self, bus_entry):
        next_stop = bus_entry['next_stop']
        # print(f"next_stop: {next_stop}")
        if next_stop == '' or type(next_stop) != int:
            self.error_summary['next_stop'] += 1
            return False
        else:
            return True

    def validate_stop_types(self, bus_entry):
        stop_type = bus_entry['stop_type']
        # print(f"stop_type: {stop_type}")
        if type(stop_type) != str or len(stop_type) > 1:
            self.error_summary['stop_type'] += 1
            return False
        else:
            template = r'[SOF]{1}'
            if not re.match(template, stop_type) and len(stop_type) > 0:
                self.error_summary['stop_type'] += 1
                return False
            else:
                return True

    def validate_a_times(self, bus_entry):
        a_time = bus_entry['a_time']
        # print(f"a_time: {a_time}")
        if type(a_time) != str or ':' not in a_time:
            self.error_summary['a_time'] += 1
            return False
        else:
            template = r'\A[0-1][0-9]:[0-5][0-9]\Z'
            if not re.match(template, a_time):
                self.error_summary['a_time'] += 1
                return False
            else:
                return True

    def validate_bus_lines(self):
        for bus_id, bus_stop in self.bus_line.items():
            if len(bus_stop['start']) != 1 or len(bus_stop['finish']) != 1:
                print(f'There is no start or end stop for the line: {bus_id}.')
                return False
        return True

    def add_bus_line_entry(self, bus_entry):
        bus_id = bus_entry['bus_id']
        stop_id = bus_entry['stop_id']
        stop_name = bus_entry['stop_name']
        next_stop = bus_entry['next_stop']
        stop_type = bus_entry['stop_type']
        a_time = bus_entry['a_time']

        if bus_id not in self.stop_summary:
            self.stop_summary[bus_id] = 1
        else:
            self.stop_summary[bus_id] += 1

        if bus_id not in self.bus_line:
            bus_stop = {'start': set(), 'interim': set(), 'finish': set()}
            if stop_type == 'S':
                bus_stop['start'].add(stop_name)
            elif stop_type == '' or stop_type == 'O':
                bus_stop['interim'].add(stop_name)
            elif stop_type == 'F':
                bus_stop['finish'].add(stop_name)
            self.bus_line[bus_id] = bus_stop
        else:
            if stop_type == 'S':
                self.bus_line[bus_id]['start'].add(stop_name)
            elif stop_type == '':
                self.bus_line[bus_id]['interim'].add(stop_name)
            elif stop_type == 'F':
                self.bus_line[bus_id]['finish'].add(stop_name)

    def print_error_summary(self):
        # print(self.json_bus_data)
        print(f"Type and required field validation: {sum(self.error_summary.values())} errors")
        print(f"bus_id: {self.error_summary['bus_id']}")
        print(f"stop_id: {self.error_summary['stop_id']}")
        print(f"stop_name: {self.error_summary['stop_name']}")
        print(f"next_stop: {self.error_summary['next_stop']}")
        print(f"stop_type: {self.error_summary['stop_type']}")
        print(f"a_time: {self.error_summary['a_time']}")

    def print_stop_summary(self):
        print('Line names and number of stops:')
        for bus_id, stop_count in self.stop_summary.items():
            print(f'bus_id: {bus_id}, stops: {stop_count}')

    def print_bus_line_summary(self):
        start_list = set()
        transfer_list = set()
        finish_list = set()
        for bus_id, bus_stop in self.bus_line.items():
            start_list.add(*bus_stop["start"])
            finish_list.add(*bus_stop["finish"])
            all_stops = bus_stop["start"].union(bus_stop["interim"]).union(bus_stop["finish"])
            for other_id, other_stop in self.bus_line.items():
                if bus_id != other_id:
                    other_all_stops = other_stop["start"].union(other_stop["interim"]).union(other_stop["finish"])
                    if all_stops.intersection(other_all_stops):
                        transfer_list = transfer_list.union(all_stops.intersection(other_all_stops))
        print(f'Start stops: {len(start_list)} {sorted(list(start_list))}')
        print(f'Transfer stops: {len(transfer_list)} {sorted(list(transfer_list))}')
        print(f'Finish stops: {len(finish_list)} {sorted(list(finish_list))}')


if __name__ == '__main__':
    bus_company = BusCompany()
    bus_company.load_bus_data_from_input()

