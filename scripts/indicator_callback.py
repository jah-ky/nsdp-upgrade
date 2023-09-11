import os
from io import StringIO
import csv
import json

def indicator_callback(indicator):
    """
    Perform any actions needed after the build, per indicator.
    """
    
    show_map = indicator.get_meta_field_value('data_show_map')
    map_points = indicator.get_meta_field_value('map_points')
    if show_map and map_points:
        for map_point in map_points:
            data = read_map_points_csv(os.path.abspath(map_point['input']))
            geojson = generate_geojson_data(data)
            write_geojson_data(geojson, map_point['output'])


def read_map_points_csv(filepath):
    rows = []
    with open(filepath) as file:
        data = file.read()
        f = StringIO(data)
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            rows.append(row)
        return rows


def generate_geojson_data(data):
    geojson = {
        'type': 'FeatureCollection',
        'features': [],
    }
    for row in data:
        if 'latitude' in row and 'longitude' in row:
            properties = {}
            for key in row:
                if key == 'latitude' or key == 'longitude':
                    continue
                properties[key] = row[key]
            geojson['features'].append({
                'type': 'Feature',
                'properties': properties,
                'geometry': {
                    'type': 'Point',
                    'coordinates': [row['longitude'], row['latitude']],
                },
            })
    return geojson


def write_geojson_data(data, output_path):
    for language in ['en', 'untranslated']:
        output_folder = os.path.join('_build', language, 'geojson')
        output_file = os.path.abspath(os.path.join(output_folder, output_path))
        with open(output_file, 'w') as f:
            json.dump(data, f)
