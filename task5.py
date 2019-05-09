"""
===================   TASK 5  ====================
* Create class Vehicle which represents any 
* vehicle and carries general info about the 
* vehicle like: company that built that vehicle, 
* model of the vehicle, year of production, 
* registration number, engine power and color.
* Create method cost_of_registration() that will 
* return how much will registration cost for that 
* instance of vehicle.
*
* Use this formula:

     - Production year fees: 100 EUR  if production year < 1990
                             200 EUR  if production year < 2000
                             300 EUR  if production year < 2010 
                             400 EUR  if production year < 2020
     - On production year fee add engine fee:   (engine power in kw * 2 EUR)
*
* In your main function create single instance of the
* Vehicle class and demonstrate the use of
* cost_of_registration method.
===================================================
"""

# Write your class here

class Vehicle():

    def __init__(self, company, model, year_of_production, registration_number, power, color):
        self.company = company
        self.model = model
        self.year_of_production = year_of_production
        self.registration_numberr = registration_number
        self.power = power
        self.color = color

    def __str__(self):
        return "Company that built that vehicle : {0}, Model of the vehicle: {1}, Year of product: {2}, Registration nuber: {3}, " \
               "Engine power: {4}kW, Colour: {5}".format(self.company, self.model, self.year_of_production, self.registration_numberr, self.power, self.color)

    def cost_of_registration(self):

        if int(self.year_of_production)< 1990:
            production_year_fee = 100
        elif int(self.year_of_production)< 2000:
            production_year_fee = 200
        elif int(self.year_of_production)< 2010:
            production_year_fee = 300
        else:
            production_year_fee = 400

        fee1 = production_year_fee + int(self.power)*2
        return fee1







print("")
vehicleNo1 = Vehicle("Audi", "A4", "2009", "PG-HD258", "77", "red")
print(vehicleNo1)
print("Registration for this vehicle will cost : " + str(Vehicle.cost_of_registration(vehicleNo1)) +" EUR")


def main():
    # Test your function here
    pass

if _name_ == "_main_":
    main()