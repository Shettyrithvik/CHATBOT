class Contact:
    def __init__(self,iname,icontact,idept):
        self.name = iname
        self.contact = icontact
        self.dept = idept

key = input("Enter a key to start")

end1 = "yes"
while end1 == "yes":
    service = int(input("Greetings Welcome to my Chatbot \nWhat brings you to Niveus today? \n1. Services 2. Career Enquiries\n"
              "3. Others   4. About our Products \nEnter your choice"))
    if service == 1:
        choice = int(input("Please select our offerings you are interested in \n1.Infrastructure Modernization 2. Application Modernization \n3. Cloud Security  4. Data Modernization \nEnter your choice"))
        if choice == 1:
            name = input("Enter name")
            contact = input("enter number")
            person1 = Contact(name,contact,"Infrastructure Modernization")
            print("We will get back to you shortly")
        if choice == 2:
            name = input("Enter name")
            contact = input("enter number")
            person1 = Contact(name, contact, "Application Modernization")
            print("We will get back to you shortly")
        if choice == 3:
            name = input("Enter name")
            contact = input("enter number")
            person1 = Contact(name, contact, "Cloud Security")
            print("We will get back to you shortly")
        if choice == 4:
            name = input("Enter name")
            contact = input("enter number")
            person1 = Contact(name, contact, "Data Modernization")
            print("We will get back to you shortly")
    if service == 2:
        print("Visit our Careers Page \033[4mcareers\033[0m")

    if service == 3:
        print("Great, we will contact you shortly please provide your details ")
        name = input("Enter name")
        contact = input("enter number")
        person1 = Contact(name, contact, "Others")
    if service == 4:
        product = int(input("Please choose an option \n1. Nephon: Cloud Management Platform \n2. AssetTraq \nEnter your choice"))
        if product == 1:
            print("Great, we will contact you shortly please provide your details ")
            name = input("Enter name")
            contact = input("enter number")
            person1 = Contact(name, contact, "Nephon")

        else:
            print("Great, we will contact you shortly please provide your details ")
            name = input("Enter name")
            contact = input("enter number")
            person1 = Contact(name, contact, "AssetTraq")
    end1 = input("Do you have other Queries")
    if end1 == "no":
        break
    elif end1 == "yes":
        pass


print("Thank you for visiting us..... Have a great day")









