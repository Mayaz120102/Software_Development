class Hall:
    def __init__(self, hall_no, row, col):
        self.row = row
        self.col = col
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

    def enter_show(self, show_id, movie_name, time):
        self.tuple = (show_id, movie_name, time)
        self.show_list.append(self.tuple)
        self.seat_list = []
        for i in range(self.row):
            row = []
            for j in range(self.col):
                row.append("f")
            self.seat_list.append(row)
        self.seats[show_id] = self.seat_list

    def view_show_list(self):
        for x in self.show_list:
            print("show id: ", x[0], "\t Movie: ", x[1], "\t Time: ", x[2])

    def view_avaible_seats(self, id):
        for i in self.show_list:
            if i[0] == id:
                print("\n Movie: ", i[1], "\t\t Time : today at", i[2], "\n\n")
        for x in range(self.row):
            for y in range(self.col):
                if self.seats[id][x][y] == "f":
                    print(f"{chr(x + 65)}{y + 1}", end="\t")
                else:
                    print("X", end="\t")
                # print(self.seats[id][x],end=' ')
            print("\n")

    # def book_tickets(self, id, name, phone, booking_seats):
    #     for x in booking_seats:
    #         r = x[0] - 65


my_hall = Hall(2, 6, 8)
my_hall.enter_show(123, "DOM", "1.00pm")
my_hall.enter_show(105, "dleh", "1.00pm")
my_hall.enter_show(106, "clhe", "1.00pm")
my_hall.enter_show(107, "bleh", "1.00pm")
# print(my_hall.view_show_list)

while True:
    print("\n--------------------------------------------------------\n")
    print("1. View all show today: ")
    print("2. Available seats: ")
    print("3. Book tickets")

    option = int(input("Enter you option: "))
    if option == 1:
        print("\n--------------------------------------------------\n")
        my_hall.view_show_list()
    elif option == 2:
        id = int(input("enter show id: "))
        my_hall.view_avaible_seats(id)
    elif option == 3:
        id = int(input("enter show id: "))
        name = input("enter you name: ")
        phone = input("Enter the phone number: ")
        # tickets =

        # booking_seats = []
        # for i in range(tickets):
    else:
        print("wrong")
