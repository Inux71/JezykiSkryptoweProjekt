import os
from datetime import datetime
from datetime import date


def load_data(directory: str):
    data = []
    path = os.listdir(directory)
    for file in path:
        f = open(str(directory + file))
        data.append(f.readlines())
        f.close()
    return data


def generate_template():
    template = ''
    for i in range(0, len(input_files)):
        template += '''
        <div class="line">
            <div class="data">
        '''
        for j in input_files[i]:
            template += f'''
                <div class="input">{j}</div>
            '''
        template += f'''
            </div>
            <div class="data">{output_files[i][0]}</div>
        </div>'''
    return template


def print_data():
    time = datetime.now()
    time = time.strftime("%H-%M-%S")
    today = date.today()
    today = today.strftime("%d-%m-%Y")
    file = open(f'./raporty/{today}_{time}_raport.html', 'w')
    file.write(f'''
    <!DOCTYPE HTML>
    <html lang="pl-PL">
        <head>
            <meta charset="utf-8">
            <title>{today}_{time}_Raport</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <link rel="stylesheet" href="../style.css">
        </head>

        <body>
            <h1>Kacper Grabiec</h1>
            <h3>Jezyki Skryptowe PIONEK</h3>
            {generate_template()}
        </body>
    </html>
    ''')
    file.close()


input_files = load_data('./input_data/')
output_files = load_data('./output_data/')

print_data()