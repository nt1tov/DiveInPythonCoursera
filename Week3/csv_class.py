import csv 
import os





class CarBase:
    car_type = None
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
    def get_photo_file_ext(self):
        '''getting file extension'''
        _, ext = os.path.splitext(self.photo_file_name)
        return ext


class Car(CarBase):
    car_type = "car"
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__( brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = "truck"
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        whl_strlist = body_whl.split('x')
        whl_floatlist = []
        if len(whl_strlist) != 3:
            whl_floatlist =  [0.0, 0.0, 0.0]
        else:
            for elem in whl_strlist:
                if elem == "":
                    whl_floatlist = [0.0, 0.0, 0.0]
                    break
                float_elem = float(elem)
                if float_elem < 0 :
                    whl_floatlist =  [0.0, 0.0, 0.0]
                    break
                whl_floatlist.append(float_elem)
        self.body_length,  self.body_width,  self.body_height = whl_floatlist

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = "spec_machine"
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    ext_set = {".jpg", ".jpeg", ".png", ".gif"}
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            #print(row)
            new_car = None
            if len(row) < 7:
                continue
            if not row[0] or not row[1] or not row[3] or not row[5]:
                continue
            if float(row[5]) < 0:
                continue
            if row[0] == "car":
                if not row[2]:
                    continue
                new_car = Car(row[1], row[3], row[5], row[2])
            if row[0] == "truck":
                new_car = Truck(row[1], row[3], row[5], row[4])
            if row[0] == "spec_machine":
                if not row[6]:
                    continue
                new_car = SpecMachine(row[1], row[3], row[5], row[6])
            if(not (new_car.get_photo_file_ext() in ext_set)):
                continue
            car_list.append(new_car)
    return car_list


# cars = []
# cars.append(Truck('Nissan', 't1.jpg', '2.5', ''))

# cars = get_car_list('cars.csv')
# print(cars)


# for car in cars:
#     print(car.brand, car.carrying, car.photo_file_name)
  