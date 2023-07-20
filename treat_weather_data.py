"""
Python file for conducting tests on weather app.
Conversion to pdf or other file types will be made with PANDOC at github actions!
"""

import json
from datetime import datetime as dt
import pytz

## input variables
FN = 'output/weather-output.json'
OUTPUT = 'output/README.md'
TITLE = "⛅ COSTA DA CAPARICA!"

def forecast_date():
    """Function to get forecast date"""
    source_date = dt.now()
    source_timezone = pytz.timezone('UTC')
    source_date_with_timezone = source_timezone.localize(source_date)
    target_time_zone = pytz.timezone('Europe/Lisbon')
    target_date_with_timezone = source_date_with_timezone.astimezone(target_time_zone)
    target_date_str = target_date_with_timezone.strftime('%d of %b at %H:%M')
    return target_date_str

date_now = forecast_date()
print(f'Forecasted at {date_now}')

class ConvertJson():
    """Class converting json"""

    def __init__(self, json_fp, h1_heading):
        self.fp_filename = json_fp
        self.h1_heading = h1_heading
        self.jdata = self.get_json()
        self.mddata = self.format_json_to_md()

    def get_json(self):
        """Function to open json file and load"""        
        with open(self.fp_filename, encoding='utf-8') as json_file:
            res = json.load(json_file)
        return res

    def convert_json_to_txt(self, output_fn):
        """Function to transform json data to text"""
        with open(output_fn, 'w', encoding='utf-8') as json_file:
            json.dump(self.jdata, json_file)
        print('Json file successfully converted to txt')

    def format_json_to_md(self):
        """Function to transform json data to md"""
        text = f'# {self.h1_heading}\n'
        text += f'Forecast date {date_now}'
        data_list = self.jdata
        for dct in data_list:
            localized_date = localize_date(dct["dt_txt"])
            text += f'## Forecast for {localized_date}\n'
            text += f'### {dct["weather"][0]["description"]}\n'
            text += '#### Main data info\n'
            print(dct['main'])
            for content_header, content_data in dct['main'].items():
                text += f'**{content_header}**: {content_data}\n'
            text += '#### 🪁 Main wind info\n'
            for content_header, content_data in dct['wind'].items():
                if content_header == 'deg':
                    text += f'**{content_header}**: {content_data} degrees\n'
                else:
                    converted_data = convert_knots(content_data)
                    text += f'**{content_header}**: {converted_data} knots\n'
            text += '\n'
        return text

    def convert_dict_to_md(self, output_fn):
        """ Function to transform json dictionary to md """
        with open(output_fn, 'w', encoding='utf-8') as writer_file:
            writer_file.writelines(self.mddata)
        print('Dict successfully converted to md')

def convert_knots(wind_value):
    """ Function to convert wind in m/s into knots """
    wind_value *= 1.94384
    converted_value = round(wind_value)
    return converted_value

def localize_date(utc_date):
    """Function to localize date"""
    source_date = dt.strptime(utc_date, '%Y-%m-%d %H:%M:%S')
    source_timezone = pytz.timezone('UTC')
    source_date_with_timezone = source_timezone.localize(source_date)
    target_time_zone = pytz.timezone('Europe/Lisbon')
    target_date_with_timezone = source_date_with_timezone.astimezone(target_time_zone)
    target_date_str = target_date_with_timezone.strftime('%d of %b at %H:%M')
    return target_date_str

def treat_data():
    """ Main function that runs on main """
    converter = ConvertJson(FN, TITLE)
    converter.convert_dict_to_md(output_fn = OUTPUT)

if __name__ == "__main__":
    treat_data()
