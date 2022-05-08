def calculateChildTicketCost(AdultTicketCost,No_Of_Children):
    return float(AdultTicketCost/3) * No_Of_Children

def calculateAdultTicketCost(AdultTicketCost,No_Of_Adults):
    return AdultTicketCost * No_Of_Adults

def calculateAmountAfterServiceTax(TotalAmount,serviceTax):
    return TotalAmount + (TotalAmount*serviceTax)

def calculateDiscount(Amount,Discount):
    return Amount - (Amount*Discount)


def calculate_total_ticket_cost(No_Of_Adults, No_Of_Children):
    total_ticket_cost=0
    #Write your logic here
    childTicketCost = calculateChildTicketCost(37550.0, No_Of_Children)
    AdultTicketCost = calculateAdultTicketCost(37550.0, No_Of_Adults)
    AmountWithTax = calculateAmountAfterServiceTax(childTicketCost + AdultTicketCost, 0.07)
    total_ticket_cost = calculateDiscount(AmountWithTax, 0.1)
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)