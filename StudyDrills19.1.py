#LPTHW Study Drill from Ex19

#Define your own function.
def froome_salbutamuol_case(the_decision_limit, froome_sample):
    print("Everything you need to know about Froome's salbutamol case:")
    print(f"The dicision limit is {the_decision_limit}, But Froome's sample is {froome_sample}")


#The first way is giving the funciton numbers directly
froome_salbutamuol_case(1000, 2000)

#Let's do some math
froome_salbutamuol_case(200*5, 200*10)

#We can assign number to variables.
the_limit = 1000
the_real_number = 2000
froome_salbutamuol_case(the_limit, the_real_number)

#It's also a good way to combine math and variables.
froome_salbutamuol_case(the_limit+0, the_real_number+0)

#More tricky skills
froome_salbutamuol_case(the_limit+50*4, the_real_number+20*0)

#More variables...
useless_uci = 0
stupid_wada = 0
froome_salbutamuol_case(the_limit + useless_uci, the_real_number+stupid_wada)

#And input from the user
print("What's the limit of salbutamuol?")
the_limit_input = input("> ")
print("What's the froome's sample's salbutamol level?")
the_froome_real_number_input = input("> ")
froome_salbutamuol_case(the_limit_input, the_froome_real_number_input)

#As Zed mentioned in Common Student Questions, it's possible to call a function within a function.
#But I failed with this one :( 
#So, I will try it later, someday in the future.

#Ok, I can do this after learing Ex21. Because I know how to use "return".

def the_second_fun(x, y):
    print("Ok, we don't trust team sky and froom")
    return x + y

froome_salbutamuol_case(1000, the_second_fun(1200, 1300))
