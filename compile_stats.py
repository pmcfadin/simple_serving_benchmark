import json
import csv
import os

def read_json_files(directory):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                row = extract_data(json_data)
                row.insert(0, filename[:-5])  # Remove '.json' extension
                data.append(row)
    return data

def extract_data(json_data):
    row = [
        json_data.get('base_url', ''),
        json_data.get('total_requests', ''),
        json_data.get('failed_requests', ''),
        json_data.get('requests_per_second', ''),
        json_data.get('dns_median', ''),
        json_data['tcp_connect']['mean'],
        json_data['tcp_connect']['median'],
        json_data['tcp_connect']['95th_percentile'],
        json_data['server_processing']['mean'],
        json_data['server_processing']['median'],
        json_data['server_processing']['95th_percentile'],
        json_data['content_transfer']['mean'],
        json_data['content_transfer']['median'],
        json_data['content_transfer']['95th_percentile']
    ]
    return row

def write_to_csv(data, output_file):
    header = ['filename', 'base_url', 'total_requests', 'failed_requests', 'requests_per_second',
              'dns_median', 'tcp_connect_mean', 'tcp_connect_median', 'tcp_connect_95th_percentile',
              'server_processing_mean', 'server_processing_median', 'server_processing_95th_percentile',
              'content_transfer_mean', 'content_transfer_median', 'content_transfer_95th_percentile']
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

# Example usage
directory = './test_output/'
output_csv = 'run_stats.csv'
data = read_json_files(directory)
write_to_csv(data, output_csv)
