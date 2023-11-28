# small = 2
# regular = 5
# big = 6
#
# user_budget = input('What is your budget? ')
#
# try:
#     user_budget = int(user_budget)
# except:
#     print('Please enter a number')
#     exit()
#
# if user_budget > 0:
#     if user_budget >= big:
#         print('You can afford the big coffee')
#         if user_budget == big:
#             print('It\'s complete')
#         else:
#             print('Your change is', user_budget - big)
#     elif user_budget == regular:
#         print('You can afford the regular coffee')
#         print('It\'s complete')
#     elif user_budget >= small:
#         print('You can buy the small coffee')
#         if user_budget == small:
#             print('It\'s complete')
#         else:
#             print('Your change is', user_budget - small)
#
# class Coffee:
#     # Constructor
#     def __init__(self, name, price):
#         self.name = name
#         self.price = float(price)
#
#     def check_budget(self, budget):
#         # Check if the budget is valid
#         if not isinstance(budget, (int, float)):
#             print('Enter float or int')
#             exit()
#         if budget < 0:
#             print('Sorry you don\'t have money')
#             exit()
#
#     def get_change(self, budget):
#         return budget - self.price
#
#     def sell(self, budget):
#         self.check_budget(budget)
#         if budget >= self.price:
#             print(f'You can buy the {self.name} coffee')
#             if budget == self.price:
#                 print('It\'s complete')
#             else:
#                 print(f'Here is your change {self.get_change(budget)}$')
#
#             exit('Thanks for your transaction')


class bola:
    def __init__(self, cor = 'red', circunstancia = '16 cm', material = 'ferro'):
        self.cor = cor
        self.circunstancia = circunstancia
        self.material = material

    def Trocacor(self):
        Ncolor = (input("Digite a nova cor da bola:\n"))
        self.cor = Ncolor

    def mostracor(self):
        print("A cor atual é:", self.cor)


futebol = bola()
print(
    f"A bola ter a cor {futebol.cor}, sua circunstancia é {futebol.circunstancia} e seu material é {futebol.material}.")
futebol.Trocacor()
print(f"A nova cor da bola é {futebol.cor}")
futebol.mostracor()
