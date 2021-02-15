import datetime, csv, logging

files = ["1.csv", "2.csv", "3.csv", "4.csv", "5.csv", "6.csv", "7.csv"]
rows = []


def read_file(file):
    global rows
    try:
        with open(file) as csvfile:
            inputcsv = csv.reader(csvfile, delimiter=',')
            rows = list(inputcsv)
        logging.info(file + " - успешно прочитан")
        return True
    except Exception as e:
        print("Ошибка открытия файла: ", file, str(e))
        logging.error("Ошибка открытия файла: " + file + " " + str(e))
        return False


def write_file(file):
    try:
        with open(file, "a", newline="") as csvfile:
            output = csv.writer(csvfile)
            for row in rows:
                output.writerow(row)
        logging.info("Успешно скопирован в " + file)
    except IOError:
        print("Ошибка записи: ", file)
        logging.error("Ошибка записи в файл: " + file)


dt_str = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
result_file = dt_str+"_result.csv"
logfile = 'python_' + dt_str + '.log'
logging.basicConfig(filename=logfile, level=logging.DEBUG, format='%(asctime)s_%(levelname)s: %(message)s')


for file in files:
    if read_file(file):
        write_file(result_file)

