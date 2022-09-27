from ipostal import ipost_parse


if __name__ == '__main__':
    parsed_data = ipost_parse('The Book Club 100-106 Leonard St, Shoreditch, London, Greater London, EC2A 4RH, United Kingdom')
    print(parsed_data)