import os


def load_data(directory: str):
    data = []
    path = os.listdir(directory)
    for file in path:
        f = open(str(directory + file))
        data.append(f.readlines())
        f.close()
    return data


def print_data():
    file = open('raport.html', 'w')
    file.write(f'''
    <!DOCTYPE HTML>
    <html lang="pl-PL">
        <head>
            <meta charset="utf-8"/>
            <title>Raport</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        
        <body>
            {}
        </body>
    </html>
    ''')
    file.close()


input_files = load_data('./input_data/')
output_files = load_data('./output_data/')

print_data()