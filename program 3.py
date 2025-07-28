print("Government of Tamilnadu")
print("Electricty Board")
print("-----------------------")
no1=input("Enter the EB.NO,")
no2=input("Enter the Coustomer Name:")
no3=int(input("Reading for previous Month:"))
no4=int(input("Reading for current Month:"))
total=no4-no3
print("Total unit consumed:",total)
paid=total*5
print("Amount to be paid Rs:",paid)
