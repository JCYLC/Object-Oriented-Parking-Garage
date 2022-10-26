class ParkingGarage():
    def __init__(self,tickets=[],parkingspaces=[],currentticket={}):
        self.tickets = tickets
        self.parkingspaces = parkingspaces
        self.currentticket = currentticket

    def logic(self):
        while True:
            answer = input('What would you like to do? enter/leave/show/done? ')
            if answer == 'done':
                break
            elif answer == 'enter':
                ParkingGarage.takeTicket(self)
            elif answer == 'leave':
                ParkingGarage.Leave(self)
            elif answer == 'show':
                ParkingGarage.Show(self)

    def takeTicket(self):
        if len(self.tickets) == 0: 
            print('It is full,come later')

        elif len(self.tickets) <= 9:
            newticket = self.tickets.pop()
            print(f'here is your ticket number: {newticket}')
            parkingspace = self.parkingspaces.pop()
            print(f'here is your parking space number: {parkingspace}')
            self.currentticket[newticket] = "unpaid"
    def Show(self):
        parkingnumber = int(input('what is your ticket number? '))
        if self.currentticket[parkingnumber] == 'paid':
            print('Your ticket has been paid and you have 15 mins to leave. Thank you, have a nice day')
        else:
            print(f'please select leave or done button')

    def Leave(self):
        parkingnumber = int(input('what is your ticket number? '))
        
        if self.currentticket[parkingnumber] == 'unpaid':
            print(f'Pleave pay $5 now')
            self.currentticket[parkingnumber] = 'paid'
            self.tickets.append(parkingnumber)
            self.parkingspaces.append(parkingnumber)
        if self.currentticket[parkingnumber] == 'paid':
            print('Your ticket has been paid and you have 15 mins to leave. Thank you, have a nice day')
        
happyparking = ParkingGarage([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],{})
happyparking.logic()





